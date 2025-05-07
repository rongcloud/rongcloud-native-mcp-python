"""
简单的API客户端示例
"""
import asyncio
import httpx

async def call_api(url: str) -> dict:
    """调用API并返回结果"""
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()

async def main():
    """主函数"""
    base_url = "http://127.0.0.1:8000"
    
    # 调用根路径
    print("调用根路径API...")
    result = await call_api(base_url)
    print(f"响应: {result}")
    
    # 调用hello API
    name = "客户端"
    print(f"\n调用hello API，参数: {name}")
    result = await call_api(f"{base_url}/hello/{name}")
    print(f"响应: {result}")

if __name__ == "__main__":
    print("客户端启动...")
    print("确保服务器已经在 http://127.0.0.1:8000 运行")
    print("可以通过运行以下命令启动服务器:")
    print("python examples/server/simple_api.py")
    print("-" * 50)
    
    asyncio.run(main())
    print("\n客户端结束") 