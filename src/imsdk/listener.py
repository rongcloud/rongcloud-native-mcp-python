"""
IM SDK监听器模块

用于处理各种IM消息回调和事件监听
"""
import datetime
import time
import threading
import logging
from collections import defaultdict
from typing import Callable

from lib import rcim_client
from lib.rcim_utils import string_cast
from src.imsdk.util import ctypes_to_dict

# 配置日志
# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
# )
logger = logging.getLogger("im_listener")


class RustListener:
    def __init__(self):
        self.response = defaultdict(list)
        self.response_lock = threading.Lock()
        self.ConversationStatusLsr = rcim_client.RcimConversationStatusLsr(
            self.RcimConversationStatusLsr)
        self.LogLsr = rcim_client.RcimLogLsr(self.RcimLogLsr)
        self.LogLsrDev = rcim_client.RcimDevLogLsr(self.RcimLogLsrDev)
        self.DatabaseStatusLsr = rcim_client.RcimDatabaseStatusLsr(self.RcimDatabaseStatusLsr)
        self.ConnectionStatusLsr = rcim_client.RcimConnectionStatusLsr(self.RcimConnectionStatusLsr)
        self.MessageReceivedLsr = rcim_client.RcimMessageReceivedLsr(self.RcimMessageReceivedLsr)
        self.RecallMessageLsr = rcim_client.RcimRecallMessageLsr(self.RcimRecallMessageLsr)
        self.MessageBlockLsr = rcim_client.RcimMessageBlockedLsr(self.RcimMessageBlockLsr)
        self.ChatroomStatusLsr = rcim_client.RcimChatroomStatusLsr(self.RcimChatroomStatusLsr)
        self.ChatroomKvSyncLsr = rcim_client.RcimChatroomKvSyncLsr(self.RcimChatroomKvSyncLsr)

        self.ChatroomKvDeleteLsr = rcim_client.RcimChatroomKvDeleteLsr(self.RcimChatroomKvDeleteLsr)
        self.ChatroomKvChangedLsr = rcim_client.RcimChatroomKvChangedLsr(
            self.RcimChatroomKvChangedLsr)
        self.ChatroomMultiClientSyncLsr = rcim_client.RcimChatroomMultiClientSyncLsr(
            self.RcimChatroomMultiClientSyncLsr)
        self.ChatroomMemberBlockedLsr = rcim_client.RcimChatroomMemberBlockedLsr(
            self.RcimChatroomMemberBlockedLsr)
        self.ChatroomMemberBannedLsr = rcim_client.RcimChatroomMemberBannedLsr(
            self.RcimChatroomMemberBannedLsr)

        self.ChatroomMemberChangedLsr = rcim_client.RcimChatroomMemberChangedLsr(
            self.RcimChatroomMemberChangedLsr
        )

        self.TypingStatusLsr = rcim_client.RcimTypingStatusLsr(self.RcimTypingStatusLsr)
        self.MessageSearchableWordsCbLsr = rcim_client.RcimMessageSearchableWordsCbLsr(
            self.RcimMessageSearchableWordsCbLsr)

        self.MessageExpansionKvRemoveLsr = rcim_client.RcimMessageExpansionKvRemoveLsr(
            self.RcimMessageExpansionKvRemoveLsr)

        self.MessageExpansionKvUpdateLsr = rcim_client.RcimMessageExpansionKvUpdateLsr(
            self.RcimMessageExpansionKvUpdateLsr)
        self.RcimCmpSendLsr = rcim_client.RcimCmpSendCb(
            self.RcimCmpSendCb)
        self.ConversationReadStatusLsr = rcim_client.RcimConversationReadStatusLsr(
            self.RcimConversationReadStatusLsr
        )
        self.SightCompressCbLsr = rcim_client.RcimSightCompressCbLsr(
            self.RcimSightCompressCbLsr
        )
        self.MessageNotifyLsr = rcim_client.RcimMessageNotifyLsr(self.RcimMessageNotifyLsr)
        self.ReadReceiptRequestLsr = rcim_client.RcimReadReceiptRequestLsr(
            self.RcimReadReceiptRequestLsr)

        self.ReadReceiptResponseLsr = rcim_client.RcimReadReceiptResponseLsr(
            self.RcimReadReceiptResponseLsr)
        self.MessageDestructingLsr = rcim_client.RcimMessageDestructingLsr(
            self.RcimMessageDestructingLsr)

        self.MessageDestructionStopLsr = rcim_client.RcimMessageDestructionStopLsr(
            self.RcimMessageDestructionStopLsr)
        self.OfflineMessageSyncCompletedLsr = rcim_client.RcimOfflineMessageSyncCompletedLsr(
            self.RcimOfflineMessageSyncCompletedLsr)

        self.RcimRtcKvSignalingLsr = rcim_client.RcimRtcKvSignalingLsr(self.RcimRtcKvSignalingLsr)

        self.ReadReceiptResponseV2Lsr = rcim_client.RcimReadReceiptResponseV2Lsr(self.RcimReadReceiptResponseV2Lsr)

    def wait_listener(self, name, timeout=5):
        t1 = time.time()
        while True:
            if len(self.response.get(name, [])) > 10000:
                with self.response_lock:
                    self.response.get(name).clear()
            with self.response_lock:
                data = self.response.pop(name, [])
            if data or time.time() - t1 > timeout:
                break
            time.sleep(0.01)
        return data

    def wait_until_listener_event(self, listener: str, fun: Callable, timeout: int = 5,
                                  raise_exception: bool = True):
        """
        轮询监听数据直到满足某个条件或超时
        :param listener: 监听器名
        :param fun: 判断函数，传入单条数据返回 True/False
        :param timeout: 超时时间（秒）
        :return: 匹配的数据
        """
        end_time = time.time() + timeout
        while time.time() < end_time:
            listener_data = self.wait_listener(listener)
            for data in listener_data:
                if fun(data):
                    return data
            time.sleep(0.1)
        if raise_exception:
            raise TimeoutError(f"Did not receive expected listener event '{listener}' within {timeout}s")
        else:
            return None

    # 消息接收监听器，重点增强此方法的功能
    def RcimMessageReceivedLsr(self, context, message_box, info):
        """
        消息接收监听器回调方法
        
        Args:
            context: 上下文
            message_box: 消息体
            info: 消息信息
        """
        try:
            # 转换为Python字典
            message_data = ctypes_to_dict(message_box)
            info_data = ctypes_to_dict(info)
            
            # 记录消息接收
            logger.info(f"收到新消息: {message_data}")
            
            # 构造格式化的消息对象
            formatted_message = {
                "message_id": message_data.get("message_id", ""),
                "conversation_type": message_data.get("conversation_type", 0),
                "sender_id": message_data.get("sender_id", ""),
                "target_id": message_data.get("target_id", ""),
                "content": message_data.get("content", ""),
                "timestamp": message_data.get("timestamp", int(time.time() * 1000)),
                "extra": message_data.get("extra", ""),
                "raw_data": message_data,
                "info": info_data
            }
            
            # 保存到监听数据
            with self.response_lock:
                self.response['RcimMessageReceivedLsr'].append(formatted_message)
            
        except Exception as e:
            logger.error(f"处理接收消息时出错: {e}")

    def RcimReadReceiptResponseV2Lsr(self, context, conv_type, target_id, channel_id, message_uid, read_count,total_count):
        print("监听数据", 'RcimReadReceiptResponseV2Lsr')
        data = {
            'conv_type': conv_type,
            'target_id': string_cast(target_id),
            'channel_id': string_cast(channel_id),
            'message_uid': string_cast(message_uid),
            'read_count': read_count,
            'total_count': total_count
        }
        with self.response_lock:
            self.response['RcimReadReceiptResponseV2Lsr'].append(data)

    def RcimRtcKvSignalingLsr(self, context, kv_vec, kv_vec_len):
        print("监听数据", 'RcimRtcKvSignalingLsr')
        _list = []
        for i in range(kv_vec_len):
            _list.append(ctypes_to_dict(kv_vec[i]))
        with self.response_lock:
            self.response['RcimRtcKvSignalingLsr'].append(_list)

    def RcimOfflineMessageSyncCompletedLsr(self, context):
        print('RcimOfflineMessageSyncCompletedLsr')
        with self.response_lock:
            self.response['RcimOfflineMessageSyncCompletedLsr'].append({})

    def RcimMessageExpansionKvUpdateLsr(self, context, key_vec, key_vec_len, msg_box):
        _list = []
        for i in range(key_vec_len):
            _list.append(ctypes_to_dict(key_vec[i]))
        print('RcimMessageExpansionKvUpdateLsr', _list)

        with self.response_lock:
            self.response['RcimMessageExpansionKvUpdateLsr'].append(
            {'keys': _list, 'message': ctypes_to_dict(msg_box)})

    def RcimMessageExpansionKvRemoveLsr(self, context, key_vec, key_vec_len, msg_box):
        _list = []
        for i in range(key_vec_len):
            _list.append(string_cast(key_vec[i]))
        print('RcimMessageExpansionKvRemoveLsr', _list)
        with self.response_lock:
            self.response['RcimMessageExpansionKvRemoveLsr'].append(
            {'keys': _list, 'message': ctypes_to_dict(msg_box)})

    # @log
    def RcimConversationStatusLsr(self, context, items, len):
        _list = []
        for i in range(len):
            _list.append(ctypes_to_dict(items[i]))
        with self.response_lock:
            self.response['RcimConversationStatusLsr'].append({'items': _list, 'len': len})

    # @log
    def RcimLogLsr(self, level, log_cstr):
        print(datetime.datetime.now().strftime("%H:%M:%S.%f"), ctypes_to_dict(log_cstr))
        # self.response['RcimLogLsr'].append({'level': level, 'log_cstr': log_cstr})

    def RcimLogLsrDev(self, level, log_cstr):
        pass
        # print("监听数据", level, string_cast(log_cstr))
        # self.response['RcimLogLsr'].append({'level': level, 'log_cstr': log_cstr})

    # @log
    def RcimDatabaseStatusLsr(self, context, status):
        print("监听数据", 'RcimDatabaseStatusLsr', status)
        with self.response_lock:
            self.response['RcimDatabaseStatusLsr'].append({'status': status})

    # @log
    def RcimConnectionStatusLsr(self, context, status):
        # status = ConnectionStatusC._enumvalues[status]
        print("监听数据", 'RcimConnectionStatusLsr', status)
        with self.response_lock:
            self.response['RcimConnectionStatusLsr'].append({'status': status})

    # @log
    def RcimRecallMessageLsr(self, context, message_box, recall_notify_msg):
        print(f"RcimRecallMessageLsr----{id(self)}")
        message_box = ctypes_to_dict(message_box)
        recall_notify_msg = ctypes_to_dict(recall_notify_msg)
        print("监听数据", 'RcimRecallMessageLsr', message_box, recall_notify_msg)
        with self.response_lock:
            self.response['RcimRecallMessageLsr'].append(
            {'message': message_box, 'recall_notify_msg': recall_notify_msg})

    # @log
    def RcimMessageBlockLsr(self, context, msg_block_info):
        msg_block_info = ctypes_to_dict(msg_block_info)
        print("监听数据", 'RcimMessageBlockLsr', msg_block_info)
        with self.response_lock:
            self.response['RcimMessageBlockLsr'].append({'msg_block_info': msg_block_info})

    # @log
    def RcimChatroomStatusLsr(self, context, code, room_id, status, response, ):
        # code = ChatroomStatusC._enumvalues[code]
        print("监听数据", 'RcimChatroomStatusLsr', code, room_id, status, response)
        with self.response_lock:
            self.response['RcimChatroomStatusLsr'].append(
                {'room_id': room_id, 'status': status, 'response': ctypes_to_dict(response),
                 'code': code})

    def RcimChatroomKvSyncLsr(self, context, room_id):
        # code = ChatroomStatusC._enumvalues[code]
        print("监听数据", 'RcimChatroomKvSyncLsr', string_cast(room_id))
        with self.response_lock:
            self.response['RcimChatroomKvSyncLsr'].append(
                {'room_id': string_cast(room_id)})

    def RcimChatroomKvChangedLsr(self, context, room_id, kv_vec, kv_vec_len):
        _list = []
        for i in range(kv_vec_len):
            _list.append(ctypes_to_dict(kv_vec[i]))
        print("监听数据", 'RcimChatroomKvChangedLsr', kv_vec_len, _list)
        with self.response_lock:
            self.response['RcimChatroomKvChangedLsr'].append(
                {'room_id': string_cast(room_id), 'RcimChatroomKvInfo': _list})

    def RcimChatroomMultiClientSyncLsr(self, context, sync_info):
        info = ctypes_to_dict(sync_info)
        print("监听数据", 'RcimChatroomMultiClientSyncLsr', info)
        with self.response_lock:
            self.response['RcimChatroomMultiClientSyncLsr'].append(info)

    def RcimChatroomMemberBlockedLsr(self, context, block_info):
        info = ctypes_to_dict(block_info)
        print("监听数据", 'RcimChatroomMemberBlockedLsr', info)
        with self.response_lock:
            self.response['RcimChatroomMemberBlockedLsr'].append(block_info)

    def RcimChatroomMemberBannedLsr(self, context, ban_info):

        info = {
            'room_id': string_cast(ban_info.contents.room_id),
            'event_type': ban_info.contents.event_type,
            'duration_time': ban_info.contents.duration_time,
            'operate_time': ban_info.contents.operate_time,
            'extra': string_cast(ban_info.contents.extra),
        }
        user_id_vec_len = ban_info.contents.user_id_vec_len
        user_id_vec = []
        for i in range(user_id_vec_len):
            user_id_vec.append(ctypes_to_dict(ban_info.contents.user_id_vec[i]))

        info['user_id_vec'] = user_id_vec
        print("监听数据", 'RcimChatroomMemberBannedLsr', info)
        with self.response_lock:
            self.response['RcimChatroomMemberBannedLsr'].append(info)

    def RcimChatroomMemberChangedLsr(self, context, change_info):
        info = {
            'room_id': string_cast(change_info.contents.room_id),
            'member_count': change_info.contents.member_count,
        }
        action_vec_len = change_info.contents.action_vec_len
        user_id_vec = []
        for i in range(action_vec_len):
            user_id_vec.append(ctypes_to_dict(change_info.contents.action_vec[i]))
        info['user_id_vec'] = user_id_vec
        print("监听数据", 'RcimChatroomMemberChangedLsr', info)
        with self.response_lock:
            self.response['RcimChatroomMemberChangedLsr'].append(info)

    def RcimChatroomKvDeleteLsr(self, context, room_id, kv_vec, kv_vec_len):
        _list = []
        for i in range(kv_vec_len):
            _list.append(ctypes_to_dict(kv_vec[i]))
        print("监听数据", 'RcimChatroomKvDeleteLsr', kv_vec_len, _list)
        with self.response_lock:
            self.response['RcimChatroomKvDeleteLsr'].append(
                {'room_id': string_cast(room_id), 'kv_vec': _list})

    def RcimTypingStatusLsr(self, context, conv_type, target_id, channel_id, typing_status,
                            typing_status_vec_len):
        info = {
            'conv_type': conv_type,
            'target_id': string_cast(target_id),
            'channel_id': string_cast(channel_id),
        }
        typing_status_vec = []
        for i in range(typing_status_vec_len):
            typing_status_vec.append(ctypes_to_dict(typing_status[i]))
        info['typing_status_vec'] = typing_status_vec
        print("监听数据", 'RcimTypingStatusLsr', info)
        with self.response_lock:
            self.response['RcimTypingStatusLsr'].append(info)

    def RcimMessageSearchableWordsCbLsr(self, context, obj_name, content, callback_context, cb):
        data = {'obj_name': string_cast(obj_name), 'content': string_cast(content), 'cb': cb}
        print("监听数据", 'RcimMessageSearchableWordsCbLsr', data)
        with self.response_lock:
            self.response['RcimMessageSearchableWordsCbLsr'].append(data)
        import _thread
        _thread.start_new_thread(demo, (cb, callback_context))
        # cb(callback_context, char_pointer_cast("788888"))

    def RcimCmpSendCb(self, context, code):
        print("监听数据", 'RcimCmpSendCb', code)
        with self.response_lock:
            self.response['RcimCmpSendCb'].append({'code': code})

    def RcimConversationReadStatusLsr(self, context, conv_type, target_id, channel_id, timestamp):
        print("监听数据", 'RcimConversationReadStatusLsr', conv_type, string_cast(target_id), string_cast(channel_id),
              timestamp)
        with self.response_lock:
            self.response['RcimConversationReadStatusLsr'].append(
                {'conv_type': conv_type, 'target_id': string_cast(target_id), 'channel_id': string_cast(channel_id),
                 'timestamp': timestamp})

    def RcimMessageNotifyLsr(self, context, msg_box):
        msg_box = ctypes_to_dict(msg_box)
        print("监听数据", 'RcimMessageNotifyLsr', msg_box)
        with self.response_lock:
            self.response['RcimMessageNotifyLsr'].append({'message': msg_box})

    def RcimSightCompressCbLsr(self, context, target_width, target_height, path, callback_context, callback):
        print("监听数据", 'RcimSightCompressCbLsr', target_width, target_height, string_cast(path))
        with self.response_lock:
            self.response['RcimSightCompressCbLsr'].append(
                {'target_width': target_width, 'target_height': target_height, 'path': path})
        _path = string_cast(path)
        import _thread
        _thread.start_new_thread(demo2, (callback, callback_context, _path))

    def RcimReadReceiptRequestLsr(self, context, conv_type, target_id, channel_id, message_uid):
        print("监听数据", 'RcimReadReceiptRequestLsr', conv_type, string_cast(target_id), string_cast(channel_id),
              string_cast(message_uid))
        with self.response_lock:
            self.response['RcimReadReceiptRequestLsr'].append(
                {'conv_type': conv_type, 'target_id': string_cast(target_id), 'channel_id': string_cast(channel_id),
                 'message_uid': string_cast(message_uid)})

    def RcimReadReceiptResponseLsr(self, context, conv_type, target_id, channel_id, message_uid, respond_user_vec,
                                   respond_user_vec_len):

        respond_user_list = []
        for i in range(respond_user_vec_len):
            respond_user_list.append(ctypes_to_dict(respond_user_vec[i]))
        print("监听数据", 'RcimReadReceiptResponseLsr', conv_type, string_cast(target_id), string_cast(channel_id),
              string_cast(message_uid), respond_user_list, respond_user_vec_len)

        with self.response_lock:
            self.response['RcimReadReceiptResponseLsr'].append(
                {'conv_type': conv_type, 'target_id': string_cast(target_id), 'channel_id': string_cast(channel_id),
                 'message_uid': string_cast(target_id), 'respond_user_list': respond_user_list})

    def RcimMessageDestructingLsr(self, context, message_box, left_duration):
        print("监听数据", 'RcimMessageDestructingLsr', ctypes_to_dict(message_box), left_duration)
        with self.response_lock:
            self.response['RcimMessageDestructingLsr'].append(
                {'message': ctypes_to_dict(message_box), 'left_duration': left_duration})

    def RcimMessageDestructionStopLsr(self, context, message_box):
        print("监听数据", 'RcimMessageDestructionStopLsr', ctypes_to_dict(message_box))
        with self.response_lock:
            self.response['RcimMessageDestructionStopLsr'].append(
                {'message': ctypes_to_dict(message_box)})

# 导出类和实例
__all__ = ["RustListener"]
