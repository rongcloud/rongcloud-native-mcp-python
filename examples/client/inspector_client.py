"""
演示如何使用Inspector调试MCP服务的客户端示例
"""
import asyncio
import httpx

# 直接调用MCP服务器的API而不是使用MCP客户端
# 这样可以模拟Inspector的工作方式
async def call_mcp_tool(tool_name, arguments):
    """
    直接调用MCP工具
    
    Args:
        tool_name: 工具名称
        arguments: 工具参数
    
    Returns:
        工具调用结果
    """
    # 构建请求体，符合JSON-RPC 2.0规范
    request_body = {
        "jsonrpc": "2.0",
        "id": 1,  # 在实际应用中，每个请求应该有唯一的ID
        "method": "tools/call",
        "params": {
            "name": tool_name,
            "arguments": arguments
        }
    }
    
    async with httpx.AsyncClient() as client:
        # MCP服务器的SSE端点
        url = "http://localhost:8000/message"
        
        # 发送请求
        print(f"发送请求到MCP服务器: {request_body}")
        response = await client.post(url, json=request_body)
        
        # 检查响应
        if response.status_code == 200:
            result = response.json()
            print(f"收到响应: {result}")
            return result
        else:
            print(f"请求失败: {response.status_code} - {response.text}")
            return None

async def main():
    """主函数，演示调用MCP工具"""
    print("=== MCP调试示例 ===")
    print("提示: 可以通过以下方式使用MCP Inspector进行调试:")
    print("1. 运行: npx @modelcontextprotocol/inspector")
    print("2. 在浏览器中访问: http://localhost:xxxx")
    print("3. 连接到: http://localhost:xxxx/sse")
    print("")
    
    # 调用hello工具
    print("调用'hello'工具...")
    await call_mcp_tool("hello", {"name": "MCP调试器"})
    
    # 调用send_message工具
    print("\n调用'send_message'工具...")
    await call_mcp_tool("send_message", {
        "receiver": "测试用户",
        "content": "这是一条测试消息"
    })

if __name__ == "__main__":
    asyncio.run(main()) 