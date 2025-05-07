"""
使用自定义DemoClient的客户端示例
"""
import asyncio
from src.client import DemoClient

async def main():
    """主函数，演示如何使用DemoClient"""
    # 创建客户端
    client = DemoClient()
    print("客户端已创建")
    
    # 调用不同名称的hello方法
    names = ["世界", "Python", "MCP"]
    
    for name in names:
        print(f"\n调用say_hello(\"{name}\")...")
        response = await client.say_hello(name)
        print(f"响应: {response}")

if __name__ == "__main__":
    print("DemoClient客户端示例启动...")
    print("-" * 50)
    
    asyncio.run(main())
    print("\nDemoClient客户端示例结束") 