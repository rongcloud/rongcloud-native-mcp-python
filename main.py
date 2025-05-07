"""
主入口文件
"""
import asyncio
from src.server import DemoServer
from src.client import DemoClient

async def main():
    """
    主函数，演示如何使用DemoServer和DemoClient
    """
    # 创建服务器
    server = DemoServer()
    print("服务器已创建")
    
    # 创建客户端
    client = DemoClient()
    print("客户端已创建")
    
    # 测试功能
    name = "世界"
    print(f"客户端调用say_hello({name})...")
    response = await client.say_hello(name)
    print(f"响应: {response}")

if __name__ == "__main__":
    print("启动示例...")
    asyncio.run(main())
    print("示例结束")
