"""
IM服务器模块

导出IM服务器相关功能
"""
# 导出MCP IM服务器的主要组件
import os
import sys

# 添加项目根目录到Python路径
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if project_root not in sys.path:
    sys.path.append(project_root)

# 尝试添加src目录到Python路径
src_path = os.path.join(project_root, "src")
if src_path not in sys.path:
    sys.path.append(src_path)


# 导出所有需要的组件
__all__ = [
    # 核心IM服务器组件
    "app", "run_server", "init", "connect", "send_message", "get_history_messages",
] 