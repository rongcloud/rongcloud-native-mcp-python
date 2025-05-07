import hashlib
import random
import socket
import time
from copy import deepcopy
from urllib.parse import urljoin, urlencode

import requests

from . import ALOG, save_node, convert_json
from .curl import request_to_curl

HEADER_APP_KEY = 'App-Key'
HEADER_NONCE = 'Nonce'
HEADER_TIMESTAMP = 'Timestamp'
HEADER_SIGNATURE = 'Signature'
HEADER_USER_AGENT = 'User-Agent'
HEADER_CONTENT_TYPE = 'Content-Type'
api_dict = dict()


def parse_data(data: dict, parse_none=False):
    if not data:
        data = dict()
    if 'self' in data:
        del data['self']
    if 'param_dict' in data:
        del data['param_dict']
    _tmp_data = deepcopy(data)
    if not parse_none:
        for k, v in _tmp_data.items():
            if v is None:
                del data[k]
    return data


class ParamException(Exception):
    def __init__(self, info):
        super().__init__(self)
        self.info = info

    def __str__(self):
        return self.info


class Module:
    def __init__(self, rc):
        self._rc = rc
        socket.setdefaulttimeout(10)

    def _signature(self):
        nonce = str(random.randint(0, 1000000000))
        timestamp = str(int(time.time()))
        sha1 = (self._rc.app_secret + nonce + timestamp).encode('utf8')
        signature = hashlib.sha1(sha1).hexdigest()
        return {HEADER_APP_KEY: self._rc.app_key,
                HEADER_NONCE: nonce,
                HEADER_TIMESTAMP: timestamp,
                HEADER_SIGNATURE: signature,
                HEADER_USER_AGENT: 'rc-python-sdk/3.2.0'}

    def _request(self, method, path, data=None, url_encode=True, seq=True, parse_none=False,
                 headers=None, json=True,
                 timeout=10) -> dict:
        """
        @param method: 方法类型 post 等
        @param path: 访问地址
        @param data: 请求数据
        @param url_encode: 是否需要 url code 编码
        @param seq: url code 关联，是否需要解析数组类型 userId=1&userId=2，否则将直接硬编码 userId=['1','2']
        @param parse_none: 是否需要忽略 None 值，为 True 则为传输时则 userId=None 否则 不传输 userId 字段
        @param headers: header 头内容
        @param timeout: 超时时间
        @return:
        """
        data = parse_data(data, parse_none)

        if data is None:
            data = {}
        _headers = self._signature()
        if headers:
            _headers.update(headers)
        url = path if 'http' in path else self._rc.host_url.get_url().rstrip('/') + '/' + path.lstrip('/')
        try:
            if url_encode:
                try:
                    data = urlencode(data, seq)
                except:
                    ALOG.warning(f'urlencode 编码异常 ：{data}')
                ALOG.info(f'post url:{url} data :{data}')
                _headers[HEADER_CONTENT_TYPE] = 'application/x-www-form-urlencoded'
                req = self._rc.client.request(method, url, headers=_headers, data=data,
                                              timeout=timeout, verify=self._rc.verify)
                # allure.attach(request_to_curl(req.request), 'curl 请求',
                #               allure.attachment_type.TEXT)
                ALOG.debug(f'curl 请求:{request_to_curl(req.request)}')
            else:
                ALOG.info(f'post url:{url} data :{data}')
                _headers[HEADER_CONTENT_TYPE] = 'application/json'
                req = self._rc.client.request(method, url, headers=_headers, json=data,
                                              timeout=timeout, verify=self._rc.verify)
                # allure.attach(request_to_curl(req.request), 'curl 请求',
                #               allure.attachment_type.TEXT)
                ALOG.debug(f'curl 请求:{request_to_curl(req.request)}')
            if req.status_code != 200:
                ret = convert_json(req)
                ALOG.warning(f'code :{req.status_code} 返回:{ret},请求 :{data}')
            ALOG.info(f'req url:{url} data :{req.content}')
            save_node(url, req.json())
            if json:
                return req.json()
            else:
                return req
        except requests.exceptions.ReadTimeout:
            ALOG.info(f'body :{data}')
            ALOG.info(f'timeout:{url}')
        except Exception as e:
            ALOG.info(f'error:{e}')

    def _http_post(self, path, data=None, url_encode=True, seq=True, parse_none=False, headers=None, json=True,
                   timeout=10):
        return self._request('post', path, data, url_encode, seq, parse_none, headers, json, timeout)

    def _http_get(self, path, data=None, url_encode=True, seq=True, parse_none=False, headers=None, json=True,
                  timeout=10):
        return self._request('get', path, data, url_encode, seq, parse_none, headers, json, timeout)

    def _http_delete(self, path, data=None, url_encode=True, seq=True, parse_none=False,
                     headers=None, json=True, timeout=10):
        return self._request('DELETE', path, data, url_encode, seq, parse_none, headers, json, timeout)

    def _http_put(self, path, data=None, url_encode=True, seq=True, parse_none=False, headers=None, json=True,
                  timeout=10):
        return self._request('PUT', path, data, url_encode, seq, parse_none, headers, json, timeout)
