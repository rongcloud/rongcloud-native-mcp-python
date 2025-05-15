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
import threading
from typing import Dict, Any, List

# 获取动态库文件的绝对路径
_ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
_LIB_DIR = os.path.join(_ROOT_DIR, "lib")
_USER_ID = ""

# 添加lib目录到Python路径，确保可以导入lib.rcim_client
if _ROOT_DIR not in sys.path:
    sys.path.append(_ROOT_DIR)

# 导入rcim_client模块
from src.imsdk.util import dict_to_ctypes,ctypes_to_dict
from lib import rcim_client
from lib.rcim_utils import string_cast, char_pointer_cast
# 从rcim_client导入所需类型
from lib.rcim_client import (
    RcimConversationType_Group,
    RcimConversationType_Private,
    RcimEngineBuilder,
    RcimEngineBuilderParam,
    RcimEngineSync,
    RcimLogLevel_Debug,
    RcimMessageBox,
    RcimPlatform,
    RcimConversationType,
    RcimPlatform_Linux,
    RcimPlatform_MacOS,
    RcimPlatform_Unknown,
    RcimPlatform_Windows,
    RcimSDKVersion,
    RcimSendMessageOption
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
            # 导入RustListener类
            from src.imsdk.listener import RustListener, message_callback_manager
            self.rust_listener = RustListener()
            self.message_callback_manager = message_callback_manager
            self._message_listener_registered = False
        except Exception as e:
            self.rust_listener = None
            self.message_callback_manager = None
            print(f"警告: 创建rust_listener失败: {e}")
        
    def initialize(self, app_key: str, navi_host: str, device_id: str) -> Dict[str, Any]:
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
                "sdk_version_vec": {"name":"rust","version":"0.17.1"},
                "sdk_version_vec_len": 1,
                "app_version": "1.0.0",
            }
            
            # 创建参数结构体
            param = dict_to_ctypes(RcimEngineBuilderParam, engine_builder_param)
            
            # 创建builder指针
            builder = ctypes.pointer(ctypes.pointer(RcimEngineBuilder()))
            
            # 调用创建函数
            ret = rcim_client.rcim_create_engine_builder(param,builder)
            if ret != 0:
                print(f"rcim_create_engine_builder failed, error code: {ret}")
                return {"code": -1, "error": f"rcim_create_engine_builder failed, error code: {ret}"}
            
            # 保存builder引用
            self.builder = builder.contents
            
            # 设置存储路径
            db_path = os.path.join(rust_path, "rust_db")
            # 确保目录存在
            os.makedirs(db_path, exist_ok=True)
            
            ret = rcim_client.rcim_engine_builder_set_store_path(self.builder, char_pointer_cast(db_path))
            if ret != 0:
                print(f"rcim_engine_builder_set_store_path failed, error code: {ret}")

            # 设置navi服务器
            navi_list = [navi_host]
            char_ptrs = (ctypes.POINTER(ctypes.c_char) * len(navi_list))()
            for i, string in enumerate(navi_list):
                if string is None:
                    char_ptrs[i] = None
                    continue
                # 创建对应字符串的 c_char 数组，并获取其指针
                char_array = ctypes.create_string_buffer(string.encode('utf-8'))
                char_ptrs[i] = ctypes.cast(char_array, ctypes.POINTER(ctypes.c_char))
            double_ptr = ctypes.cast(char_ptrs, ctypes.POINTER(ctypes.POINTER(ctypes.c_char)))
            
            ret = rcim_client.rcim_engine_builder_set_navi_server(self.builder, double_ptr,1)
            if ret != 0:
                print(f"rcim_engine_builder_set_navi_server failed, error code: {ret}")


            # 创建引擎
            engine_ptr = ctypes.pointer(ctypes.pointer(RcimEngineSync()))
            
            print(f"rcim_engine_builder_build 即将执行")

            # 构建引擎
            ret = rcim_client.rcim_engine_builder_build(self.builder, engine_ptr)
            if ret != 0:
                print(f"rcim_engine_builder_build failed, error code: {ret}")
                return {"code": -1, "error": f"rcim_engine_builder_build failed, error code: {ret}"}
            
            # 保存引擎引用
            self.engine = engine_ptr.contents

            rcim_client.rcim_engine_set_log_filter(self.engine,RcimLogLevel_Debug)
            rcim_client.rcim_engine_set_log_listener(self.engine, None, self.rust_listener.LogLsr)

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
        
        if not self.engine:
            return {"code": -1, "error": "引擎实例尚未构建，请先调用initialize初始化SDK"}
        if _USER_ID:
            print(f"已经存在连接，跳过连接")
            return {"code": 0, "user_id": _USER_ID}
        
        print(f"连接融云服务，token: {token[:10]}..., 超时: {timeout_sec}秒")
        
        # 创建回调数据类
        class ConnectData:
            def __init__(self):
                self.result = {"code": -1}
            
            def callback(self, user_data, code, user_id):
                # 从String类型获取字符串
                user_id_str = string_cast(user_id)
                # 将user_id_str赋值给全局变量_USER_ID
                global _USER_ID
                _USER_ID = user_id_str
                self.result = {
                    "code": code,
                    "user_id": user_id_str,
                }
                print(f"连接回调: {'成功' if code == 0 else '失败'}, 用户ID: {user_id_str}, 错误码: {code}")
        
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
        token_buffer = char_pointer_cast(token)
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
                    ctypes.pointer(rcim_client.RcimMessageBox)  # message_box
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
                    ctypes.pointer(rcim_client.RcimMessageBox)  # message
                )
                message_callback_fn = MESSAGE_CALLBACK_TYPE(empty_message_callback)
            
            # 保存引用，防止被垃圾回收
            self.string_references.append(callback_fn)
            self.string_references.append(message_callback_fn)
            
            # 判断使用哪个发送函数
            if hasattr(rcim_client, "rcim_engine_send_message"):
                message_box_dic = {
                    'conv_type':real_conversation_type,
                    'target_id':receiver,
                    'object_name': 'RC:TxtMsg',
                    'content' : {
                        'content':content
                    },
                    'uid': _USER_ID
                }

                # 创建RcimMessageBox结构体实例
                message_box = dict_to_ctypes(RcimMessageBox,message_box_dic)
                # 创建send_message_option对象
                send_option = dict_to_ctypes(RcimSendMessageOption,{})

                # 调用发送函数
                rcim_client.rcim_engine_send_message(
                    self.engine[0],  # 使用self.engine[0]获取指针对象 
                    message_box,
                    send_option,
                    None,  # user_data参数设为None
                    callback_fn,
                    message_callback_fn
                )
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
            # 返回回调的结果
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
            
            # 创建同步事件
            done_event = threading.Event()

            class GetMessagesData:
                def __init__(self):
                    self.messages = []
                    self.code = -1

                def callback(self, user_data, code, messages, messages_len):
                    print(f"获取远程消息回调: code={code}, message_count={messages_len}")
                    self.code = code
                    if code == 0 and messages and messages_len > 0:
                        print("-1")
                        for i in range(messages_len):
                            msg_dict = ctypes_to_dict(messages[i])
                            print(f"i={i}")
                            self.messages.append(msg_dict)
                    print(f"-2")
                    done_event.set()  # 回调结束，通知主线程
                    print(f"-3")
            
            # 创建回调数据
            callback_data = GetMessagesData()
            
            # 使用正确的回调函数类型和参数
            def callback_wrapper(user_data, code, messages, messages_len):
                try:
                    return callback_data.callback(user_data, code, messages, messages_len)
                except Exception as e:
                    print(f"回调包装函数错误: {e}")
                    done_event.set()
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
                    ctypes.pointer(ctypes.pointer(rcim_client.RcimMessageBox)),  # messages
                    ctypes.c_int  # message_count
                )
                callback_fn = CALLBACK_TYPE(callback_wrapper)
            
            # 保存引用，防止被垃圾回收
            self.string_references.append(callback_fn)
            
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
                    char_pointer_cast(user_id),  # 目标用户ID
                    None,  # 频道ID（为空）
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
            
            # 等待回调，最多5秒
            finished = done_event.wait(timeout=5)
            print(f"获取历史消息回调结束: {finished}")
            self.string_references.remove(callback_fn)

            if not finished:
                print("获取历史消息超时，未收到回调")
                return [{"code": -2, "error": "获取历史消息超时，未收到回调"}]

            if callback_data.code != 0:
                return [{"code": callback_data.code, "error": callback_data.messages}]
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

    def register_message_callback(self, callback):
        """
        注册消息回调函数
        
        Args:
            callback: 回调函数，接收消息数据字典作为参数
            
        Returns:
            成功返回True，失败返回False
        """
        if not self.message_callback_manager:
            print("消息回调管理器未初始化")
            return False
            
        try:
            self.message_callback_manager.register_callback(callback)
            return True
        except Exception as e:
            print(f"注册消息回调失败: {e}")
            return False
    
    def unregister_message_callback(self, callback):
        """
        注销消息回调函数
        
        Args:
            callback: 之前注册的回调函数
            
        Returns:
            成功返回True，失败返回False
        """
        if not self.message_callback_manager:
            print("消息回调管理器未初始化")
            return False
            
        try:
            self.message_callback_manager.unregister_callback(callback)
            return True
        except Exception as e:
            print(f"注销消息回调失败: {e}")
            return False
    
    def register_client(self, client_id):
        """
        注册客户端
        
        Args:
            client_id: 客户端唯一标识
            
        Returns:
            成功返回True，失败返回False
        """
        if not self.message_callback_manager:
            print("消息回调管理器未初始化")
            return False
            
        try:
            self.message_callback_manager.register_client(client_id)
            return True
        except Exception as e:
            print(f"注册客户端失败: {e}")
            return False
    
    def unregister_client(self, client_id):
        """
        注销客户端
        
        Args:
            client_id: 客户端唯一标识
            
        Returns:
            成功返回True，失败返回False
        """
        if not self.message_callback_manager:
            print("消息回调管理器未初始化")
            return False
            
        try:
            self.message_callback_manager.unregister_client(client_id)
            return True
        except Exception as e:
            print(f"注销客户端失败: {e}")
            return False
    
    def get_client_messages(self, client_id, max_count=20):
        """
        获取并清空客户端消息队列
        
        Args:
            client_id: 客户端唯一标识
            max_count: 最大获取消息数量
            
        Returns:
            消息列表，失败返回空列表
        """
        if not self.message_callback_manager:
            print("消息回调管理器未初始化")
            return []
            
        try:
            return self.message_callback_manager.get_client_messages(client_id, max_count)
        except Exception as e:
            print(f"获取客户端消息失败: {e}")
            return []

# 创建默认SDK实例，使用默认参数
default_sdk = IMSDK() 