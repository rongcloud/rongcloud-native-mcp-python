"""
实时聊天演示应用

展示如何使用IM MCP客户端与MCP IM服务器通信实现实时聊天
"""
import asyncio
import sys
import os
import signal
from datetime import datetime

# 将src目录添加到系统路径中
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# 导入MCP IM客户端
from examples.server.config.config import Common, Config
from src.client import IMClient

# 全局客户端实例
client = None

async def handle_new_message(message):
    """
    处理新收到的消息
    
    Args:
        message: 消息数据对象
    """
    sender = message.get("sender_id", "未知")
    content = message.get("content", "")
    timestamp = message.get("timestamp", 0)
    
    # 格式化时间戳
    if timestamp:
        try:
            # 转换时间戳为可读格式
            time_str = datetime.fromtimestamp(timestamp / 1000).strftime("%H:%M:%S")
        except (ValueError, TypeError):
            time_str = "未知时间"
    else:
        time_str = "未知时间"
    
    # 打印消息，避免干扰用户输入
    print(f"\n[{time_str}] {sender}: {content}")
    print(">>> ", end="", flush=True)  # 重新显示输入提示

async def shutdown(client):
    """关闭客户端连接并清理资源"""
    print("\n正在关闭连接...")
    try:
        # 注销消息监听器
        await client.unregister_message_listener()
        # 关闭客户端连接
        await client.close()
        print("连接已关闭")
    except Exception as e:
        print(f"关闭连接时出错: {e}")
    
    # 确保程序退出
    asyncio.get_event_loop().stop()

async def main():
    """主函数"""
    global client
    
    print("=== MCP通信实时聊天应用 ===")
    
    # 获取服务器地址
    server_url = "http://127.0.0.1:8000"
    print(f"连接到MCP服务器: {server_url}")
    
    # 创建MCP客户端
    client = IMClient(server_url)
    
    # 初始化和连接客户端
    print("正在初始化并连接IM引擎...")
    init_connect_result = await client.initAndConnect({
        "app_key": Config.appKey,
        "device_id": f"chat_client_{os.getpid()}",
        "token": Common.LoginUser.token,
        "timeout_sec": 30
    })
    
    if not init_connect_result.get("success", False):
        print(f"初始化或连接失败: {init_connect_result.get('error', '未知错误')}")
        return
    
    print("初始化和连接成功！")
    
    # 启动消息监听，使用通知方式
    print("正在注册消息监听器并启动通知...")
    try:    
        register_result = await client.register_message_listener(handle_new_message)
        
        if not register_result.get("success", False):
            print(f"注册消息监听器失败: {register_result.get('error', '未知错误')}")
            return
    except Exception as e:
        print(f"注册消息监听器异常: {e}")
        return
    
    print("消息监听已启动，您将收到实时消息提醒")
    print("发送格式: @用户ID 消息内容")
    print("输入'exit'退出")
    
    # 设置信号处理，确保程序可以正常退出
    loop = asyncio.get_event_loop()
    for sig in (signal.SIGINT, signal.SIGTERM):
        try:
            loop.add_signal_handler(sig, lambda: asyncio.create_task(shutdown(client)))
        except NotImplementedError:
            # Windows不支持add_signal_handler
            pass
    
    try:
        while True:
            print(">>> ", end="", flush=True)
            command = await loop.run_in_executor(None, input)
            
            if command.lower() == "exit":
                break
                
            # 解析命令: @userId 消息内容
            if command.startswith("@"):
                parts = command.split(" ", 1)
                if len(parts) < 2:
                    print("格式错误，请使用: @用户ID 消息内容")
                    continue
                    
                receiver = parts[0][1:]  # 去除@前缀
                content = parts[1]
                
                # 发送消息
                send_result = await client.call_tool("sendMessage", {
                    "receiver": receiver,
                    "content": content,
                    "conversation_type": 1  # 单聊
                })
                
                if send_result.get("success", False):
                    message_id = send_result.get("message_id", "未知")
                    print(f"消息已发送给 {receiver}, 消息ID: {message_id}")
                else:
                    print(f"发送失败: {send_result.get('error', '未知错误')}")
            else:
                print("格式错误，请使用: @用户ID 消息内容")
    finally:
        await shutdown(client)

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="MCP通信实时聊天应用")
    parser.add_argument("--server", default="http://127.0.0.1:8000", help="MCP服务器的URL地址")
    
    args = parser.parse_args()
    
    # 更新服务器地址
    if args.server:
        server_url = args.server
    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n程序已被用户中断")