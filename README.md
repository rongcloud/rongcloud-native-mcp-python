# MCP IM 客户端

一个基于MCP协议的即时通讯(IM)客户端SDK，可用于构建聊天应用和其他需要即时通讯功能的应用程序。

## 项目说明

本项目提供了一个简单易用的Python SDK，用于与基于MCP协议的IM服务进行交互。它包含以下组件：

1. **MCP IM 客户端**: 一个用于连接到MCP IM服务器的客户端库
2. **MCP IM 服务端**: 一个本地的IM服务器实现
3. **示例应用**: 演示如何使用客户端库的示例代码

## 功能特点

- 易于集成到现有Python应用中
- 支持发送即时消息
- 支持查询历史消息记录
- 提供异步API，易于与现代Python异步应用集成
- 详细的日志记录，方便调试和监控

## 安装

```bash
# 克隆仓库
git clone https://github.com/yourusername/mcp-im-client.git
cd mcp-im-client

# 安装依赖
pip install -r requirements.txt
```

## 使用方法

### 客户端使用

创建一个IM客户端并使用它来发送和接收消息：

```python
import asyncio
from src.client import IMClient

async def main():
    # 创建客户端实例
    client = IMClient("http://127.0.0.1:8000")
    
    # 发送消息
    result = await client.send_message("user123", "你好！这是一条测试消息")
    print(f"发送结果: {result}")
    
    # 获取历史消息
    messages = await client.get_history_messages("user123", 10)
    print(f"历史消息: {messages}")

if __name__ == "__main__":
    asyncio.run(main())
```

### 运行演示应用

项目包含一个简单的聊天演示应用，可以直接运行：

```bash
python examples/client/chat_demo.py
```

你也可以指定自定义服务器地址：

```bash
python examples/client/chat_demo.py --server http://custom-server:8080
```

## API 参考

### IMClient 类

#### 构造函数

```python
def __init__(self, server_url: str = "http://127.0.0.1:8000")
```

- `server_url`: MCP服务器的URL地址

#### 发送消息

```python
async def send_message(self, to_user: str, content: str) -> dict
```

- `to_user`: 接收消息的用户ID
- `content`: 要发送的消息内容
- 返回: 包含操作结果的字典，格式为 `{"success": bool, "error": str}`

#### 获取历史消息

```python
async def get_history_messages(self, user_id: str, count: int = 10) -> list
```

- `user_id`: 要获取与之的聊天历史的用户ID
- `count`: 要获取的消息数量，默认为10
- 返回: 消息列表，每条消息为一个字典，包含 `sender`, `content`, `timestamp` 等字段

## 配置

默认情况下，客户端会连接到 `http://127.0.0.1:8000`。你可以在创建客户端时指定不同的服务器地址。

## 示例

更多示例请查看 `examples` 目录：

- `client/chat_demo.py`: 一个简单的控制台聊天应用

## 许可证

MIT

## 贡献

欢迎提交问题和拉取请求！
