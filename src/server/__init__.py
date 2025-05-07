"""
IM服务器模块

导出IM服务器相关功能
"""
# 导出MCP IM服务器的主要组件
from .mcp_im_server import app, run_server, init, connect, send_message, get_history_messages

# 导出所有需要的组件
__all__ = [
    # 核心IM服务器组件
    "app", "run_server", "init", "connect", "send_message", "get_history_messages",
] 