"""
IM聊天演示示例

一个简单的控制台聊天应用，展示如何使用IM MCP客户端收发消息
"""
import asyncio
import sys
import os
import time
from datetime import datetime

# 将src目录添加到系统路径中，以便导入模块
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.client import IMClient

async def chat_console(server_url: str = "http://127.0.0.1:8000"):
    """
    启动一个简单的控制台聊天应用
    
    Args:
        server_url: MCP服务器的URL地址
    """
    print(f"=== IM聊天演示 ===")
    print(f"连接到服务器: {server_url}")
    
    # 创建客户端
    client = IMClient(server_url)
    
    # 登录/设置用户信息
    user_id = input("请输入您的用户ID: ")
    
    while True:
        print("\n可用命令:")
        print("1. 发送消息")
        print("2. 查看历史消息")
        print("3. 退出")
        
        choice = input("请选择操作 (1-3): ")
        
        if choice == "1":
            # 发送消息
            receiver = input("接收者ID: ")
            message = input("消息内容: ")
            
            result = await client.send_message(receiver, message)
            
            if result.get("success", False):
                print(f"消息已发送!")
            else:
                print(f"发送失败: {result.get('error', '未知错误')}")
                
        elif choice == "2":
            # 查看历史消息
            other_user = input("请输入要查看历史消息的用户ID: ")
            count = input("要查看多少条消息? (默认10): ")
            
            try:
                count = int(count) if count.strip() else 10
            except ValueError:
                count = 10
                
            messages = await client.get_history_messages(other_user, count)
            
            print(f"\n=== 与 {other_user} 的历史消息 ===")
            
            if not messages or (len(messages) == 1 and "error" in messages[0]):
                if messages and "error" in messages[0]:
                    print(f"获取历史消息失败: {messages[0]['error']}")
                else:
                    print("没有历史消息")
            else:
                for msg in messages:
                    timestamp = msg.get("timestamp", "")
                    if timestamp:
                        # 转换时间戳为可读格式
                        try:
                            timestamp = datetime.fromtimestamp(float(timestamp)).strftime("%Y-%m-%d %H:%M:%S")
                        except (ValueError, TypeError):
                            pass
                    
                    sender = msg.get("sender", "未知")
                    content = msg.get("content", "")
                    
                    # 区分自己和对方的消息
                    if sender == user_id:
                        print(f"[{timestamp}] 我: {content}")
                    else:
                        print(f"[{timestamp}] {sender}: {content}")
                    
        elif choice == "3":
            # 退出
            print("再见!")
            break
            
        else:
            print("无效的选择，请重试")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="IM聊天演示")
    parser.add_argument("--server", default="http://127.0.0.1:8000", help="MCP服务器的URL地址")
    
    args = parser.parse_args()
    
    try:
        asyncio.run(chat_console(args.server))
    except KeyboardInterrupt:
        print("\n程序已终止") 