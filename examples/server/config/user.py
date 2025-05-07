import json
from typing import Union, List, Mapping

from .module import Module


class User(Module):
    """
    客户端通过融云 SDK 每次连接服务器时，都需要向服务器提供 Token，以便验证身份。
    后续登录过程中，就不必再向融云请求 Token，由 App Server 直接提供之前保存过的 Token。
    如果您的 App 是免登录设计，也可以将 Token 保存在 App 本地（注意保证本地数据存储安全），直接登录。
    App 获取 Token 后，根据情况可选择在 App 本地保留当前用户的 Token，如果 Token 失效，还需要提供相应的代码重新向服务器获取 Token。
    在`融云开发者平台`设置 Token 有效期，默认永久有效，除非您在开发者后台刷新 App Secret ，Token 可以获取多次，但之前的仍然可用。
    """

    def __init__(self, rc):
        super().__init__(rc)

    def getToken(self, userId, name=None, portraitUri=None):
        """
        获取 Token。
        :param userId:              用户 Id，支持大小写英文字母、数字、部分特殊符号 + = - _ 的组合方式，最大长度 64 字节。
                                    是用户在 App 中的唯一标识，必须保证在同一个 App 内不重复，
                                    重复的用户 Id 将被当作是同一用户。（必传）
        :param name:                用户名称，最大长度 128 字节。用来在 Push 推送时显示用户的名称。（必传）
        :param portraitUri:         用户头像 URI，最大长度 1024 字节。（必传）
        :return:                    请求返回结果，code 返回码，200 为正常；
                                    token 用户 Token，可以保存应用内，长度在 256 字节以内；
                                    userId 用户 Id，与输入的用户 Id 相同。
                                    如：{"code":200, "userId":"jlk456j5", "token":"sfd9823ihufi"}
        """
        param_dict = locals().copy()
        url = '/user/getToken.json'
        return self._http_post(url, param_dict)

    def validateToken(self, token):
        """
        验证token。
        :param token:               用户 Id，支持大小写英文字母、数字、部分特殊符号 + = - _ 的组合方式，最大长度 64 字节。
                                    是用户在 App 中的唯一标识，必须保证在同一个 App 内不重复，
        :return:                    请求返回结果，code 返回码，200 为正常；
                                    token 用户 Token，可以保存应用内，长度在 256 字节以内；
                                    userId 用户 Id，与输入的用户 Id 相同。
                                    如：{"code":200, "userId":"jlk456j5", "token":"sfd9823ihufi"}
        """
        param_dict = locals().copy()
        url = '/user/validateToken.json'
        return self._http_post(url, param_dict)

    def update(self, userId, name, portraitUri=None):
        """
        修改用户信息。
        :param userId:              用户 Id，支持大小写英文字母、数字、部分特殊符号 + = - _ 的组合方式，最大长度 64 字节。
                                    是用户在 App 中的唯一标识，必须保证在同一个 App 内不重复，
                                    重复的用户 Id 将被当作是同一用户。（必传）
        :param name:                用户名称，最大长度 128 字节。用来在 Push 推送时，显示用户的名称，刷新用户名称后 5 分钟内生效。
                                    （可选，提供即刷新，不提供忽略）
        :param portraitUri:         用户头像 URI，最大长度 1024 字节。用来在 Push 推送时显示。（可选，提供即刷新，不提供忽略）
        :return:                    请求返回结果，code 返回码，200 为正常。
                                    如：{"code":200}
        """
        param_dict = locals().copy()
        url = '/user/refresh.json'
        return self._http_post(url, param_dict)

    def info(self, userId):
        """
        查询用户信息。
        :param userId:              用户 Id。（必传）
        :return:                    请求返回结果，code 返回码，200 为正常；userName 用户名称；userPortrait 用户头像地址。
                                    createTime 用户创建时间。
                                    如：{"code":200,"userName":"123","userPortrait":"","createTime":"2016-05-24 10:38:19"}
        """
        param_dict = locals().copy()
        url = '/user/info.json'
        return self._http_post(url, param_dict)

    def check_online(self, userId):
        """
        检查用户在线状态。
        :param userId:              用户 Id。（必传）
        :return:                    请求返回结果，code 返回码，200 为正常；status 在线状态，1为在线，0为不在线。
                                    如：{"code":200,"status":"1"}
        """
        param_dict = locals().copy()
        url = '/user/checkOnline.json'
        return self._http_post(url, param_dict)

    def offline(self, app_key, deviceId, userId, packageName):
        """
        用户下线
        """
        _dict = {
            "deviceId": deviceId,
            "userId": userId,
            "packageName": packageName,
            "App-Key": app_key,

        }
        url = '/user/offline.json'
        return self._http_post(url, _dict)

    def expire(self, userId, time: int = None):
        """
        设置指定用户在某个时间点之前获取的 Token 失效；
        :param userId:              用户 Id。（必传）
        :param time:              	过期时间戳精确到毫秒，该时间戳前用户获取的 Token 全部失效，
                                    使用时间戳之前的 Token 已经在连接中的用户不会立即失效，断开后无法进行连接。（必传）
        :return:                    请求返回结果，code 返回码，200 为正常；status 在线状态，1为在线，0为不在线。
                                    如：{"code":200,"status":"1"}
        """
        param_dict = locals().copy()
        url = '/user/token/expire.json'
        return self._http_post(url, param_dict)

    def cs_info(self, userId, appKey):
        """
        客服用户信息查询
        :param userId:              用户 Id。（必传）
        :param appKey:
        """
        param_dict = locals().copy()
        url = '/user/cs/info.json'
        return self._http_post(url, param_dict)

    def list(self, num, offset, order):
        """
        获得用户列表
        """
        param_dict = locals().copy()
        url = '/user/list.json'
        return self._http_post(url, param_dict)

    def delusers(self, userId, appKey):
        """
        @todo 敏感接口
        删除用户
        :param userId:              用户 Id。（必传）
        :param appKey:
        """
        param_dict = locals().copy()
        url = '/user/delusers.json'
        return self._http_post(url, param_dict)

    def quietlist(self, requestId: str):
        """
        查询免打扰列表
        :param requestId:
        :return:
        """
        param_dict = locals().copy()
        url = '/conversation/notification/quietlist.json'
        return self._http_post(url, param_dict)

    def clear_message(self, userId: str, busChannel: str):
        """
        查询免打扰列表
        :param userId:
        :param busChannel:
        :return:
        """
        param_dict = locals().copy()
        url = '/user/buschannel/message/clear.json'
        return self._http_post(url, param_dict)

    @property
    def block(self):
        return Block(self._rc)

    @property
    def blacklist(self):
        return Blacklist(self._rc)

    @property
    def whitelist(self):
        return Whitelist(self._rc)

    @property
    def tag(self):
        return Tag(self._rc)

    @property
    def remarks(self):
        return Remarks(self._rc)

    @property
    def muted(self):
        return Muted(self._rc)

    @property
    def whiteSetting(self):
        return WhiteSetting(self._rc)

    @property
    def typeUnpush(self):
        return TypeUnpush(self._rc)

    @property
    def blockPushPeriod(self):
        return BlockPushPeriod(self._rc)

    @property
    def unpushPeriod(self):
        return UnpushPeriod(self._rc)

    @property
    def messageBlock(self):
        return MessageBlock(self._rc)

    @property
    def abandon(self):
        return Abandon(self._rc)

    @property
    def userSubscribe(self):
        return UserSubscribe(self._rc)

    @property
    def userProfile(self):
        return UserProfile(self._rc)


class Abandon(Module):
    """ 用户注销相关
    """

    def __init__(self, rc):
        super().__init__(rc)

    def query(self, pageNo: int, pageSize: int):
        """
        @return:
        """
        param_dict = locals().copy()
        url = '/user/deactivate/query.json'
        return self._http_post(url, param_dict)

    # def activate(self, userId: [str]):
    #     """
    #     @return:
    #     """
    #     param_dict = locals().copy()
    #     url = '/user/reactivate.json'
    #     return self._http_post(url, param_dict)

    # def abandon(self, userId: [str]):
    #     """
    #     @return:
    #     """
    #     param_dict = locals().copy()
    #     url = '/user/deactivate.json'
    #     return self._http_post(url, param_dict)


class BlockPushPeriod(Module):
    """ 用户免打扰
    """

    def __init__(self, rc):
        super().__init__(rc)

    def set(self, userId: str, startTime: int, period: int, level: int):
        """
        @return:
        """
        param_dict = locals().copy()
        url = '/user/blockPushPeriod/set.json'
        return self._http_post(url, param_dict)

    def get(self, userId: str):
        """
        查询用户免打扰时段
        @return:
        """
        param_dict = locals().copy()
        url = '/user/blockPushPeriod/get.json'
        return self._http_post(url, param_dict)

    def delete(self, userId: str):
        """
        删除用户免打扰时段
        @return:
        """
        param_dict = locals().copy()
        url = '/user/blockPushPeriod/delete.json'
        return self._http_post(url, param_dict)


class WhiteSetting(Module):
    """ 用户白名单设置
    """

    def __init__(self, rc):
        super().__init__(rc)

    def set(self, userId: Union[str, list], whiteSetting: int):
        """
        @param userId:              用户 ID，最多设置 20 个。
        @param whiteSetting:        状态，1 为开启白名单、0 为开启黑名单，默认为黑名单。
        @return:
        """
        param_dict = locals().copy()
        url = '/user/whitesetting/set.json'
        return self._http_post(url, param_dict)

    def query(self, userId: Union[str, list]):
        """
        @param userId:              用户 ID，最多设置 20 个。
        @return:
        """
        param_dict = locals().copy()
        url = '/user/whitesetting/query.json'
        return self._http_post(url, param_dict)


class Muted(Module):
    """ 用户禁言
    """

    def __init__(self, rc):
        super().__init__(rc)

    def set(self, userId: str, state: int, type: str = 'PERSON'):
        """
        按会话禁言,受upstreamMethods 配置的影响，配置 ppMsgP,pgMsgP,chatMsg 表示单群聊聊天室都支持
        @param userId:      被禁言用户 ID，支持批量设置，最多不超过 1000 个
        @param state:       禁言状态，0 解除禁言、1 添加禁言
        @param type:        会话类型，目前支持单聊、群聊、聊天室
        @return:
        """
        # type = 'PERSON'
        param_dict = locals().copy()
        url = '/user/chat/fb/set.json'
        return self._http_post(url, param_dict)

    def querylist(self, num: int, offset: int, type: str):
        """
        @param num:         获取行数，默认为 100，最大支持 200 个。
        @param offset:      查询开始位置，默认为 0。
        @param type:        会话类型，目前支持单聊会话 PERSON
        @return:
        """
        param_dict = locals().copy()
        url = '/user/chat/fb/querylist.json'
        return self._http_post(url, param_dict)


class Remarks(Module):
    """ 推送备注
    """

    def __init__(self, rc):
        super().__init__(rc)

    def set(self, userId, remarks: List[Mapping]):
        """
        @param userId:      用户 ID。
        @param remarks:     设置的目标用户推送备注名 JSON 字符串。详见 remarks 结构说明
                            [{"id":"user11","remark":"remark1"},{"id":"user12","remark":"remark2"}]
        @return:
        """
        remarks = json.dumps(remarks)
        param_dict = locals().copy()
        url = '/user/remarks/set.json'
        return self._http_post(url, param_dict)

    def get(self, userId, page: int, size: int):
        """
        @param userId:      用户 ID。
        @param page:
        @param size:
        @return:
        """
        param_dict = locals().copy()
        url = '/user/remarks/get.json'
        return self._http_post(url, param_dict)

    def delete(self, userId, targetId):
        """
        @param userId:      用户 ID。
        @param targetId:    需要删除推送备注名的用户 ID。
        @return:
        """
        param_dict = locals().copy()
        url = '/user/remarks/del.json'
        return self._http_post(url, param_dict)


class Block(Module):
    """
    当用户违反 App 中的相关规定时，可根据情况对用户进行封禁处理，封禁时间范围由开发者自行设置，
    用户在封禁期间不能连接融云服务器，封禁期满后将自动解除封禁，
    也可以通过调用 /user/unblock 方法解除用户封禁，解除后可正常连接融云服务器。
    """

    def __init__(self, rc):
        super().__init__(rc)

    def add(self, userId: Union[str, list], minute: int):
        """
        封禁用户
        :param userId:              用户 Id，支持一次封禁多个用户，最多不超过 20 个。（必传）
        :return:                    请求返回结果，code 返回码，200 为正常。如：{"code":200}
        """
        param_dict = locals().copy()
        url = '/user/block.json'
        return self._http_post(url, param_dict)

    def remove(self, userId):
        """
        解除用户封禁。
        :param userId:              用户 Id，支持一次解除多个用户，最多不超过 20 个。（必传）
        :return:                    请求返回结果，code 返回码，200 为正常。如：{"code":200}
        """
        param_dict = locals().copy()
        url = '/user/unblock.json'
        return self._http_post(url, param_dict)

    def query(self):
        """
        获取被封禁用户。
        :param                      无
        :return:                    请求返回结果，code 返回码，200 为正常；users 被封禁用户数组；userId 被封禁用户 ID；
        """
        url = '/user/block/query.json'
        return self._http_post(url)


class Blacklist(Module):
    """
    在 App 中如果用户不想接收到某一用户的消息或不想被某一用户联系到时，可将此用户加入到黑名单中，
    应用中的每个用户都可以设置自己的黑名单列表。
    """

    def __init__(self, rc):
        super().__init__(rc)

    def add(self, userId: str, blackUserId: Union[str, list]):
        """
        添加用户到黑名单。
        :param userId:             用户 Id。（必传）
        :param blackUserId:           被加黑的用户 Id，每次最多添加 20 个用户。(必传)
        :return:                    请求返回结果，code 返回码，200 为正常。如：{"code":200}
        """
        param_dict = locals().copy()
        url = '/user/blacklist/add.json'
        return self._http_post(url, param_dict)

    def remove(self, userId: str, blackUserId: Union[str, list]):
        """
        移除黑名单中用户。
        :param userId:              用户 Id。（必传）
        :param blackUserId:         被移除的用户 Id，每次最多移除 20 个用户。(必传)
        :return:                    请求返回结果，code 返回码，200 为正常。如：{"code":200}
        """
        param_dict = locals().copy()
        url = '/user/blacklist/remove.json'
        return self._http_post(url, param_dict)

    def query(self, userId, size=None, pageToken=None):
        """
        获取某用户黑名单列表。
        :param userId:              用户 Id。（必传）
        :return:                    请求返回结果，code 返回码，200 为正常；users 黑名单用户数组。
                                    如：{"code":200,"users":["jlk454","jlk457"]}
        """
        param_dict = locals().copy()
        url = '/user/blacklist/query.json'
        return self._http_post(url, param_dict)


class Whitelist(Module):
    """
    应用中对用户之间相互发送消息有限制要求的客户，可使用用户白名单功能，将用户加入白名单后，才能收到该用户发送的单聊消息。
    """

    def __init__(self, rc):
        super().__init__(rc)

    def add(self, userId, whiteUserId: Union[str, list]):
        """
        添加用户到白名单。
        :param userId:              用户 Id。（必传）
        :param whiteUserId:         被添加的用户 Id，每次最多添加 20 个用户。(必传)
        :return:                    请求返回结果，code 返回码，200 为正常。如：{"code":200}
        """
        param_dict = locals().copy()
        url = '/user/whitelist/add.json'
        return self._http_post(url, param_dict)

    def remove(self, userId, whiteUserId: Union[str, list]):
        """
        移除白名单中用户。
        :param userId:              用户 Id。（必传）
        :param whiteUserId:         被移除的用户 Id，每次最多移除 20 个用户。(必传)
        :return:                    请求返回结果，code 返回码，200 为正常。如：{"code":200}
        """
        param_dict = locals().copy()
        url = '/user/whitelist/remove.json'
        return self._http_post(url, param_dict)

    def query(self, userId, size = None, pageToken = None):
        """
        获取某用户白名单列表。
        :param userId:             用户 Id。（必传）
        :return:                    请求返回结果，code 返回码，200 为正常；users 白名单用户数组。
                                    如：{"code":200,"users":["jlk454","jlk457"]}
        """
        param_dict = locals().copy()
        url = '/user/whitelist/query.json'
        return self._http_post(url, param_dict)


class Tag(Module):
    def __init__(self, rc):
        super().__init__(rc)

    def set(self, userId: str, tags: list):
        """
        为应用中的一个或多个用户添加标签，如果某用户已经添加了标签，再次对用户添加标签时将覆盖之前设置的标签内容。
        :param userId:              用户 Id 或 Id 列表，一次最多支持 1000 个用户。（必传）
        :param tags:                用户标签，一个用户最多添加 20 个标签，每个 tag 最大不能超过 40 个字节，
                                    标签中不能包含特殊字符。（必传）
        :return:                    请求返回结果，code 返回码，200 为正常。如：{"code":200}
        """
        param_dict = locals().copy()
        url = '/user/tag/set.json'
        return self._http_post(url, param_dict, url_encode=False, )

    def sets(self, userIds: Union[str, list], tags: list):
        """
        为应用中的一个或多个用户添加标签，如果某用户已经添加了标签，再次对用户添加标签时将覆盖之前设置的标签内容。
        :param userIds:             用户 Id 或 Id 列表，一次最多支持 1000 个用户。（必传）
        :param tags:                用户标签，一个用户最多添加 20 个标签，每个 tag 最大不能超过 40 个字节，
                                    标签中不能包含特殊字符。（必传）
        :return:                    请求返回结果，code 返回码，200 为正常。如：{"code":200}
        """
        param_dict = locals().copy()
        url = '/user/tag/batch/set.json'
        return self._http_post(url, param_dict, url_encode=False, )

    def get(self, userIds: Union[str, list]):
        """
        查询用户所有标签功能，支持批量查询每次最多查询 50 个用户。
        :param userIds:            用户 Id，一次最多支持 50 个用户。（必传）
        :return:                    请求返回结果，code 返回码，200 为正常；result 用户所有的标签数组。
                                    如：{"code":200,"result":{"111":[],"222":["帅哥","北京"]}}
        """
        param_dict = locals().copy()
        url = '/user/tags/get.json'
        return self._http_post(url, param_dict)

    def getByTag(self, tags: Union[str, list], pages: int = 0, rows: int = 100):
        """
        根据tag查询用户
        :param tags:          标签
        :param pages：
        :param rows：
        :return:              请求返回结果，code 返回码，200 为正常；result 根据标签查询到的用户。
                              如：{"code":200,"users":["vyNt1wvyK","LkoV2CSki","0UjVRkmUG",
                                    "NdHtpURdY","F4fNpFJ4H"],"size":5}
        """
        param_dict = locals().copy()
        url = '/tag/users/get.json'
        return self._http_post(url, param_dict)


class TypeUnpush(Module):
    def __init__(self, rc):
        super().__init__(rc)

    def set(self, conversationType: str, requestId: str, unpushLevel: int):
        """
        设置会话类型免打扰：请求到 channelsession 服务
        :param conversationType:    会话类型。支持的会话类型包括：1（二人会话）、3（群组会话）、6（系统会话）、10（超级群会话）
        :param requestId:           设置消息免打扰的用户 ID。
        :param unpushLevel:         -1： 全部消息通知
                                    0： 未设置（用户未设置情况下，默认以群或者 APP 级别的默认设置为准，如未设置则全部消息都通知）
                                    1： 仅针对 @ 消息进行通知
                                    2： 仅针对 @ 指定用户进行通知
                                    如：@张三 则张三可以收到推送，@所有人 时不会收到推送。

                                    4： 仅针对 @ 群全员进行通知，只接收 @所有人 的推送信息。
                                    5： 不接收通知
                                    注意：IMKit 5.2.1 及之前版本不支持按会话类型设置的免打扰逻辑。推荐 IMKit 用户升级到 5.2.2 及之后版本。
        :return:                    {"code":200}	Int	返回码，200 为正常。
        """
        param_dict = locals().copy()
        url = '/conversation/type/notification/set.json'
        return self._http_post(url, param_dict)

    def get(self, conversationType: str, requestId: str):
        """
        :param conversationType:
        :param requestId:
        :return:    {"code":200,"isMuted":2}
        """
        param_dict = locals().copy()
        url = '/conversation/type/notification/get.json'
        return self._http_post(url, param_dict)


class UnpushPeriod(Module):
    def __init__(self, rc):
        super().__init__(rc)

    def add(self, userId: str, startTime: str, period: int, level: int,timezone:str=None):
        """
        添加用户免打扰时段
        :param userId:
        :param startTime: 开始时间
        :param period: 时长
        :param level: 级别
        :param timezone: 时区
        :return:
        """
        param_dict = locals().copy()
        url = '/user/blockPushPeriod/set.json'
        return self._http_post(url, param_dict)

    def delete(self, userId: str):
        """
        删除用户免打扰时段
        :param userId:
        :return:
        """
        param_dict = locals().copy()
        url = '/user/blockPushPeriod/delete.json'
        return self._http_post(url, param_dict)

    def get(self, userId: str):
        """
        查询用户免打扰时段
        :param userId:
        :return:
        """
        param_dict = locals().copy()
        url = '/user/blockPushPeriod/get.json'
        return self._http_post(url, param_dict)


class MessageBlock(Module):
    def __init__(self, rc):
        super().__init__(rc)

    def add(self, userId: str, blackUserId: str, code: int):
        """
        添加消息阻止
        :param userId:
        :param blackUserId: 被阻止用户
        :param code: 阻止原因
        :return:
        """
        param_dict = locals().copy()
        url = '/user/message/block/add.json'
        return self._http_post(url, param_dict)

    def remove(self, userId: str, blackUserId: str):
        """
        移除消息阻止
        :param userId:
        :param blackUserId: 被阻止用户
        :return:
        """
        param_dict = locals().copy()
        url = '/user/message/block/remove.json'
        return self._http_post(url, param_dict)

    def query(self, userId: str):
        """
        移除消息阻止
        :param userId:
        :return:
        """
        param_dict = locals().copy()
        url = '/user/message/block/query.json'
        return self._http_post(url, param_dict)


class UserSubscribe(Module):
    def __init__(self, rc):
        super().__init__(rc)

    def set(self, userId: str, subUserIds: str, opType: int, expiry: int, subType: int):
        """
        设置/取消订阅关系
        :param userId:
        :param subUserIds: 被订阅用户Id
        :param opType: 0 订阅，1 取消订阅
        :param expiry： 过期时间
        :param subType：1 订阅，  2 用户托管
        :return:
        """
        param_dict = locals().copy()
        url = '/user/subscribe/set.json'
        return self._http_post(url, param_dict)

    def query(self, userId: str, pageToken: str = None, pageSize: int = None, subType: int = None):
        """
        获取已订阅列表
        :param userId:
        :param pageToken: 第一页默认空，下一页的值为 response.pageToken
        :param pageSize: 页面大小
        :param subType：1 订阅，  2 用户托管
        :return:
        """
        param_dict = locals().copy()
        url = '/user/subscribe/query.json'
        return self._http_post(url, param_dict)


class UserProfile(Module):
    def __init__(self, rc):
        super().__init__(rc)

    def set(self, userId: str, userProfile: str, userExtProfile: str):
        """
        用户资料设置
        :param userId: 用户 ID
        :param userProfile: 用户基本信息
        :param userExtProfile: 用户扩展信息
        :return:
        """
        param_dict = locals().copy()
        url = '/user/profile/set.json'
        return self._http_post(url, param_dict)

    def batchQuery(self, userId: Union[str, list]):
        """
        批量查询用户资料
        :param userId:用户 ID，最多一次100个。
        :return:
        """
        param_dict = locals().copy()
        url = '/user/profile/batch/query.json'
        return self._http_post(url, param_dict)

    def query(self, page: int = 1, size: int = None, order: int = None):
        """
        分页获取应用全部用户列表
        :param page: 默认1
        :param size: 默认20，最大100
        :param order 根据注册时间的排序机制，默认正序，0为正序，1为倒序
        """
        param_dict = locals().copy()
        url = '/user/profile/query.json'
        return self._http_post(url, param_dict)

    def extSet(self, param):
        """
        添加用户扩展属性
        :param key: 属性名，长度不能超过 32 个字符
        :param allowSDKSet: 允许 SDK 设置：默认为允许状态, 允许：1 不允许：0
        :param allowSDKGet 允许 SDK获取：默认为允许状态, 允许：1 不允许：0
        """
        param_dict = locals().copy()
        data = param_dict.get('param')
        url = 'user/ext/profile/set.json'
        return self._http_post(url, data, url_encode=False, parse_none=True)

    def extUpdate(self, key: str, allowSDKSet: int = 1, allowSDKGet: int = 1):
        """
        修改用户扩展属性权限
        :param key: 属性名，长度不能超过 32 个字符
        :param allowSDKSet: 允许 SDK 设置：默认为允许状态, 允许：1 不允许：0
        :param allowSDKGet 允许 SDK获取：默认为允许状态, 允许：1 不允许：0
        """
        param_dict = locals().copy()
        url = 'user/ext/profile/upate.json'
        return self._http_post(url, param_dict)

    def extQuery(self, key: list):
        """
        获取用户扩展属性权限
        :param key: 属性名，长度不能超过 32 个字符
        """
        param_dict = locals().copy()
        url = '/user/ext/profile/query.json'
        return self._http_post(url, param_dict)

    def clean(self, userId: str):
        """
        用户托管信息清除
        :param userId: 用户ID
        """
        param_dict = locals().copy()
        url = '/user/profile/clean.json'
        return self._http_post(url, param_dict)
