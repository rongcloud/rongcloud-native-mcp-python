# MCP IM 示例

本目录包含了使用MCP协议的IM服务器示例实现。这些示例旨在帮助您了解如何使用MCP协议来构建IM应用。

## 目录结构

- `server/`: 服务器示例
  - `mock_mcp_server.py`: 模拟IM服务器（不依赖实际IM SDK）
- `client/`: 客户端示例（待添加）

## 模拟服务器 vs 实际实现

本项目包含两种服务器实现：

### 1. 模拟服务器 (`examples/server/mock_mcp_server.py`)

- **用途**：演示、测试和学习
- **特点**：
  - 不依赖实际的IM SDK
  - 不会实际发送或接收消息
  - 返回模拟数据
  - 易于运行，无需配置
- **适用场景**：
  - 快速测试MCP Inspector连接
  - 在没有实际IM SDK的环境中开发测试
  - 学习MCP协议的基本用法

### 2. 实际实现 (`src/server/mcp_im_server.py`)

- **用途**：生产环境使用
- **特点**：
  - 调用实际的IM SDK
  - 实际发送和接收消息
  - 需要正确配置IM SDK
  - 提供完整的错误处理和日志记录
- **适用场景**：
  - 生产环境部署
  - 集成到实际应用中
  - 进行真实通信测试

## 接口对比

两种实现提供了一致的接口名称和参数，但实际行为不同：

| 接口名称 | 模拟服务器 | 实际实现 |
|---------|------------|---------|
| `init` | 返回模拟数据 | 初始化真实IM SDK |
| `connect` | 模拟连接成功 | 连接到真实IM服务 |
| `sendMessage` | 返回模拟消息ID | 实际发送消息 |
| `getHistoryMessages` | 返回模拟消息列表 | 查询真实历史消息 |

## 快速开始

### 运行模拟服务器

```bash
python examples/server/mock_mcp_server.py
```

### 使用MCP Inspector连接

1. 安装MCP Inspector:
```bash
npx @modelcontextprotocol/inspector
```

2. 连接到服务器:
```
http://localhost:8000/sse
```

3. 尝试调用工具:
   - `init`: 初始化IM引擎
   - `connect`: 连接到IM服务
   - `sendMessage`: 发送消息
   - `getHistoryMessages`: 获取历史消息 