"""
MCP IM服务器 - 真实IM SDK的包装器

此服务器实现了MCP协议，并直接连接到IM SDK进行消息发送和接收。
"""
import asyncio
import logging
from typing import Dict, Any, List, Optional
from dataclasses import dataclass
import os
import ctypes

# 修复导入路径
from mcp.server.fastmcp import FastMCP
from mcp.types import Tool

# 导入我们的工具类
from src.utils.mcp_utils import MCPServerUtils

# 由于mcp库没有导出Parameter，我们需要自己定义一个简单版本
@dataclass
class Parameter:
    description: str
    default: Optional[Any] = None

from imsdk import default_sdk

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("rc_im_mcp_server")

# 创建MCP应用
app = FastMCP("im-server")

@app.tool("init")
def init(
    app_key: str = Parameter(description="应用标识（AppKey）"),
    device_id: str = Parameter(description="设备ID", default="mcp_demo")
) -> Dict[str, Any]:
    """
    初始化IM引擎
    
    Args:
        app_key: 应用的AppKey
        device_id: 设备ID
        
    Returns:
        包含初始化结果的字典
    """
    logger.info(f"正在初始化IM引擎，AppKey类型: {type(app_key)}, 值: {app_key}, 设备ID类型: {type(device_id)}, 值: {device_id}")
    try:
        # 确保参数是字符串类型并进行更详细的记录
        app_key_str = str(app_key) if app_key is not None else ""
        device_id_str = str(device_id) if device_id is not None else "mcp_demo"
        
        logger.info(f"转换后 - AppKey类型: {type(app_key_str)}, 值: {app_key_str}, 设备ID类型: {type(device_id_str)}, 值: {device_id_str}")
                
        # 使用IMSDK的initialize方法初始化引擎
        result = default_sdk.initialize(app_key_str, device_id_str)
        if result.get("success", False):
            logger.info(f"IM引擎初始化成功: {result}")
        else:
            logger.error(f"IM引擎初始化失败: {result.get('error', '未知错误')}")
        return result
    except Exception as e:
        import traceback
        logger.error(f"IM引擎初始化过程中发生异常: {e}")
        logger.error(f"异常堆栈: {traceback.format_exc()}")
        return {
            "success": False,
            "error": str(e)
        }

@app.tool("connect")
def connect(
    token: str = Parameter(description="用户连接token"),
    timeout_sec: int = Parameter(description="连接超时时间，单位为秒", default=30)
) -> Dict[str, Any]:
    """
    连接IM服务器
    
    Args:
        token: 用户连接token
        timeout_sec: 连接超时时间，单位为秒，默认为30秒
        
    Returns:
        包含连接结果的字典
    """
    logger.info(f"正在连接IM服务器，token长度: {len(token)}, 超时: {timeout_sec}秒")
    try:
        result = default_sdk.engine_connect(token, timeout_sec)
        if result.get("success", False):
            logger.info(f"IM服务器连接成功: {result}")
        else:
            logger.error(f"IM服务器连接失败: {result.get('error', '未知错误')}")
        return result
    except Exception as e:
        logger.error(f"IM服务器连接过程中发生异常: {e}")
        return {
            "success": False,
            "error": str(e)
        }

@app.tool("sendMessage")
def send_message(
    receiver: str = Parameter(description="消息接收者的ID"),
    content: str = Parameter(description="要发送的消息内容"),
) -> Dict[str, Any]:
    """
    发送IM消息给指定用户
    
    Args:
        receiver: 消息接收者的ID
        content: 要发送的消息内容
        
    Returns:
        包含发送结果的字典
    """
    logger.info(f"正在发送消息给 {receiver}: {content}")
    try:
        result = default_sdk.send_message(receiver, content)
        return {
            "success": True,
            "message_id": result.get("message_id", "unknown"),
            "timestamp": result.get("timestamp", 0),
        }
    except Exception as e:
        logger.error(f"发送消息失败: {e}")
        return {
            "success": False,
            "error": str(e)
        }

@app.tool("getHistoryMessages")
def get_history_messages(
    user_id: str = Parameter(description="用户ID，获取与该用户的历史消息"),
    count: int = Parameter(description="要获取的消息数量", default=10),
) -> List[Dict[str, Any]]:
    """
    获取与指定用户的历史消息
    
    Args:
        user_id: 用户ID，获取与该用户的历史消息
        count: 要获取的消息数量，默认为10条
        
    Returns:
        历史消息列表
    """
    logger.info(f"正在获取与用户 {user_id} 的 {count} 条历史消息")
    try:
        messages = default_sdk.get_history_messages(user_id, count)
        return messages
    except Exception as e:
        logger.error(f"获取历史消息失败: {e}")
        return [{
            "error": str(e)
        }]

# 检查FastMCP是否支持on_startup和on_shutdown
# 如果不支持，则改用其他方式处理启动和关闭逻辑
try:
    @app.on_startup
    async def startup():
        """服务器启动时执行"""
        logger.info("IM MCP服务器正在启动...")

    @app.on_shutdown
    async def shutdown():
        """服务器关闭时执行"""
        logger.info("IM MCP服务器正在关闭...")
        # 确保SDK资源被释放
        default_sdk.close()
except AttributeError:
    logger.info("FastMCP不支持on_startup和on_shutdown，将在run_server中处理启动和关闭逻辑")
    # 定义启动和关闭函数
    async def startup():
        """服务器启动时执行"""
        logger.info("IM MCP服务器正在启动...")

    async def shutdown():
        """服务器关闭时执行"""
        logger.info("IM MCP服务器正在关闭...")
        # 确保SDK资源被释放
        default_sdk.close()

def run_server(host: str = "127.0.0.1", port: int = 8000, transport: str = "sse"):
    """
    运行MCP服务器
    
    Args:
        host: 服务器主机地址
        port: 服务器端口
        transport: 传输协议，可选 "sse"（Server-Sent Events）或 "websocket"
    """
    logger.info(f"启动IM MCP服务器: {host}:{port}, 传输协议: {transport}")
    
    # 使用工具类运行应用
    MCPServerUtils.run_app(app, host=host, port=port, transport=transport)

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="运行IM MCP服务器")
    parser.add_argument("--host", default="127.0.0.1", help="服务器主机地址")
    parser.add_argument("--port", type=int, default=8000, help="服务器端口")
    parser.add_argument("--transport", default="sse", choices=["sse", "websocket"], 
                       help="传输协议，可选 'sse'（Server-Sent Events）或 'websocket'")
    
    args = parser.parse_args()
    
    print("\n=== IM MCP服务器启动中 ===")
    print("这是连接到真实IM SDK的服务器实现，将会执行实际的消息收发。")
    print(f"\n服务器配置: {args.host}:{args.port}, 传输方式: {args.transport}")
    print("\n可用工具:")
    print("- init: 初始化IM引擎")
    print("- connect: 连接到IM服务")
    print("- sendMessage: 发送消息")
    print("- getHistoryMessages: 获取历史消息")
    print("\n注意: 如果只需测试，请使用examples/server/mock_mcp_server.py\n")
    
    run_server(args.host, args.port, args.transport) 