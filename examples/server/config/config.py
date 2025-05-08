import datetime
import os

from .rongcloud import RongCloud
from imsdk.listener import RustListener
from diskcache import Cache
user_token_cache = Cache(os.path.join(os.path.dirname(__file__)))

class Config:
    apiHost = "https://api.rong-api.com"
    appKey = "c9kqb3rdcj1rj"
    appSecret = "1Coiv6bC4X"
    naviHost = "https://nav.rong-edge.com/"
    mediaHost = "https://rtc-media-ucbj2-01.rongcloud.net"
    stats_url = "https://stats.rong-edge.com"

    # apiHost = "https://api-ucqa.rongcloud.net"
    # appKey = "c9kqb3rdkbb8j"
    # appSecret = "uTNrkYskbNC"
    # naviHost = "nav-aliqa.rongcloud.net"
    # # naviHost = "http://127.0.0.1:8800"
    # mediaHost = "https://rtc-media-ucbj2-01.rongcloud.net"
    # stats_url = "http://stats-ucqa.rongcloud.net"

def get_token(user_id):
    key = Config.appKey + user_id
    token = user_token_cache.get(key)
    if token:
        return token
    server_client = RongCloud(app_key=Config.appKey, app_secret=Config.appSecret,
                              host_url=Config.apiHost,verify=False)
    token = server_client.user.getToken(user_id)["token"]
    user_token_cache.set(key, token)
    return token


class Common(Config):
    class LoginUser:
        token = get_token('5PmaSCHfI')
        userID = "5PmaSCHfI"
        userName = "5PmaSCHfI"
        phone = "18701694980"

    class TargetUser:
        token = get_token('DXIhdtUm7')
        userID = "DXIhdtUm7"
        userName = "DXIhdtUm7"
        phone = "18701694981"

    class Group:
        """群"""
        groupID = "IDFhdtUm7"
        groupName = "IDFhdtUm7"
        channelID = "test"

    class UltraGroup:
        """超级群"""
        ultraGroupID = "6005"
        busChannel = "channel1"
        privateChannel = "privateChannel"
        ultraGroupName = "test"

    class Chatroom:
        """聊天室"""
        chatroomID = "chatRoomId_100"

    server_client = RongCloud(app_key=Config.appKey, app_secret=Config.appSecret,
                              host_url=Config.apiHost)

    @staticmethod
    def get_token(user_id):
        return get_token(user_id)

    rust_listener = RustListener()

    @staticmethod
    def init_mentioned_api(mentioned_info_type: int, user_id: list = None, msg_content=None):
        """
        api 发消息 content
        @param mentioned_info_type: 1 @所有人，2 @指定用户
        @param user_id: [user_id]
        @param msg_content: 消息内容
        @return:
        """
        if not user_id:
            user_id = [""]
        if mentioned_info_type == 1:
            if not msg_content:
                msg_content = "A -> 神秘人@所有人" + str(datetime.datetime.now())
            content = {
                "content": msg_content,
                "mentionedInfo": {
                    "type": 1,
                    "mentionedContent": "有人@所有人"
                }
            }
        else:
            if not msg_content:
                msg_content = "A -> 神秘人@你" + str(datetime.datetime.now())
            content = {
                "content": msg_content,
                "mentionedInfo": {
                    "type": 2,
                    "userIdList": [user_id],
                    "mentionedContent": "有人@你"
                }
            }
        return content