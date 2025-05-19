"""
MCP IM服务器 - 真实IM SDK的包装器

此服务器实现了MCP协议，并直接连接到IM SDK进行消息发送和接收。

"""
from collections import defaultdict, deque
from typing import Dict, Any, List
from mcp import ServerSession
from mcp.server.fastmcp import FastMCP

from imsdk import _ROOT_DIR, _LIB_DIR, default_sdk
from imsdk.engine import _USER_ID

# 修复导入路径

# 配置日志
from lib.rcim_client import RcimConversationType_Group, RcimConversationType_Private
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
client_queues = defaultdict(deque)

# TODO：删除默认值

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

    Returns:
        包含code、message、init_success(bool) 和 connect_success(bool)的字典
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
        init_result = default_sdk.engine_build(app_key_str, navi_host, device_id_str)
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
        失败：包含code和error的字典
        成功：包含code、message_id和message的字典
    """
    logger.info(f"正在发送消息给 {receiver}: {content}")
    result = default_sdk.send_message(receiver, content, conversation_type)
    return result
    

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
        失败：包含code和error的字典
        成功：包含code和message数组的字典
    """
    logger.info(f"正在获取与用户 {user_id} 的 {count} 条历史消息")
    messages = default_sdk.get_history_messages(user_id, count)
    return messages

@app.tool()
def disconnect() -> Dict[str, Any]:
    """
    断开与IM服务器的连接
    
    Returns:
        包含断开连接结果的字典
    """
    logger.info("正在断开与IM服务器的连接")
    result = default_sdk.engine_disconnect()
    return result

def close():
    """
    关闭IM引擎
    """
    default_sdk.destroy()

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
    print("- disconnect: 断开与IM服务器的连接")
    
    print(f"FastAPI SSE服务已启动: http://{args.host}:{args.port + 1}/mcp")

    app.run(transport="streamable-http")