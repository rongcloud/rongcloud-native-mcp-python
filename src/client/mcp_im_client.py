"""
IM MCP客户端

用于连接IM MCP服务器的客户端
"""
import asyncio
import logging
from typing import Dict, Any, List, Optional

from mcp import Client

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("mcp_im_client")

class IMClient:
    """
    IM客户端，封装MCP客户端与IM服务器的通信
    """
    
    def __init__(self, server_url: str = "http://127.0.0.1:8000"):
        """
        初始化IM客户端
        
        Args:
            server_url: MCP服务器的URL地址
        """
        self.server_url = server_url
        self.client = Client(server_url)
        logger.info(f"已初始化IM客户端，连接到服务器: {server_url}")
    
    async def send_message(self, receiver: str, content: str) -> Dict[str, Any]:
        """
        发送消息给指定用户
        
        Args:
            receiver: 消息接收者的ID
            content: 要发送的消息内容
            
        Returns:
            包含发送结果的字典
        """
        logger.info(f"正在发送消息给 {receiver}: {content}")
        try:
            result = await self.client.sendMessage(receiver=receiver, content=content)
            logger.info(f"消息发送成功: {result}")
            return result
        except Exception as e:
            logger.error(f"发送消息失败: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    async def get_history_messages(self, user_id: str, count: int = 10) -> List[Dict[str, Any]]:
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
            messages = await self.client.getHistoryMessages(user_id=user_id, count=count)
            return messages
        except Exception as e:
            logger.error(f"获取历史消息失败: {e}")
            return [{
                "error": str(e)
            }]

async def demo():
    """演示使用IM客户端的示例"""
    client = IMClient()
    
    # 发送消息
    await client.send_message("user123", "你好，这是一条测试消息!")
    
    # 获取历史消息
    messages = await client.get_history_messages("user123", 5)
    print("历史消息:")
    for msg in messages:
        if "error" in msg:
            print(f"错误: {msg['error']}")
        else:
            print(f"[{msg.get('timestamp', '')}] {msg.get('sender', '未知')}: {msg.get('content', '')}")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="运行IM MCP客户端演示")
    parser.add_argument("--server", default="http://127.0.0.1:8000", help="MCP服务器的URL地址")
    
    args = parser.parse_args()
    
    asyncio.run(demo()) 