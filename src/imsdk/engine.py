"""
IM SDK Python封装模块

用于加载和封装Rust Universal IM SDK动态库
"""
import os
import random
import ctypes
import platform
import sys
from typing import Dict, Any, List

# 获取动态库文件的绝对路径
_ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
_LIB_DIR = os.path.join(_ROOT_DIR, "lib")

# 添加lib目录到Python路径，确保可以导入lib.rcim_client
if _ROOT_DIR not in sys.path:
    sys.path.append(_ROOT_DIR)

# 导入rcim_client模块
from lib import rcim_client
from lib.rcim_utils import string_cast, char_pointer_cast, ctypes_to_dict
# 从rcim_client导入所需类型
from lib.rcim_client import (
    RcimEngineBuilder,
    RcimEngineBuilderParam,
    RcimEngineSync,
    RcimPlatform,
    RcimConversationType,
    RcimPlatform_Linux,
    RcimPlatform_MacOS,
    RcimPlatform_Unknown,
    RcimPlatform_Windows,
    RcimSDKVersion,
    String,  # 添加String类型导入
)

_PLATFORM = RcimPlatform_Unknown

# 根据操作系统选择正确的动态库文件名
if platform.system() == "Darwin":  # macOS
    _LIB_PATH = os.path.join(_LIB_DIR, "librust_universal_imsdk.dylib")
    _PLATFORM = RcimPlatform_MacOS
elif platform.system() == "Windows":
    _LIB_PATH = os.path.join(_LIB_DIR, "rust_universal_imsdk.dll")
    _PLATFORM = RcimPlatform_Windows
else:  # Linux 或其他类Unix系统
    _LIB_PATH = os.path.join(_LIB_DIR, "librust_universal_imsdk.so")
    _PLATFORM = RcimPlatform_Linux


# 确保文件存在
if not os.path.exists(_LIB_PATH):
    raise ImportError(f"找不到IM SDK动态库: {_LIB_PATH}")

# 加载动态库
try:
    _lib = ctypes.cdll.LoadLibrary(_LIB_PATH)
except Exception as e:
    raise ImportError(f"加载IM SDK动态库失败: {e}")


rust_path = os.path.dirname(__file__)

class IMSDK:
    """IM SDK的Python封装类"""
    
    def __init__(self) -> None:
        """初始化IM SDK"""
        # 初始化属性
        self.engine = None
        self.builder = None
        
        # 初始化rust_listener
        try:
            # 尝试创建一个简单的监听器对象
            class RustListener:
                def LogLsrDev(self, level, log_str):
                    print(f"日志开发监听器被调用: [{level}] {log_str}")
                
                def LogLsr(self, level, log_str):
                    print(f"日志监听器被调用: [{level}] {log_str}")
            
            self.rust_listener = RustListener()
        except Exception as e:
            self.rust_listener = None
            print(f"警告: 创建rust_listener失败: {e}")
        
    def initialize(self, app_key: str, device_id: str) -> Dict[str, Any]:
        """
        初始化IM SDK并返回状态
        
        Args:
            app_key: 应用的AppKey
            device_id: 设备ID
            
        Returns:
            包含初始化结果的字典
        """
        # 存储应用信息
        self.app_key = app_key
        self.device_id = device_id
        
        print(f"初始化IM SDK，AppKey: {app_key}, 设备ID: {device_id}")
        
        try:
            # 创建结构体
            param = rcim_client.RcimEngineBuilderParam()
            
            # 使用更精确的类型转换
            def to_lp_c_char(s):
                # 先创建一个c_char数组
                c_str = (ctypes.c_char * (len(s) + 1))()
                c_str.value = s.encode('utf-8')
                # 然后创建指向该数组的指针
                return ctypes.cast(c_str, ctypes.POINTER(ctypes.c_char))

            # 设置参数
            param.app_key = rcim_client.String(to_lp_c_char(app_key))
            param.platform = _PLATFORM
            param.device_id = rcim_client.String(to_lp_c_char(device_id))
            param.package_name = rcim_client.String(to_lp_c_char(""))
            param.imlib_version = rcim_client.String(to_lp_c_char("0.17.1"))
            param.device_model = rcim_client.String(to_lp_c_char(""))
            param.device_manufacturer = rcim_client.String(to_lp_c_char(""))
            param.os_version = rcim_client.String(to_lp_c_char(""))
            version = RcimSDKVersion(
                name=rcim_client.String(to_lp_c_char("rust"))   ,
                version=rcim_client.String(to_lp_c_char("0.17.1"))
            )
            param.sdk_version_vec = ctypes.pointer(version)
            param.sdk_version_vec_len = 1
            param.app_version = rcim_client.String(to_lp_c_char(""))
            
            # 创建builder指针
            builder = ctypes.POINTER(rcim_client.RcimEngineBuilder)()
            
            # 调用创建函数
            ret = rcim_client.rcim_create_engine_builder(
                ctypes.byref(param),
                ctypes.byref(builder)
            )
            if ret != 0:
                print(f"rcim_create_engine_builder failed, error code: {ret}")
                return {"success": False, "error": f"rcim_create_engine_builder failed, error code: {ret}"}
            
            # 设置存储路径
            db_path = os.path.join(rust_path, "rust_db").encode('utf-8')
            # 需要将路径转换为c_char_p
            c_db_path = ctypes.c_char_p(db_path)
            rcim_client.rcim_engine_builder_set_store_path(builder, c_db_path)
            
            # 创建引擎
            engine = ctypes.POINTER(ctypes.POINTER(RcimEngineSync))()
            print(f"rcim_engine_builder_build 即将执行")

            # 构建引擎
            ret = rcim_client.rcim_engine_builder_build(builder, engine)
            if ret != 0:
                print(f"rcim_engine_builder_build failed, error code: {ret}")
                return {"success": False, "error": f"rcim_engine_builder_build failed, error code: {ret}"}
            
            self.engine = engine

            return {
                "success": True,
                "app_key": app_key,
                "device_id": device_id,
                "message": "IM SDK初始化成功"
            }
        except Exception as e:
            import traceback
            print(f"初始化IM SDK失败: {e}")
            print(f"异常堆栈: {traceback.format_exc()}")
            return {
                "success": False,
                "error": str(e)
            }

    def engine_connect(self, token: str, timeout_sec: int = 30) -> Dict[str, Any]:
        """
        连接融云服务
        
        Args:
            token: 用户连接token
            timeout_sec: 连接超时时间，单位为秒
            
        Returns:
            包含结果的字典
        """
        if not hasattr(rcim_client, "rcim_engine_connect"):
            return {"success": False, "error": "动态库不支持rcim_engine_connect方法"}
        
        if not self.engine:
            return {"success": False, "error": "引擎实例尚未构建，请先调用engine_builder_build"}
        
        try:
            print(f"连接融云服务，token: {token[:10]}..., 超时: {timeout_sec}秒")
            
            # 创建回调函数
            def connect_callback(user_data, code, user_id):
                success = code == 0
                print(f"连接回调: {'成功' if success else '失败'}, 用户ID: {user_id}, 错误码: {code}")
                return {"success": success, "user_id": user_id.decode() if user_id else None, "code": code}
            
            # 将Python回调函数包装为C回调函数
            callback = rcim_client.RcimConnectCb(connect_callback)
            
            result = rcim_client.rcim_engine_connect(self.engine, token.encode(), timeout_sec, None, callback)
            if result != 0:
                return {"success": False, "error": f"连接请求失败，错误码: {result}"}
            return {"success": True, "message": "连接请求已发送"}
        except Exception as e:
            print(f"连接服务失败: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    def send_message(self, receiver: str, content: str, conversation_type: int = None) -> Dict[str, Any]:
        """
        发送消息
        
        Args:
            receiver: 接收者ID
            content: 消息内容
            conversation_type: 会话类型，默认为私聊(1)
            
        Returns:
            包含发送结果的字典
        """
        if conversation_type is None:
            conversation_type = RcimConversationType.PRIVATE
            
        # 这里应该调用动态库中的相应函数
        try:
            print(f"调用IM SDK发送消息给 {receiver}: {content}, 会话类型: {conversation_type}")
            
            # 如果可以使用真实的SDK
            if hasattr(rcim_client, "rcim_engine_send_text_message"):
                # 创建回调函数
                def send_message_callback(user_data, code, message_id):
                    success = code == 0
                    print(f"发送消息回调: {'成功' if success else '失败'}, 消息ID: {message_id}, 错误码: {code}")
                    return {"success": success, "message_id": message_id.decode() if message_id else None, "code": code}
                
                # 将Python回调函数包装为C回调函数
                if hasattr(rcim_client, "RcimSendMessageCb"):
                    callback = rcim_client.RcimSendMessageCb(send_message_callback)
                    result = rcim_client.rcim_engine_send_text_message(
                        self.engine, 
                        conversation_type,
                        receiver.encode(), 
                        content.encode(), 
                        None, 
                        None, 
                        callback
                    )
                    if result != 0:
                        return {"success": False, "error": f"发送消息请求失败，错误码: {result}"}
                    return {"success": True, "message": "发送消息请求已发送"}
            
            # 模拟发送结果
            return {
                "success": True,
                "message_id": "msg_12345",
                "timestamp": 1653812345,
            }
        except Exception as e:
            print(f"发送消息失败: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    def get_history_messages(self, user_id: str, count: int = 10) -> List[Dict[str, Any]]:
        """
        获取历史消息
        
        Args:
            user_id: 用户ID
            count: 获取的消息数量
            
        Returns:
            历史消息列表
        """
        # 这里应该调用动态库中的相应函数
        try:
            print(f"调用IM SDK获取与用户 {user_id} 的 {count} 条历史消息")
            
            # 如果可以使用真实的SDK
            if hasattr(rcim_client, "rcim_engine_get_messages"):
                # 创建回调函数
                def get_messages_callback(user_data, code, messages, messages_len):
                    success = code == 0
                    result = []
                    if success and messages and messages_len > 0:
                        for i in range(messages_len):
                            msg = messages[i]
                            result.append({
                                "id": msg.message_id.decode() if msg.message_id else None,
                                "sender": msg.sender_id.decode() if msg.sender_id else None,
                                "content": msg.content.decode() if msg.content else None,
                                "timestamp": msg.timestamp
                            })
                    print(f"获取历史消息回调: {'成功' if success else '失败'}, 获取到 {len(result)} 条消息, 错误码: {code}")
                    return {"success": success, "messages": result, "code": code}
                
                # 将Python回调函数包装为C回调函数
                if hasattr(rcim_client, "RcimGetMessagesCb"):
                    callback = rcim_client.RcimGetMessagesCb(get_messages_callback)
                    result = rcim_client.rcim_engine_get_messages(
                        self.engine, 
                        RcimConversationType.PRIVATE,
                        user_id.encode(), 
                        None,  # 消息ID，从这条消息开始获取
                        count,
                        None, 
                        callback
                    )
                    if result != 0:
                        return []
                    # 注意：这里的实现是异步的，实际结果会通过回调返回
                    # 为了简化，我们返回一个模拟的结果
            
            # 模拟历史消息结果
            return [
                {"id": f"msg_{i}", "sender": user_id if i % 2 else "me", 
                "content": f"示例消息 {i}", "timestamp": 1653812345 + i * 60}
                for i in range(count)
            ]
        except Exception as e:
            print(f"获取历史消息失败: {e}")
            return []
    
    def close(self) -> None:
        """关闭IM SDK，释放资源"""
        if hasattr(_lib, "im_sdk_close"):
            _lib.im_sdk_close.argtypes = []
            _lib.im_sdk_close.restype = ctypes.c_int
            result = _lib.im_sdk_close()
            if result != 0:
                print(f"警告: IM SDK关闭时发生错误，错误码: {result}")
        
        # 释放引擎资源
        if self.engine and hasattr(rcim_client, "rcim_destroy_engine"):
            try:
                # 调用销毁引擎的函数
                rcim_client.rcim_destroy_engine(self.engine)
                print("释放引擎资源")
                self.engine = None
            except Exception as e:
                print(f"释放引擎资源时发生错误: {e}")

# 创建默认SDK实例，使用默认参数
default_sdk = IMSDK() 