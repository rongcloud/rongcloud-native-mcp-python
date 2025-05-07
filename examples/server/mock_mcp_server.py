"""
模拟IM服务器 (Mock IM Server)

这是一个用于演示和测试的MCP服务器，它调用src/server/mcp_im_server.py中的功能。
依赖关系为：mock_mcp_server.py → mcp_im_server.py → engine.py

此服务器主要用于：
1. 提供MCP协议接口给客户端
2. 实际功能实现委托给mcp_im_server中的方法
3. 允许通过MCP Inspector进行调试和测试
"""
import sys
import os
import logging
import asyncio
from dataclasses import dataclass
from typing import Optional, Any, Dict, List
import functools
import inspect

from mcp import ServerSession

from config.config import Common

# 添加项目根目录到Python路径
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if project_root not in sys.path:
    sys.path.append(project_root)

# 导入正确的MCP模块
from mcp.server.fastmcp import FastMCP
from mcp.types import Tool

# 导入我们的工具类
from src.utils.mcp_utils import MCPServerUtils

# 由于mcp库没有导出Parameter，我们需要自己定义一个简单版本
@dataclass
class Parameter:
    description: str
    default: Optional[Any] = None

# 导入真实的IM服务器功能实现
from src.server.mcp_im_server import (
    init as real_init,
    connect as real_connect,
    send_message as real_send_message,
    get_history_messages as real_get_history_messages
)

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("mock_im_server")

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

# 创建MCP服务器应用
app = FastMCP('im-server')

# 记录SDK是否已初始化
sdk_initialized = False

# 初始化检查装饰器
def require_initialization(func):
    """确保在调用其他工具前先调用init"""
    @functools.wraps(func)  # 保留原始函数的名称和文档
    def wrapper(*args, **kwargs):
        global sdk_initialized
        # 如果是init函数，则标记为已初始化
        if func.__name__ == "init":
            result = func(*args, **kwargs)
            if result.get("success", False):
                sdk_initialized = True
                logger.info("SDK已成功初始化，现在可以使用其他工具")
            return result
        
        # 如果不是init且未初始化，则返回错误
        if not sdk_initialized:
            logger.error("尝试在SDK初始化之前调用工具，请先调用init工具")
            return {
                "success": False,
                "error": "SDK尚未初始化，请先调用init工具"
            }
        
        # 调用原始函数
        return func(*args, **kwargs)
    
    return wrapper

# 添加参数过滤装饰器
def filter_params(func):
    """过滤掉未在函数签名中定义的参数"""
    @functools.wraps(func)  # 保留原始函数的名称和文档
    def wrapper(*args, **kwargs):
        # 获取函数签名
        sig = inspect.signature(func)
        valid_params = {}
        
        # 只保留函数签名中定义的参数
        for name, param in sig.parameters.items():
            if name in kwargs:
                valid_params[name] = kwargs[name]
        
        # 如果有非预期参数，记录日志
        unexpected_params = set(kwargs.keys()) - set(valid_params.keys())
        if unexpected_params:
            logger.warning(f"调用{func.__name__}时收到非预期参数: {unexpected_params}，这些参数将被忽略")
        
        # 调用原始函数，只传递有效参数
        return func(*args, **valid_params)
    
    return wrapper

# 添加该同步工具包装器函数
def sync_tool(function_name=None, description=None):
    """将函数包装为同步MCP工具，明确设置is_async=False"""
    def decorator(func):
        nonlocal function_name, description
        if function_name is None:
            function_name = func.__name__
        if description is None:
            description = func.__doc__
            
        # 使用app._tool_manager.add_tool而不是@app.tool装饰器
        app._tool_manager.add_tool(
            fn=func,
            name=function_name,
            description=description,
            is_async=False  # 明确设置为同步函数
        )
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator

# 使用真实实现但包装为MCP工具
@require_initialization
@filter_params
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
    # 这是一个同步函数，直接调用同步的real_init函数
    logger.info(f"mock_mcp_server: 调用init (同步函数), 参数: app_key={app_key}, device_id={device_id}")
    
    # 直接调用同步函数
    result = real_init(app_key=app_key, device_id=device_id)
    logger.info(f"init结果: {result}")
    # 直接返回同步结果
    return result

@require_initialization
@filter_params
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
    # 这是一个同步函数，直接调用同步的real_connect函数
    logger.info(f"mock_mcp_server: 调用connect (同步函数), 参数: token长度={len(token)}, timeout_sec={timeout_sec}")
    try:
        # 直接调用同步函数
        result = real_connect(token=token, timeout_sec=timeout_sec)
        logger.info(f"connect结果: {result}")
        # 直接返回同步结果
        return result
    except Exception as e:
        logger.error(f"connect执行失败: {e}")
        return {"success": False, "error": str(e)}

@require_initialization
@filter_params
@app.tool("sendMessage")
def send_message(
    receiver: str = Parameter(description="消息接收者的ID"),
    content: str = Parameter(description="要发送的消息内容")
) -> Dict[str, Any]:
    """
    发送消息给指定接收者
    
    Args:
        receiver: 接收者ID或名称
        content: 消息内容
    
    Returns:
        发送结果信息
    """
    # 这是一个同步函数，直接调用同步的real_send_message函数
    logger.info(f"mock_mcp_server: 调用sendMessage (同步函数), 参数: receiver={receiver}, content={content}")
    try:
        # 直接调用同步函数
        result = real_send_message(receiver=receiver, content=content)
        logger.info(f"sendMessage结果: {result}")
        # 直接返回同步结果
        return result
    except Exception as e:
        logger.error(f"sendMessage执行失败: {e}")
        return {"success": False, "error": str(e)}

@require_initialization
@filter_params
@app.tool("getHistoryMessages")
def get_history_messages(
    user_id: str = Parameter(description="用户ID，获取与该用户的历史消息"),
    count: int = Parameter(description="要获取的消息数量", default=10)
) -> List[Dict[str, Any]]:
    """
    获取与指定用户的历史消息
    
    Args:
        user_id: 用户ID，获取与该用户的历史消息
        count: 要获取的消息数量，默认为10条
        
    Returns:
        历史消息列表
    """
    # 这是一个同步函数，直接调用同步的real_get_history_messages函数
    logger.info(f"mock_mcp_server: 调用getHistoryMessages (同步函数), 参数: user_id={user_id}, count={count}")
    try:
        # 直接调用同步函数
        result = real_get_history_messages(user_id=user_id, count=count)
        logger.info(f"getHistoryMessages结果: {len(result)}条消息")
        # 直接返回同步结果
        return result
    except Exception as e:
        logger.error(f"getHistoryMessages执行失败: {e}")
        return [{"success": False, "error": str(e)}]

# 启动和关闭逻辑
try:
    @app.on_startup
    async def startup():
        """服务器启动时执行"""
        logger.info("IM MCP服务器正在启动...")

    @app.on_shutdown
    async def shutdown():
        """服务器关闭时执行"""
        logger.info("IM MCP服务器正在关闭...")
        # 这里可以添加其他清理代码
except AttributeError:
    logger.info("FastMCP不支持on_startup和on_shutdown，将在启动时直接处理")
    # 直接在启动前记录日志
    logger.info("IM MCP服务器正在启动...")

if __name__ == "__main__":

    # TODO 发布前删除代码
    print("token : " + Common.LoginUser.token)
    # 使用SSE传输方式以便Inspector可以连接
    # 默认端口为8000，可通过参数修改
    print("\n=== IM MCP服务器启动成功 ===")
    print("此服务器调用真实的IM实现，通过mcp_im_server.py来访问IM功能。")
    print("\n调试方法:")
    print("1. 使用MCP Inspector: npx @modelcontextprotocol/inspector")
    print("2. 在Inspector中连接: http://localhost:8000/sse")
    print("3. 可用工具: init, connect, sendMessage, getHistoryMessages")
    print("注意: 使用前必须先调用init初始化SDK!")
    
    # 增加MCP超时时间
    app.request_timeout = 60  # 设置请求超时为60秒
    
    # 配置初始化要求
    app.require_init_before_use = True  # 确保在使用其他工具前必须先初始化
    
    # 如果需要自动初始化，可以在这里调用初始化函数
    # asyncio.create_task(init(app_key="您的AppKey", device_id="server_auto_init"))
    
    # 使用工具类运行应用
    MCPServerUtils.run_app(app, host="0.0.0.0", port=8000, transport="sse") 
    