import json
import logging
import os
from sys import gettrace

from utils.mcp_utils import ServerLog

# import coloredlogs

PROGRAM_NAME = 'server_interface_test'

GLOBAL_OPTS = {'thread_process_switch': True,
               'pytest_speed': {"PASS": 0, "FAIL": 0, "SKIP": 0, "TOTAL": 0, "STATUS": 1}}


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
