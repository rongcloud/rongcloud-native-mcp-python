"""
应用服务器 (App Server)

这是一个演示应用服务器，展示如何调用src/server/mcp_im_server.py中的IM服务。
此示例不依赖MCP框架，而是通过MCP客户端调用MCP IM服务器。

主要用途：
1. 演示如何在应用层集成IM功能
2. 提供简单的API接口来调用IM服务
3. 作为如何构建应用服务器的参考

TODO：
1. 增加消息监听机制
2. 发送媒体消息
3. 获取历史消息（需要开启历史消息云存储）
4. engine代码整理
5. 取消获取token机制 直接传token（提前commit）

其他非高优优化
1. 将init与connect方法合并
2. mcp inspector 中默认值设置和注释设置

"""
import sys
import os
import logging
import json
import asyncio
from typing import Dict, Any, List, Optional
import time
import uuid
import argparse
import random

# 添加项目根目录到Python路径
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if project_root not in sys.path:
    sys.path.append(project_root)
        

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("app_server")

# MCP IM服务器地址
MCP_SERVER_URL = "http://127.0.0.1:8000"

# 应用服务器状态
sdk_initialized = False

# 导入正确的MCP客户端
from src.client import IMClient

class IMServiceClient:
    """IM服务客户端，使用MCP客户端与MCP IM服务器通信"""
    
    def __init__(self, server_url: str = MCP_SERVER_URL):
        """
        初始化IM服务客户端
        
        Args:
            server_url: MCP服务器的URL地址
        """
        self.server_url = server_url
        self.client = IMClient(server_url)
        logger.info(f"初始化IM服务客户端，服务器地址: {server_url}")
    
    async def call_service(self, tool_name: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        调用MCP服务的通用方法
        
        Args:
            tool_name: 工具名称
            params: 参数字典
            
        Returns:
            服务调用结果
        """
        try:
            # 记录请求信息
            logger.info(f"调用IM服务: {tool_name}, 参数: {params}")
            
            # 使用IM客户端真正调用MCP服务器
            if tool_name == "init":
                # 直接调用IMClient的call_tool方法
                return await self.client.call_tool(tool_name, params)
                
            elif tool_name == "connect":
                # 调用连接方法
                return await self.client.call_tool(tool_name, params)
                
            elif tool_name == "sendMessage":
                # 提取参数
                receiver = params.get("receiver", "")
                content = params.get("content", "")
                conversation_type = params.get("conversation_type", 1)
                
                # 构建完整参数
                message_params = {
                    "receiver": receiver,
                    "content": content,
                    "conversation_type": conversation_type
                }
                
                # 调用发送消息方法
                return await self.client.call_tool("sendMessage", message_params)
                
            elif tool_name == "getHistoryMessages":
                # 提取参数
                user_id = params.get("user_id", "")
                count = params.get("count", 10)
                
                # 构建参数
                history_params = {
                    "user_id": user_id,
                    "count": count
                }
                
                # 调用获取历史消息方法
                return await self.client.call_tool("getHistoryMessages", history_params)
                
            elif tool_name == "registerMessageListener":
                # 提取参数
                client_id = params.get("client_id", "")
                
                # 构建参数
                register_params = {
                    "client_id": client_id
                }
                
                # 调用注册监听器方法
                return await self.client.call_tool("registerMessageListener", register_params)
                
            elif tool_name == "unregisterMessageListener":
                # 提取参数
                client_id = params.get("client_id", "")
                
                # 构建参数
                unregister_params = {
                    "client_id": client_id
                }
                
                # 调用注销监听器方法
                return await self.client.call_tool("unregisterMessageListener", unregister_params)
                
            elif tool_name == "pullMessages":
                # 提取参数
                client_id = params.get("client_id", "")
                max_count = params.get("max_count", 20)
                
                # 构建参数
                pull_params = {
                    "client_id": client_id,
                    "max_count": max_count
                }
                
                # 调用拉取消息方法
                result = await self.client.call_tool("pullMessages", pull_params)
                
                # 确保返回结果包含messages字段
                if isinstance(result, dict) and "messages" not in result and "success" in result and result["success"]:
                    result["messages"] = []
                
                return result
                
            else:
                logger.error(f"未知的工具名称: {tool_name}")
                return {
                    "success": False,
                    "error": f"未知的工具名称: {tool_name}"
                }
        except Exception as e:
            error_msg = f"调用服务时发生异常: {e}"
            logger.error(error_msg)
            return {
                "success": False,
                "error": error_msg
            }

# 创建全局IM服务客户端实例
im_client = IMServiceClient()

async def init(app_key: str, device_id: str = "app_server_demo") -> Dict[str, Any]:
    """
    初始化IM引擎
    
    Args:
        app_key: 应用的AppKey
        device_id: 设备ID
        
    Returns:
        包含初始化结果的字典
    """
    global sdk_initialized
    
    logger.info(f"初始化IM引擎, 参数: app_key={app_key}, device_id={device_id}")
    
    # 调用服务
    result = await im_client.call_service("init", {
        "app_key": app_key,
        "device_id": device_id
    })
    
    # 更新状态
    if result.get("success", False):
        sdk_initialized = True
        logger.info("IM引擎初始化成功")
    else:
        logger.error(f"IM引擎初始化失败: {result.get('error', '未知错误')}")
    
    return result

async def connect(token: str) -> Dict[str, Any]:
    """
    连接IM服务器
    
    Args:
        token: 用户连接token
        
    Returns:
        包含连接结果的字典
    """
    global sdk_initialized
    
    if not sdk_initialized:
        logger.error("尝试在SDK初始化之前连接服务，请先调用init函数")
        return {
            "success": False,
            "error": "SDK尚未初始化，请先调用init函数"
        }
    
    logger.info(f"连接IM服务器, token长度={len(token)}")
    
    # 调用服务
    result = await im_client.call_service("connect", {
        "token": token
    })
    
    if result.get("success", False):
        logger.info("IM服务器连接成功")
    else:
        logger.error(f"IM服务器连接失败: {result.get('error', '未知错误')}")
    
    return result

async def send_message(receiver: str, content: str, conversation_type: int = 1) -> Dict[str, Any]:
    """
    发送IM消息给指定用户(单聊或群聊)
    
    Args:
        receiver: 消息接收者的ID
        content: 要发送的消息内容
        conversation_type: 会话类型，1=单聊，2=群聊，默认为单聊(1)
        
    Returns:
        包含发送结果的字典
    """
    if not sdk_initialized:
        logger.error("尝试在SDK初始化之前发送消息，请先调用init函数")
        return {
            "success": False,
            "error": "SDK尚未初始化，请先调用init函数"
        }
    
    logger.info(f"发送消息给 {receiver}: {content}, 会话类型: {conversation_type}")
    
    # 调用服务
    result = await im_client.call_service("sendMessage", {
        "receiver": receiver,
        "content": content,
        "conversation_type": conversation_type
    })
    
    if result.get("success", False):
        logger.info("消息发送成功")
    else:
        logger.error(f"消息发送失败: {result.get('error', '未知错误')}")
    
    return result

async def send_media_message(receiver: str, media_type: str, media_url: str, conversation_type: int = 1) -> Dict[str, Any]:
    """
    发送媒体消息给指定用户(单聊或群聊)
    
    Args:
        receiver: 消息接收者的ID
        media_type: 媒体类型，如 'image', 'video', 'audio', 'file'
        media_url: 媒体文件的URL或本地路径
        conversation_type: 会话类型，1=单聊，2=群聊，默认为单聊(1)
        
    Returns:
        包含发送结果的字典
    """
    if not sdk_initialized:
        logger.error("尝试在SDK初始化之前发送媒体消息，请先调用init函数")
        return {
            "success": False,
            "error": "SDK尚未初始化，请先调用init函数"
        }
    
    logger.info(f"发送媒体消息给 {receiver}，类型: {media_type}，URL: {media_url}，会话类型: {conversation_type}")
    
    # 构建媒体消息内容
    media_content = json.dumps({
        "type": media_type,
        "url": media_url,
        "format": "media"  # 标记为媒体消息格式
    })
    
    # 调用发送消息服务
    return await send_message(receiver, media_content, conversation_type)

async def get_history_messages(user_id: str, count: int = 10) -> List[Dict[str, Any]]:
    """
    获取与指定用户的历史消息
    
    Args:
        user_id: 用户ID，获取与该用户的历史消息
        count: 要获取的消息数量，默认为10条
        
    Returns:
        历史消息列表
    """
    if not sdk_initialized:
        logger.error("尝试在SDK初始化之前获取历史消息，请先调用init函数")
        return [{
            "error": "SDK尚未初始化，请先调用init函数"
        }]
    
    logger.info(f"获取与用户 {user_id} 的 {count} 条历史消息")
    
    # 调用服务
    result = await im_client.call_service("getHistoryMessages", {
        "user_id": user_id,
        "count": count
    })
    
    if isinstance(result, List):
        return result
    else:
        # 如果结果不是列表，则返回空列表或错误信息
        if "error" in result:
            return [{
                "error": result.get("error", "未知错误")
            }]
        return []

async def register_message_listener(client_id: str = None) -> Dict[str, Any]:
    """
    注册消息监听器
    
    Args:
        client_id: 客户端唯一标识ID，如果为None则自动生成
        
    Returns:
        包含注册结果的字典
    """
    if not sdk_initialized:
        logger.error("尝试在SDK初始化之前注册消息监听器，请先调用init函数")
        return {
            "success": False,
            "error": "SDK尚未初始化，请先调用init函数"
        }
    
    # 如果未提供client_id，生成一个
    if not client_id:
        client_id = f"client_{uuid.uuid4()}"
    
    logger.info(f"注册消息监听器，客户端ID: {client_id}")
    
    # 调用服务
    result = await im_client.call_service("registerMessageListener", {
        "client_id": client_id
    })
    
    if result.get("success", False):
        logger.info("消息监听器注册成功")
    else:
        logger.error(f"消息监听器注册失败: {result.get('error', '未知错误')}")
    
    # 确保结果中包含client_id
    if result.get("success", False) and "client_id" not in result:
        result["client_id"] = client_id
    
    return result

async def unregister_message_listener(client_id: str) -> Dict[str, Any]:
    """
    注销消息监听器
    
    Args:
        client_id: 客户端唯一标识ID
        
    Returns:
        包含注销结果的字典
    """
    if not sdk_initialized:
        logger.error("尝试在SDK初始化之前注销消息监听器，请先调用init函数")
        return {
            "success": False,
            "error": "SDK尚未初始化，请先调用init函数"
        }
    
    logger.info(f"注销消息监听器，客户端ID: {client_id}")
    
    # 调用服务
    result = await im_client.call_service("unregisterMessageListener", {
        "client_id": client_id
    })
    
    if result.get("success", False):
        logger.info("消息监听器注销成功")
    else:
        logger.error(f"消息监听器注销失败: {result.get('error', '未知错误')}")
    
    return result

async def pull_messages(client_id: str, max_count: int = 20) -> Dict[str, Any]:
    """
    从服务器拉取新消息
    
    Args:
        client_id: 客户端唯一标识ID
        max_count: 最大获取消息数量
        
    Returns:
        包含消息列表的字典
    """
    if not sdk_initialized:
        logger.error("尝试在SDK初始化之前拉取消息，请先调用init函数")
        return {
            "success": False,
            "error": "SDK尚未初始化，请先调用init函数",
            "messages": []
        }
    
    logger.info(f"拉取消息，客户端ID: {client_id}, 最大数量: {max_count}")
    
    # 调用服务
    result = await im_client.call_service("pullMessages", {
        "client_id": client_id,
        "max_count": max_count
    })
    
    if result.get("success", False):
        logger.info(f"成功拉取 {len(result.get('messages', []))} 条消息")
    else:
        logger.error(f"拉取消息失败: {result.get('error', '未知错误')}")
    
    return result

async def run_demo_async():
    """异步运行演示程序"""
    print("\n=== IM应用服务器演示 ===")
    print("这是一个简单的演示，展示如何调用MCP IM服务。")
    
    # 初始化
    init_result = await init(Config.appKey)
    if not init_result.get("success", False):
        print(f"初始化失败: {init_result.get('error', '未知错误')}")
        return
    
    # 连接
    connect_result = await connect(Config.LoginUser.token)
    if not connect_result.get("success", False):
        print(f"连接失败: {connect_result.get('error', '未知错误')}")
        return
    
    # 注册消息监听器
    client_id = f"demo_client_{int(time.time())}"
    register_result = await register_message_listener(client_id)
    if not register_result.get("success", False):
        print(f"注册消息监听器失败: {register_result.get('error', '未知错误')}")
        return
    
    print("\n消息监听已启动，您可以通过以下命令操作:")
    print("1. 发送文本消息: send 接收者ID 消息内容")
    print("2. 发送媒体消息: media 接收者ID 媒体类型 媒体URL")
    print("3. 拉取消息: pull")
    print("4. 获取历史消息: history 用户ID [条数]")
    print("5. 退出: exit 或 quit\n")
    
    while True:
        try:
            cmd = await asyncio.get_event_loop().run_in_executor(None, lambda: input("> ").strip())
            
            if cmd in ["exit", "quit"]:
                break
            
            parts = cmd.split(" ", 3)  # 最多分割3部分
            
            if parts[0] == "send" and len(parts) >= 3:
                receiver = parts[1]
                content = parts[2]
                result = await send_message(receiver, content)
                print(f"发送结果: {result}")
            
            elif parts[0] == "media" and len(parts) >= 4:
                receiver = parts[1]
                media_type = parts[2]
                media_url = parts[3]
                result = await send_media_message(receiver, media_type, media_url)
                print(f"媒体消息发送结果: {result}")
            
            elif parts[0] == "pull":
                result = await pull_messages(client_id)
                messages = result.get("messages", [])
                if messages:
                    print(f"收到 {len(messages)} 条新消息:")
                    for msg in messages:
                        sender = msg.get("sender_id", "未知")
                        content = msg.get("content", "")
                        
                        # 尝试解析可能的JSON格式媒体消息
                        try:
                            content_obj = json.loads(content)
                            if isinstance(content_obj, dict) and content_obj.get("format") == "media":
                                content = f"[{content_obj.get('type', '媒体')}]: {content_obj.get('url', '无URL')}"
                        except (json.JSONDecodeError, TypeError):
                            pass  # 不是JSON格式，保持原样
                        
                        print(f"[{sender}]: {content}")
                else:
                    print("没有新消息")
            
            elif parts[0] == "history" and len(parts) >= 2:
                user_id = parts[1]
                count = int(parts[2]) if len(parts) >= 3 else 10
                messages = await get_history_messages(user_id, count)
                print(f"历史消息（{len(messages)}条）:")
                for msg in messages:
                    if "error" in msg:
                        print(f"错误: {msg['error']}")
                    else:
                        sender = msg.get("sender_id", "未知")
                        content = msg.get("content", "")
                        
                        # 尝试解析可能的JSON格式媒体消息
                        try:
                            content_obj = json.loads(content)
                            if isinstance(content_obj, dict) and content_obj.get("format") == "media":
                                content = f"[{content_obj.get('type', '媒体')}]: {content_obj.get('url', '无URL')}"
                        except (json.JSONDecodeError, TypeError):
                            pass  # 不是JSON格式，保持原样
                        
                        print(f"[{sender}]: {content}")
            
            else:
                print("无效命令，请使用以下格式:")
                print("  send 接收者ID 消息内容")
                print("  media 接收者ID 媒体类型 媒体URL")
                print("  pull")
                print("  history 用户ID [条数]")
                print("  exit 或 quit")
        
        except Exception as e:
            print(f"执行命令时出错: {e}")
    
    # 注销监听器
    await unregister_message_listener(client_id)
    print("演示结束，已注销消息监听器")

def run_demo():
    """运行演示程序的同步入口点"""
    # 创建事件循环并运行异步函数
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_demo_async())

if __name__ == "__main__":
    print("\n要自定义服务器地址，可以使用以下命令：")
    print('python examples/server/app_server.py --server http://custom-server:8080')
    print("默认使用地址：", MCP_SERVER_URL)
    
    parser = argparse.ArgumentParser(description="运行IM应用服务器演示")
    parser.add_argument("--server", default=MCP_SERVER_URL, help="MCP服务器的URL地址")
    
    args = parser.parse_args()
    
    # 更新服务器地址
    if args.server != MCP_SERVER_URL:
        im_client = IMServiceClient(args.server)
        MCP_SERVER_URL = args.server
    
    run_demo() 
    