import datetime
import threading
import time
import requests

from .user import User

class RongCloud:
    app_key = ''
    app_secret = ''
    host = ''

    class _HostUrl:
        def __init__(self, host_url):
            self.host_list = host_url.split(';')
            self.now = 0
            self.last_change_url_duration = 30
            self.last_change_url_time = 0

        def get_url(self):
            return self.host_list[self.now]

        def switch_url(self):
            lock = threading.Lock()
            with lock:
                # 检查距离上次更换uri的时间间隔
                now = time.time()
                seconds = (datetime.datetime.fromtimestamp(now) - datetime.datetime.fromtimestamp(
                    self.last_change_url_time)).seconds
                if seconds >= self.last_change_url_duration:
                    if self.now < len(self.host_list) - 1:
                        self.now = self.now + 1
                    else:
                        self.now = 0
                    self.last_change_url_time = time.time()

    def __init__(self, app_key=None, app_secret=None,
                 host_url='http://api-cn.ronghub.com;http://api2-cn.ronghub.com', stats_url='',
                 verify=True):
        self.app_key = self.app_key or app_key
        self.app_secret = self.app_secret or app_secret
        self.host_url = self._HostUrl(self.host or host_url)
        self.client = requests.Session()
        self.stats_url = stats_url
        # self.stats_api = StatsAPI(self.app_secret, self.app_key, self.stats_url)
        self.verify = verify

    @property
    def user(self):
        return User(self)