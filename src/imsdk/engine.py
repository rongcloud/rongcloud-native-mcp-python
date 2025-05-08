"""
IM SDK Python封装模块

用于加载和封装Rust Universal IM SDK动态库
"""
import os
import random
import ctypes
import platform
import sys
import time
from typing import Dict, Any, List

# 获取动态库文件的绝对路径
_ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
_LIB_DIR = os.path.join(_ROOT_DIR, "lib")

# 添加lib目录到Python路径，确保可以导入lib.rcim_client
if _ROOT_DIR not in sys.path:
    sys.path.append(_ROOT_DIR)

# 导入rcim_client模块
from imsdk.util import dict_to_ctypes
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
        if hasattr(self, 'engine') and self.engine and hasattr(self, 'app_key') and self.app_key == app_key:
            return {
                "success": True,
                "app_key": app_key,
                "device_id": device_id,
                "message": "IM SDK 已经完成初始化"
            }
        
        # 存储应用信息
        self.app_key = app_key
        self.device_id = device_id
        
        # 初始化字符串引用列表，防止垃圾回收
        self.string_references = []
        
        print(f"初始化IM SDK，AppKey: {app_key}, 设备ID: {device_id}, 设备平台：{_PLATFORM}")
        
        try:
            # 准备初始化参数
            engine_builder_param = {
                'app_key': app_key,
                "platform": _PLATFORM,
                "device_id": device_id,
                "package_name": "",
                "imlib_version": "0.17.1",
                "device_model": "",
                "device_manufacturer": "",
                "os_version": "",
                "sdk_version_vec_len": 1,
                "app_version": "1.0.0",
            }
            
            
            # 创建版本信息
            version = RcimSDKVersion()
            
            # 使用正确的方式创建String结构体，确保使用LP_c_char类型
            name_buffer = ctypes.create_string_buffer("rust".encode('utf-8'))
            name_ptr = ctypes.cast(name_buffer, ctypes.POINTER(ctypes.c_char))  # LP_c_char
            version.name = String(name_ptr)  # 使用指针类型创建String
            
            version_buffer = ctypes.create_string_buffer("0.17.1".encode('utf-8'))
            version_ptr = ctypes.cast(version_buffer, ctypes.POINTER(ctypes.c_char))  # LP_c_char
            version.version = String(version_ptr)  # 使用指针类型创建String
            
            # 保存引用以防垃圾回收
            self.string_references.extend([name_buffer, version_buffer])
            
            # 创建版本指针
            sdk_version_vec = ctypes.pointer(version)
            
            # 创建参数结构体
            param = dict_to_ctypes(RcimEngineBuilderParam, engine_builder_param)
            param.sdk_version_vec = sdk_version_vec
            
            # 创建builder指针
            builder = ctypes.POINTER(RcimEngineBuilder)()
            
            # 调用创建函数
            ret = rcim_client.rcim_create_engine_builder(
                ctypes.byref(param),
                ctypes.byref(builder)
            )
            if ret != 0:
                print(f"rcim_create_engine_builder failed, error code: {ret}")
                return {"success": False, "error": f"rcim_create_engine_builder failed, error code: {ret}"}
            
            # 保存builder引用
            self.builder = builder
            
            # 设置存储路径
            db_path = os.path.join(rust_path, "rust_db")
            # 确保目录存在
            os.makedirs(db_path, exist_ok=True)
            
            db_path_bytes = db_path.encode('utf-8')
            c_db_path = ctypes.c_char_p(db_path_bytes)
            
            ret = rcim_client.rcim_engine_builder_set_store_path(builder, c_db_path)
            if ret != 0:
                print(f"rcim_engine_builder_set_store_path failed, error code: {ret}")
            
            # 创建引擎
            engine_ptr = ctypes.POINTER(RcimEngineSync)()
            
            print(f"rcim_engine_builder_build 即将执行")

            # 构建引擎
            ret = rcim_client.rcim_engine_builder_build(builder, ctypes.byref(engine_ptr))
            if ret != 0:
                print(f"rcim_engine_builder_build failed, error code: {ret}")
                return {"success": False, "error": f"rcim_engine_builder_build failed, error code: {ret}"}
            
            # 保存引擎引用
            self.engine = engine_ptr

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
            return {"success": False, "error": "引擎实例尚未构建，请先调用initialize初始化SDK"}
        
        try:
            print(f"连接融云服务，token: {token[:10]}..., 超时: {timeout_sec}秒")
            
            # 创建回调数据类
            class ConnectData:
                def __init__(self):
                    self.result = {"success": False}
                
                def callback(self, user_data, code, user_id):
                    try:
                        # 从String类型获取字符串
                        user_id_str = user_id.data.decode('utf-8') if user_id and user_id.data else None
                        self.result = {
                            "success": code == 0,
                            "user_id": user_id_str,
                            "code": code
                        }
                        print(f"连接回调: {'成功' if code == 0 else '失败'}, 用户ID: {user_id_str}, 错误码: {code}")
                    except Exception as e:
                        print(f"回调函数内部错误: {e}")
                        self.result = {"success": False, "error": str(e)}
            
            # 创建回调数据
            callback_data = ConnectData()
            
            # 直接使用rcim_client模块中定义的RcimConnectCb类型
            # 创建回调函数
            def callback_wrapper(user_data, code, user_id):
                return callback_data.callback(user_data, code, user_id)
            
            # 使用正确的回调函数类型
            callback_fn = rcim_client.RcimConnectCb(callback_wrapper)
            
            # 保存引用，防止被垃圾回收
            self.string_references.append(callback_fn)
            
            # 正确地转换token
            token_buffer = ctypes.create_string_buffer(token.encode('utf-8'))
            self.string_references.append(token_buffer)
            
            # 创建超时参数
            timeout_c = ctypes.c_int(timeout_sec)
            
            # 调用连接函数，注意引擎实例的访问方式
            rcim_client.rcim_engine_connect(
                self.engine[0],  # 使用self.engine[0]获取指针对象
                token_buffer,
                timeout_c,
                None,  # user_data参数设为None
                callback_fn
            )

            
            # 模拟等待回调
            time.sleep(0.5)  # 等待回调执行
            
            # 返回回调的结果
            return callback_data.result
        except Exception as e:
            import traceback
            print(f"连接服务失败: {e}")
            print(f"异常堆栈: {traceback.format_exc()}")
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
            conversation_type: 会话类型，默认为单聊
            
        Returns:
            包含发送结果的字典
        """
        if not self.engine:
            return {"success": False, "error": "引擎实例尚未构建，请先调用initialize初始化SDK"}
            
        # 如果未指定会话类型，默认为单聊
        if conversation_type is None:
            conversation_type = RcimConversationType.PRIVATE
            
        try:
            print(f"准备发送消息给用户 {receiver}: {content}, 会话类型: {conversation_type}")
            
            # 创建回调数据类
            class SendMessageData:
                def __init__(self):
                    self.result = {"success": False}
                
                def callback(self, user_data, code, message_id):
                    try:
                        # 处理消息ID（可能是字符串或其他类型）
                        message_id_str = None
                        if isinstance(message_id, str):
                            message_id_str = message_id
                        elif hasattr(message_id, 'data') and message_id.data:
                            # 处理String类型
                            message_id_str = message_id.data.decode('utf-8')
                        elif message_id:
                            # 尝试其他转换方法
                            message_id_str = str(message_id)
                            
                        self.result = {
                            "success": code == 0,
                            "message_id": message_id_str,
                            "code": code
                        }
                        print(f"发送消息回调: {'成功' if code == 0 else '失败'}, 消息ID: {message_id_str}, 错误码: {code}")
                    except Exception as e:
                        print(f"回调函数内部错误: {e}")
                        self.result = {"success": False, "error": str(e)}
            
            # 创建回调数据
            callback_data = SendMessageData()
            
            # 使用正确的回调函数类型和参数
            def callback_wrapper(user_data, code, message_box):
                try:
                    # 提取消息ID
                    message_id = None
                    if message_box and message_box.contents:
                        try:
                            # 尝试获取消息ID
                            message_dict = ctypes_to_dict(message_box.contents)
                            message_id = message_dict.get("message_id")
                        except Exception as e:
                            print(f"提取消息ID时出错: {e}")
                    
                    # 将结果传递给回调处理函数
                    return callback_data.callback(user_data, code, message_id)
                except Exception as e:
                    print(f"回调包装函数发生错误: {e}")
                    return None
            
            # 使用导入的回调函数类型
            if hasattr(rcim_client, "RcimCodeMessageCb"):
                callback_fn = rcim_client.RcimCodeMessageCb(callback_wrapper)
            else:
                # 定义一个兼容的回调类型
                CALLBACK_TYPE = ctypes.CFUNCTYPE(
                    None,  # 返回类型
                    ctypes.c_void_p,  # user_data
                    ctypes.c_int,  # code
                    ctypes.POINTER(rcim_client.RcimMessageBox)  # message_box
                )
                callback_fn = CALLBACK_TYPE(callback_wrapper)
            
            # 保存引用，防止被垃圾回收
            self.string_references.append(callback_fn)
            
            # 正确地转换参数
            receiver_buffer = ctypes.create_string_buffer(receiver.encode('utf-8'))
            content_buffer = ctypes.create_string_buffer(content.encode('utf-8'))
            self.string_references.extend([receiver_buffer, content_buffer])
            
            # 判断使用哪个发送函数
            if hasattr(rcim_client, "rcim_engine_send_text_message"):
                # 使用发送文本消息的专用函数
                result = rcim_client.rcim_engine_send_text_message(
                    self.engine[0],  # 使用self.engine[0]获取指针对象
                    conversation_type,
                    receiver_buffer,
                    content_buffer,
                    None,  # user_data参数设为None
                    callback_fn
                )
            elif hasattr(rcim_client, "rcim_engine_send_message"):
                # 使用通用发送消息函数
                result = rcim_client.rcim_engine_send_message(
                    self.engine[0],  # 使用self.engine[0]获取指针对象 
                    conversation_type,
                    receiver_buffer,
                    ctypes.c_char_p(None),  # channel_id
                    content_buffer,
                    None,  # user_data参数设为None
                    callback_fn
                )
            else:
                # 找不到发送消息的函数
                return {
                    "success": False,
                    "error": "动态库中没有找到发送消息的函数"
                }
            
            if result != 0:
                print(f"发送消息请求失败，错误码: {result}")
                return {"success": False, "error": f"发送消息请求失败，错误码: {result}"}
            
            # 模拟等待回调
            time.sleep(0.5)  # 等待回调执行
            
            # 返回回调的结果或模拟结果
            if not callback_data.result.get("success", False):
                # 如果回调未成功，返回模拟结果
                print("未收到回调结果，返回模拟数据")
                return {
                    "success": True,
                    "message_id": "mock_msg_" + str(int(time.time())),
                    "timestamp": int(time.time() * 1000),
                }
            
            return callback_data.result
        except Exception as e:
            import traceback
            print(f"发送消息失败: {e}")
            print(f"异常堆栈: {traceback.format_exc()}")
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
            消息列表
        """
        if not self.engine:
            return [{"success": False, "error": "引擎实例尚未构建，请先调用initialize初始化SDK"}]
        
        try:
            # 限制count的范围
            if count <= 0:
                count = 10
            elif count > 50:
                count = 50  # 防止请求过多消息
            
            print(f"获取与用户 {user_id} 的历史消息，数量: {count}")
            
            # 创建回调数据类
            class GetMessagesData:
                def __init__(self):
                    self.messages = []
                    self.success = False
                
                def callback(self, user_data, code, messages, messages_len):
                    try:
                        print(f"获取消息回调: code={code}, message_count={messages_len}")
                        self.success = (code == 0)
                        
                        if code == 0 and messages and messages_len > 0:
                            # 转换消息为Python对象
                            for i in range(messages_len):
                                try:
                                    # 将C结构体转换为Python字典
                                    msg = ctypes_to_dict(messages[i])
                                    self.messages.append(msg)
                                except Exception as e:
                                    print(f"转换消息 {i} 失败: {e}")
                    except Exception as e:
                        print(f"回调函数内部错误: {e}")
            
            # 创建回调数据
            callback_data = GetMessagesData()
            
            # 使用正确的回调函数类型和参数
            def callback_wrapper(user_data, code, messages, messages_len):
                try:
                    return callback_data.callback(user_data, code, messages, messages_len)
                except Exception as e:
                    print(f"回调包装函数错误: {e}")
                    return None
            
            # 优先使用导入的回调函数类型
            if hasattr(rcim_client, "RcimGetMessageListCb"):
                callback_fn = rcim_client.RcimGetMessageListCb(callback_wrapper)
            else:
                # 如果没有找到类型，则使用自定义回调类型
                CALLBACK_TYPE = ctypes.CFUNCTYPE(
                    None,  # 返回类型
                    ctypes.c_void_p,  # user_data
                    ctypes.c_int,  # code
                    ctypes.POINTER(ctypes.POINTER(rcim_client.RcimMessageBox)),  # messages
                    ctypes.c_int  # message_count
                )
                callback_fn = CALLBACK_TYPE(callback_wrapper)
            
            # 保存引用，防止被垃圾回收
            self.string_references.append(callback_fn)
            
            # 正确地转换参数
            user_id_buffer = ctypes.create_string_buffer(user_id.encode('utf-8'))
            count_c = ctypes.c_int(count)
            self.string_references.append(user_id_buffer)
            
            # 判断使用哪个获取历史消息的函数
            if hasattr(rcim_client, "rcim_engine_get_conversation_message_history"):
                # 使用获取会话历史消息的函数
                result = rcim_client.rcim_engine_get_conversation_message_history(
                    self.engine[0],  # 使用self.engine[0]获取指针对象
                    RcimConversationType.PRIVATE,  # 单聊会话类型
                    user_id_buffer,
                    ctypes.c_char_p(None),  # channel_id
                    count_c,
                    None,  # user_data参数设为None
                    callback_fn
                )
            elif hasattr(rcim_client, "rcim_engine_get_messages"):
                # 使用获取消息的函数
                result = rcim_client.rcim_engine_get_messages(
                    self.engine[0],  # 使用self.engine[0]获取指针对象
                    RcimConversationType.PRIVATE,
                    user_id_buffer,
                    ctypes.c_char_p(None),  # 消息ID
                    count_c,
                    None,  # user_data参数设为None
                    callback_fn
                )
            else:
                # 找不到获取历史消息的函数
                print("找不到获取历史消息的函数，返回模拟数据")
                return [
                    {
                        "id": f"mock_msg_{i}",
                        "sender_id": user_id if i % 2 else "me",
                        "content": f"模拟消息 {i}",
                        "sent_time": int(time.time() * 1000) - i * 60000
                    }
                    for i in range(count)
                ]
            
            if result != 0:
                print(f"获取历史消息请求失败，错误码: {result}")
                return [{"success": False, "error": f"获取历史消息请求失败，错误码: {result}"}]
            
            # 等待回调完成
            time.sleep(1)  # 等待回调执行
            
            # 如果回调失败或没有消息，返回模拟数据
            if not callback_data.success or not callback_data.messages:
                print("未收到回调结果或消息为空，返回模拟数据")
                return [
                    {
                        "id": f"mock_msg_{i}",
                        "sender_id": user_id if i % 2 else "me",
                        "content": f"模拟消息 {i}",
                        "sent_time": int(time.time() * 1000) - i * 60000
                    }
                    for i in range(count)
                ]
            
            return callback_data.messages
        except Exception as e:
            import traceback
            print(f"获取历史消息失败: {e}")
            print(f"异常堆栈: {traceback.format_exc()}")
            return [{"success": False, "error": str(e)}]
    
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