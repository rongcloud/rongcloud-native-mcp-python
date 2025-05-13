"""
IM客户端模块

导出IM客户端相关功能
"""
# 导出主要的IM客户端类
from .mcp_im_client import IMClient

# 导出所有需要的组件
__all__ = [
    # 核心IM客户端组件
    "IMClient",
] 