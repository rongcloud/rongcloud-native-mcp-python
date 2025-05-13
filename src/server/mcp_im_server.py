"""
MCP IM服务器 - 真实IM SDK的包装器

此服务器实现了MCP协议，并直接连接到IM SDK进行消息发送和接收。

"""
import asyncio
import logging
import os
import sys
from typing import Dict, Any, List, Optional
from dataclasses import dataclass

# 添加项目根目录到Python路径
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if project_root not in sys.path:
    sys.path.append(project_root)

# 修复导入路径
from mcp import ServerSession
from mcp.server.fastmcp import FastMCP
from mcp.types import Tool

# 导入IM SDK
from src.imsdk import default_sdk

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("rc_im_mcp_server")

####################################################################################
# Temporary monkeypatch which avoids crashing when a POST message is received
# before a connection has been initialized, e.g: after a deployment.
# pylint: disable-next=protected-access
old__received_request = ServerSession._received_request


async def _received_request(self, *args, **kwargs):
    try:
        return await old__received_request(self, *args, **kwargs)
    except RuntimeError:
        pass


# pylint: disable-next=protected-access
ServerSession._received_request = _received_request
####################################################################################


# 创建MCP应用
app = FastMCP("im-server")


# 导入我们的工具类
from lib.rcim_client import RcimConversationType, RcimConversationType_Private, RcimConversationType_Group
from src.utils.mcp_utils import MCPServerUtils

# 由于mcp库没有导出Parameter，我们需要自己定义一个简单版本
@dataclass
class Parameter:
    description: str
    default: Optional[Any] = None

@app.tool("initAndConnect")
def init_and_connect(
    app_key: str = Parameter(description="应用标识（AppKey）"),
    device_id: str = Parameter(description="设备ID", default="mcp_demo"),
    token: str = Parameter(description="用户连接token"),
    timeout_sec: int = Parameter(description="连接超时时间，单位为秒", default=30)
) -> Dict[str, Any]:
    """
    初始化IM引擎并连接到IM服务器
    
    Args:
        app_key: 应用的AppKey
        device_id: 设备ID
        token: 用户连接token
        timeout_sec: 连接超时时间，单位为秒，默认为30秒
        
    Returns:
        包含初始化和连接结果的字典
    """
    logger.info(f"正在初始化并连接IM服务器，AppKey: {app_key}, 设备ID: {device_id}, token长度: {len(token)}, 超时: {timeout_sec}秒")
    
    # 第1步：初始化IM引擎
    # 确保参数是字符串类型并进行更详细的记录
    
    # 检查是否已初始化，如果已初始化则跳过初始化步骤
    if default_sdk.engine:
        logger.info(f"IM引擎初始化已经存在")
    else:
        app_key_str = str(app_key) if app_key is not None else ""
        device_id_str = str(device_id) if device_id is not None else "mcp_demo"
                    
        # 使用IMSDK的initialize方法初始化引擎
        init_result = default_sdk.initialize(app_key_str, device_id_str)
        if init_result.get("code", -1) != 0:
            logger.error(f"IM引擎初始化失败: {init_result}")
            return init_result
            
        logger.info(f"IM引擎初始化成功: {init_result}")
    
    # 第2步：连接IM服务器
    connect_result = default_sdk.engine_connect(token, timeout_sec)
    if connect_result.get("code", -1) != 0:
        logger.error(f"IM服务器连接失败: {connect_result}")
        # 返回连接结果，并标记初始化成功但连接失败
        return {
            **connect_result,
            "init_success": True,
            "connect_success": False
        }
        
    logger.info(f"IM服务器连接成功: {connect_result}")
    
    # 返回成功结果
    return {
        **connect_result,
        "init_success": True,
        "connect_success": True
    }
    
@app.tool("sendMessage")
def send_message(
    receiver: str = Parameter(description="消息接收者的ID"),
    content: str = Parameter(description="要发送的消息内容"),
    conversation_type: int = Parameter(description="会话类型，1=单聊，2=群聊", default=1)
) -> Dict[str, Any]:
    """
    发送IM消息给指定用户(单聊或群聊)
    
    Args:
        receiver: 消息接收者的ID
        content: 要发送的消息内容
        conversation_type: 会话类型，1=单聊，2=群聊，默认为单聊(1)
        
    Returns:
        包含发送结果的字典
    """
    logger.info(f"正在发送消息给 {receiver}: {content}")
    try:
        # 转换整数值为 RcimConversationType
        from lib.rcim_client import RcimConversationType_Private, RcimConversationType_Group
        
        # 根据整数值选择对应的会话类型
        real_conversation_type = RcimConversationType_Private
        if conversation_type == 2:
            real_conversation_type = RcimConversationType_Group
            
        result = default_sdk.send_message(receiver, content, real_conversation_type)
        return result
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
    messages = default_sdk.get_history_messages(user_id, count)
    logger.info(f"获取历史消息成功: {messages}")
    return messages

@app.tool("registerMessageListener")
def register_message_listener(
    client_id: str = Parameter(description="客户端ID，用于标识消息接收者")
) -> Dict[str, Any]:
    """
    注册消息监听器
    
    Args:
        client_id: 客户端唯一标识ID
        
    Returns:
        包含注册结果的字典
    """
    logger.info(f"注册消息监听器，客户端ID: {client_id}")
    
    try:
        # 调用SDK注册客户端
        result = default_sdk.register_client(client_id)
        
        if result:
            return {
                "success": True,
                "client_id": client_id,
                "message": "消息监听器注册成功"
            }
        else:
            return {
                "success": False,
                "error": "消息监听器注册失败"
            }
    except Exception as e:
        logger.error(f"注册消息监听器失败: {e}")
        return {
            "success": False,
            "error": str(e)
        }

@app.tool("unregisterMessageListener")
def unregister_message_listener(
    client_id: str = Parameter(description="客户端ID")
) -> Dict[str, Any]:
    """
    注销消息监听器
    
    Args:
        client_id: 客户端唯一标识ID
        
    Returns:
        包含注销结果的字典
    """
    logger.info(f"注销消息监听器，客户端ID: {client_id}")
    
    try:
        # 调用SDK注销客户端
        result = default_sdk.unregister_client(client_id)
        
        if result:
            return {
                "success": True,
                "message": "消息监听器注销成功"
            }
        else:
            return {
                "success": False,
                "error": "消息监听器注销失败"
            }
    except Exception as e:
        logger.error(f"注销消息监听器失败: {e}")
        return {
            "success": False,
            "error": str(e)
        }



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

# 实现基于SSE的消息推送服务（可选）
try:
    from fastapi import FastAPI, Request
    from fastapi.responses import StreamingResponse
    import json
    import asyncio

    # 创建FastAPI应用
    app_fastapi = FastAPI()

    @app_fastapi.get("/events/{client_id}")
    async def message_stream(client_id: str, request: Request):
        """SSE消息流接口"""
        logger.info(f"客户端 {client_id} 已连接SSE消息流")
        
        # 确保客户端已注册
        default_sdk.register_client(client_id)
        
        async def event_generator():
            try:
                while True:
                    # 客户端断开连接时退出
                    if await request.is_disconnected():
                        logger.info(f"客户端 {client_id} SSE连接已断开")
                        break
                    
                    # 获取所有消息
                    messages = default_sdk.get_client_messages(client_id)
                    
                    # 如果有消息，发送到客户端
                    if messages:
                        yield f"data: {json.dumps(messages)}\n\n"
                    
                    # 等待一段时间
                    await asyncio.sleep(0.5)
            except Exception as e:
                logger.error(f"SSE流处理错误: {e}")
            finally:
                # 确保在连接关闭时清理资源
                default_sdk.unregister_client(client_id)
                logger.info(f"客户端 {client_id} SSE连接资源已清理")
        
        return StreamingResponse(event_generator(), media_type="text/event-stream")

    # 修改run_server函数，支持多种传输方式
    def run_server(host: str = "127.0.0.1", port: int = 8000, transport: str = "sse"):
        """
        运行MCP服务器
        
        Args:
            host: 服务器主机地址
            port: 服务器端口
            transport: 传输协议，可选 "sse"（Server-Sent Events）、"websocket"或"stdio"
        """
        logger.info(f"启动IM MCP服务器: {host}:{port}, 传输协议: {transport}")
        
        if transport == "stdio":
            # 使用stdio方式运行
            logger.info("使用stdio传输方式")
            MCPServerUtils.run_app(app, transport="stdio")
        else:
            # 使用HTTP方式运行，支持SSE
            # 将FastAPI应用安装到MCP应用中
            from fastapi.middleware.wsgi import WSGIMiddleware
            
            # 将FastAPI应用安装到MCP应用中
            try:
                # FastMCP对象可能有不同的属性结构
                if hasattr(app, 'app'):
                    app.app.mount("/sse", WSGIMiddleware(app_fastapi))
                elif hasattr(app, 'router'):
                    app.router.mount("/sse", WSGIMiddleware(app_fastapi))
                else:
                    # 如果无法直接挂载，创建一个单独的FastAPI服务器
                    import threading
                    import uvicorn
                    
                    def run_fastapi_server():
                        logger.info(f"启动独立的FastAPI服务器（SSE）: {host}:{port+1}")
                        uvicorn.run(app_fastapi, host=host, port=port+1)
                    
                    # 在单独的线程中启动FastAPI服务器
                    fastapi_thread = threading.Thread(target=run_fastapi_server)
                    fastapi_thread.daemon = True  # 设置为守护线程，主线程结束时自动结束
                    fastapi_thread.start()
                    
                    logger.info(f"SSE服务可通过 http://{host}:{port+1}/events/{{client_id}} 访问")
            except Exception as e:
                logger.warning(f"挂载FastAPI应用时出错: {e}")
                logger.warning(f"SSE服务可能不可用，但其他MCP服务仍正常运行")
            
            # 使用工具类运行应用
            MCPServerUtils.run_app(app, host=host, port=port, transport=transport)
except Exception as e:
    logger.warning(f"设置传输层时出错: {e}")
    
    # 备用run_server函数
    def run_server(host: str = "127.0.0.1", port: int = 8000, transport: str = "sse"):
        """
        运行MCP服务器
        
        Args:
            host: 服务器主机地址
            port: 服务器端口
            transport: 传输协议，可选 "sse"（Server-Sent Events）、"websocket"或"stdio"
        """
        logger.info(f"启动IM MCP服务器: {host}:{port}, 传输协议: {transport}")
        
        if transport == "stdio":
            # 使用stdio方式运行
            logger.info("使用stdio传输方式")
            MCPServerUtils.run_app(app, transport="stdio")
        else:
            # 使用HTTP方式运行
            MCPServerUtils.run_app(app, host=host, port=port, transport=transport)

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="运行IM MCP服务器")
    parser.add_argument("--host", default="127.0.0.1", help="服务器主机地址")
    parser.add_argument("--port", type=int, default=8000, help="服务器端口")
    parser.add_argument("--transport", default="sse", choices=["sse", "websocket", "stdio"], 
                       help="传输协议，可选 'sse'（Server-Sent Events）、'websocket'或'stdio'")
    
    args = parser.parse_args()
    
    print("\n=== IM MCP服务器启动中 ===")
    print("这是连接到真实IM SDK的服务器实现，将会执行实际的消息收发。")
    print(f"\n服务器配置: {args.host}:{args.port}, 传输方式: {args.transport}")
    print("\n可用工具:")
    print("- initAndConnect: 初始化IM引擎并连接到IM服务")
    print("- sendMessage: 发送消息")
    print("- getHistoryMessages: 获取历史消息")
    print("- registerMessageListener: 注册消息监听器")
    print("- unregisterMessageListener: 注销消息监听器")
    print("\n注意: 如果只需测试，请使用examples/server/app_server.py\n")
    
    run_server(args.host, args.port, args.transport) 