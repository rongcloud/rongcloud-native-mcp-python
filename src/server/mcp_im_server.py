"""
MCP IM服务器 - 真实IM SDK的包装器

此服务器实现了MCP协议，并直接连接到IM SDK进行消息发送和接收。

"""
import asyncio
import json
import os
import sys
import threading
from typing import Dict, Any, List
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
import asyncio

# 添加项目根目录到Python路径
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if project_root not in sys.path:
    sys.path.append(project_root)

# 修复导入路径
from mcp import ServerSession
from mcp.server.fastmcp import FastMCP

# 导入IM SDK
from src.imsdk import default_sdk

# 配置日志
from src.utils.mcp_utils import ServerLog
logger = ServerLog.getLogger("rc_im_mcp_server")

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
app_fastapi = FastAPI()

@app.tool()
def init_and_connect(
    app_key: str = "c9kqb3rdkbb8j",
    navi_host: str = "nav-aliqa.rongcloud.net",
    device_id: str = "mcp_demo",
    token: str = "9wsuWlmIb40dlPLyqnPPDg4tAoQYZad98YSv/s428ofgnNDij3yLM3JlkLD9dTPSmyX6mtamT12R6SRDHOAAfQ==",
    timeout_sec: int = 30
) -> Dict[str, Any]:
    """
    初始化IM引擎并连接到IM服务器
    
    Args:
        app_key: 应用的AppKey"
        navi_host: 导航地址
        device_id: 设备ID
        token: 用户连接token
        timeout_sec: 连接超时时间，单位为秒
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
        init_result = default_sdk.initialize(app_key_str, navi_host, device_id_str)
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
    
@app.tool()
def send_message(
    receiver: str = "DXIhdtUm7",
    content: str = "测试消息",
    conversation_type: int = 1
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

@app.tool()
def get_history_messages(
    user_id: str = "DXIhdtUm7",
    count: int = 10,
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
    return messages

@app.tool()
async def subscribe_chat_message() -> Dict[str, Any]:
    default_sdk.register_message_callback()
    return {"code": 0, "message": "消息订阅成功"}

@app.tool()
async def unsubscribe_chat_message() -> Dict[str, Any]:
    default_sdk.unregister_message_callback()
    return {"code": 0, "message": "消息订阅取消成功"}

@app_fastapi.get("/mcp")
async def mcp_message_stream():
    print("`11`")
    async def event_generator():
        while True:
            print("123")
            if not default_sdk.is_listening_message():
                continue
            # 1. 检查新消息（从队列/数据库/事件总线）
            datas = default_sdk.rust_listener.response['RcimMessageReceivedLsr']
            if len(datas) > 0:
                print(f"_____收到消息: {len(datas)}")
                with threading.Lock():
                    datas = default_sdk.rust_listener.response['RcimMessageReceivedLsr']
                    default_sdk.rust_listener.response['RcimMessageReceivedLsr'].clear()
                while len(datas) > 0:
                    datas.reverse()
                    data = datas.pop()
                    result = json.dumps(data)
                    print(f"收到消息: {result}")
                    yield f"{result}\n\n"
            yield f"{json.dumps(datas)}\n\n"
            # 每1秒循环一次，避免高频空转
            await asyncio.sleep(1)
            
    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={"Mcp-Protocol": "2025-03-26"}
    )

# 定义启动和关闭函数
async def startup():
    """服务器启动时执行"""
    logger.info("IM MCP服务器正在启动...")

async def shutdown():
    """服务器关闭时执行"""
    logger.info("IM MCP服务器正在关闭...")
    # 确保SDK资源被释放
    default_sdk.close()

    
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="运行IM MCP服务器")
    parser.add_argument("--host", default="127.0.0.1", help="服务器主机地址")
    parser.add_argument("--port", type=int, default=8000, help="服务器端口")
    parser.add_argument("--transport", default="streamable-http", choices=["sse", "streamable-http", "stdio"], 
                       help="传输协议，可选 'sse'（Server-Sent Events）、'streamable-http'或'stdio'")
    
    args = parser.parse_args()
    
    print("\n=== IM MCP服务器启动中 ===")
    print("这是连接到真实IM SDK的服务器实现，将会执行实际的消息收发。")
    print(f"\n服务器配置: {args.host}:{args.port}, 传输方式: {args.transport}")
    print("\n可用工具:")
    print("- init_and_connect: 初始化IM引擎并连接到IM服务")
    print("- send_message: 发送消息")
    print("- get_history_messages: 获取历史消息")
    print("- register_message_listener: 注册消息监听器")
    print("- unregister_message_listener: 注销消息监听器")
    
    app.run(transport="streamable-http")