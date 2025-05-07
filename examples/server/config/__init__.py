import json
import logging
import os
from sys import gettrace

# import coloredlogs

PROGRAM_NAME = 'server_interface_test'

GLOBAL_OPTS = {'thread_process_switch': True,
               'pytest_speed': {"PASS": 0, "FAIL": 0, "SKIP": 0, "TOTAL": 0, "STATUS": 1}}

class ServerLog:
    __instances = {}
    level = None

    def __init__(self, level=None):
        self.level = level

    @classmethod
    def getLogger(cls, name=os.path.abspath(__name__)) -> logging.Logger:
        if name not in cls.__instances:
            logger = logging.getLogger(name)
            fmt = '%(asctime)s [%(levelname)s] [%(name)s] %(filename)s[line:%(lineno)d] %(message)s'
            formater = logging.Formatter(fmt)
            ch = logging.StreamHandler()
            ch.setLevel(cls.level or ServerLog.__getLogLevel())
            ch.setFormatter(formater)
            logger.addHandler(ch)
            # coloredlogs.install(fmt=fmt, level=cls.level or ServerLog.__getLogLevel(), logger=logger)
            logger.setLevel(cls.level or ServerLog.__getLogLevel())
            cls.__instances[name] = logger
        return cls.__instances[name]

    @staticmethod  # 设置日志等级
    def __getLogLevel():
        if os.environ.get("DEBUG") in ("1", "on", "true"):
            return logging.DEBUG
        if os.environ.get("ERROR") in ("1", "on", "true"):
            return logging.ERROR
        if gettrace():
            return logging.DEBUG
        else:
            return logging.INFO


RLOG = ServerLog.getLogger('RMTP')
ALOG = ServerLog.getLogger('API')


def get_app_dir(*paths) -> str:
    home = os.path.expanduser("~")
    appdir = os.path.join(home, "." + PROGRAM_NAME)
    if paths:
        appdir = os.path.join(appdir, *paths)
    os.makedirs(appdir, exist_ok=True)
    return appdir


def save_node(name, data):
    if GLOBAL_OPTS.get('diff'):
        if GLOBAL_OPTS.get('nodeid'):
            if isinstance(data, dict):
                GLOBAL_OPTS['nodedata'].append({name: json.dumps(data)})
            elif isinstance(data, bytes):
                GLOBAL_OPTS['nodedata'].append({name: data.hex()})


def convert_json(req):
    ret = req.content
    try:
        ret = req.json()
    except:
        pass
    return ret
