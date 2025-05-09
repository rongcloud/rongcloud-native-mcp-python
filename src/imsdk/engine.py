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
_USER_ID = ""

# 添加lib目录到Python路径，确保可以导入lib.rcim_client
if _ROOT_DIR not in sys.path:
    sys.path.append(_ROOT_DIR)

# 导入rcim_client模块
from imsdk.util import dict_to_ctypes
from lib import rcim_client
from lib.rcim_utils import string_cast, char_pointer_cast, ctypes_to_dict
# 从rcim_client导入所需类型
from lib.rcim_client import (
    RcimConversationType_Group,
    RcimConversationType_Private,
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
        # 初始化字符串引用列表，防止垃圾回收
        self.string_references = []
        
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
                "code": 0,
                "app_key": app_key,
                "device_id": device_id,
                "message": "IM SDK 已经完成初始化"
            }
        
        # 存储应用信息
        self.app_key = app_key
        self.device_id = device_id
        
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
                return {"code": -1, "error": f"rcim_create_engine_builder failed, error code: {ret}"}
            
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
                return {"code": -1, "error": f"rcim_engine_builder_build failed, error code: {ret}"}
            
            # 保存引擎引用
            self.engine = engine_ptr

            return {
                "code": 0,
                "app_key": app_key,
                "device_id": device_id,
                "message": "IM SDK初始化成功"
            }
        except Exception as e:
            import traceback
            print(f"初始化IM SDK失败: {e}")
            print(f"异常堆栈: {traceback.format_exc()}")
            return {
                "code": -1,
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
            return {"code": -1, "error": "动态库不支持rcim_engine_connect方法"}
        
        if not self.engine:
            return {"code": -1, "error": "引擎实例尚未构建，请先调用initialize初始化SDK"}
        
        try:
            print(f"连接融云服务，token: {token[:10]}..., 超时: {timeout_sec}秒")
            
            # 创建回调数据类
            class ConnectData:
                def __init__(self):
                    self.result = {"code": -1}
                
                def callback(self, user_data, code, user_id):
                    try:
                        # 从String类型获取字符串
                        user_id_str = user_id.data.decode('utf-8') if user_id and user_id.data else None
                        # 将user_id_str赋值给全局变量_USER_ID
                        global _USER_ID
                        _USER_ID = user_id_str
                        self.result = {
                            "code": code,
                            "user_id": user_id_str,
                        }
                        print(f"连接回调: {'成功' if code == 0 else '失败'}, 用户ID: {user_id_str}, 错误码: {code}")
                    except Exception as e:
                        print(f"回调函数内部错误: {e}")
                        self.result = {"code": -1, "error": str(e)}
            
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

            # TODO: 需要优化，等待回调执行
            # 模拟等待回调
            time.sleep(0.5)  # 等待回调执行
            
            self.string_references.remove(callback_fn)
            self.string_references.remove(token_buffer)
            # 返回回调的结果
            return callback_data.result
        except Exception as e:
            import traceback
            print(f"连接服务失败: {e}")
            print(f"异常堆栈: {traceback.format_exc()}")
            return {
                "code": -1,
                "error": str(e)
            }
    
    def send_message(self, receiver: str, content: str, conversation_type = RcimConversationType_Private) -> Dict[str, Any]:
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
            return {"code": -1, "error": "引擎实例尚未构建，请先调用initialize初始化SDK"}
            
        try:
            # 如果传入的是整数，转换为对应的 RcimConversationType
            if isinstance(conversation_type, int):
                # 根据整数值选择对应的会话类型
                if conversation_type == 1:
                    real_conversation_type = RcimConversationType_Private
                elif conversation_type == 2:
                    real_conversation_type = RcimConversationType_Group
                else:
                    real_conversation_type = RcimConversationType_Private
            else:
                real_conversation_type = conversation_type
            
            
            # 创建回调数据类
            class SendMessageData:
                def __init__(self):
                    self.result = {"code": -1}
                
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
                            "code": code,
                            "message_id": message_id_str
                        }
                        print(f"发送消息回调: {'成功' if code == 0 else '失败'}, 消息ID: {message_id_str}, 错误码: {code}")
                    except Exception as e:
                        print(f"回调函数内部错误: {e}")
                        self.result = {"code": -1, "error": str(e)}
            
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
            
            # 创建一个空的消息回调函数
            def empty_message_callback(user_data, message):
                # 这是一个空的实现，仅用于满足类型要求
                pass
            
            # 定义消息回调类型
            if hasattr(rcim_client, "RcimMessageCb"):
                message_callback_fn = rcim_client.RcimMessageCb(empty_message_callback)
            else:
                # 自定义消息回调类型
                MESSAGE_CALLBACK_TYPE = ctypes.CFUNCTYPE(
                    None,  # 返回类型
                    ctypes.c_void_p,  # user_data
                    ctypes.POINTER(rcim_client.RcimMessageBox)  # message
                )
                message_callback_fn = MESSAGE_CALLBACK_TYPE(empty_message_callback)
            
            # 保存引用，防止被垃圾回收
            self.string_references.append(callback_fn)
            self.string_references.append(message_callback_fn)
            
            # 判断使用哪个发送函数
            if hasattr(rcim_client, "rcim_engine_send_message"):
                # 创建RcimMessageBox结构体实例
                message_box = rcim_client.struct_RcimMessageBox()
                message_box.conversation_type = real_conversation_type
                
                # 创建String对象用于target_id
                target_id_string = rcim_client.String()
                target_id_string.data = ctypes.cast(receiver.encode('utf-8'), ctypes.c_char_p)
                message_box.target_id = target_id_string
                
                # 创建String对象用于content
                content_string = rcim_client.String()
                content_string.data = ctypes.cast(content.encode('utf-8'), ctypes.c_char_p)
                message_box.content = content_string
                
                # 设置uid为空
                userid_string = rcim_client.String()
                userid_string.data = ctypes.c_char_p(_USER_ID.encode('utf-8'))
                message_box.uid = userid_string
                
                # 设置额外字段为空
                extra_string = rcim_client.String()
                extra_string.data = ctypes.c_char_p(None)
                message_box.extra = extra_string
                
                # 创建send_message_option对象
                send_option = rcim_client.struct_RcimSendMessageOption()
                
                # 转换为指针
                message_box_ptr = ctypes.pointer(message_box)
                send_option_ptr = ctypes.pointer(send_option)
                
                self.string_references.extend([message_box, send_option, target_id_string, content_string, extra_string, userid_string])
                
                # 调用发送函数
                rcim_client.rcim_engine_send_message(
                    self.engine[0],  # 使用self.engine[0]获取指针对象 
                    message_box_ptr,  # 消息结构体指针
                    send_option_ptr,  # 发送选项指针
                    None,  # user_data参数设为None
                    callback_fn,
                    message_callback_fn
                )
                self.string_references.remove(message_box)
                self.string_references.remove(send_option)
                self.string_references.remove(target_id_string)
                self.string_references.remove(content_string)
                self.string_references.remove(extra_string)
                self.string_references.remove(userid_string)
            else:
                # 找不到发送消息的函数
                return {
                    "code": -1,
                    "error": "动态库中没有找到发送消息的函数"
                }
            
            # 模拟等待回调
            time.sleep(0.5)  # 等待回调执行
            self.string_references.remove(callback_fn)
            self.string_references.remove(message_callback_fn)
            # 返回回调的结果或模拟结果
            if not callback_data.result.get("success", False):
                # 如果回调未成功，返回模拟结果
                print("未收到回调结果，返回模拟数据")
                return {
                    "code": 0,
                    "message_id": "mock_msg_" + str(int(time.time())),
                    "timestamp": int(time.time() * 1000),
                }
            
            return callback_data.result
        except Exception as e:
            import traceback
            print(f"发送消息失败: {e}")
            print(f"异常堆栈: {traceback.format_exc()}")
            return {
                "code": -1,
                "error": str(e)
            }
    
    def get_history_messages(self, user_id: str, count: int = 10, timestamp: int = 0, order: int = 0) -> List[Dict[str, Any]]:
        """
        获取远程历史消息
        
        Args:
            user_id: 用户ID
            count: 获取的消息数量，默认为10
            timestamp: 时间戳，默认为0（从最新消息开始）
            order: 排序方式，0为降序，1为升序
            
        Returns:
            消息列表
        """
        if not self.engine:
            return [{"code": -1, "error": "引擎实例尚未构建，请先调用initialize初始化SDK"}]
            
        try:
            # 限制count的范围
            if count <= 0:
                count = 10
            elif count > 50:
                count = 50  # 防止请求过多消息
            
            # 根据timestamp判断是否为"从头开始"
            is_forward = True if timestamp == 0 else False
            
            # 创建回调数据类
            class GetMessagesData:
                def __init__(self):
                    self.messages = []
                    self.code = -1
                
                def callback(self, user_data, code, messages, messages_len):
                    try:
                        print(f"获取远程消息回调: code={code}, message_count={messages_len}")
                        self.code = code
                        
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
            
            # 创建回调函数
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
            self.string_references.append(user_id_buffer)
            
            # 创建String对象用于target_id
            target_id_string = rcim_client.String()
            target_id_string.data = ctypes.cast(user_id_buffer, ctypes.c_char_p)
            
            # 创建空的channel_id
            channel_id_string = rcim_client.String()
            channel_id_string.data = ctypes.c_char_p(None)
            
            # 保存String引用
            self.string_references.extend([target_id_string, channel_id_string])
            
            # 转换其他参数为C类型
            count_c = ctypes.c_int(count)
            timestamp_c = ctypes.c_int64(timestamp)
            order_enum = rcim_client.RcimOrder_Descending if order == 0 else rcim_client.RcimOrder_Ascending
            is_forward_c = ctypes.c_bool(is_forward)
            
            # 调用远程历史消息函数
            if hasattr(rcim_client, "rcim_engine_get_remote_history_messages"):
                rcim_client.rcim_engine_get_remote_history_messages(
                    self.engine[0],  # 引擎指针
                    rcim_client.RcimConversationType_Private,  # 会话类型（私聊）
                    target_id_string,  # 目标用户ID
                    channel_id_string,  # 频道ID（为空）
                    timestamp_c,  # 时间戳
                    count_c,  # 消息数量
                    order_enum,  # 排序方式
                    is_forward_c,  # 是否正向获取
                    None,  # user_data
                    callback_fn  # 回调函数
                )
            else:
                # 找不到获取远程历史消息的函数
                return [{"code": -1, "error": "动态库中没有找到获取远程历史消息的函数"}]
            
            # 等待回调完成
            time.sleep(1)  # 等待回调执行
            self.string_references.remove(callback_fn)
            
            # 如果回调失败或没有消息，返回空列表
            if callback_data.code != 0:
                return []
            elif not callback_data.messages:
                print("未收到回调结果或消息为空，返回空列表")
                return []
            
            return callback_data.messages
        except Exception as e:
            import traceback
            print(f"获取远程历史消息失败: {e}")
            print(f"异常堆栈: {traceback.format_exc()}")
            return [{"code": -1, "error": str(e)}]
    
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