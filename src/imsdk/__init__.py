"""
IM SDK Python封装模块

用于加载和封装Rust Universal IM SDK动态库
"""
# 获取动态库文件的绝对路径
import os
import sys


_ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
_LIB_DIR = os.path.join(_ROOT_DIR, "lib")

# 添加lib目录到Python路径，确保可以导入lib.rcim_client
if _ROOT_DIR not in sys.path:
    sys.path.append(_ROOT_DIR)
    
from .engine import IMSDK, default_sdk

__all__ = ["IMSDK", "default_sdk"] 
