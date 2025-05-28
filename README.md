# Rongcloud Native MCP

基于 MCP 协议的融云 IM 服务（包装 Rust SDK）

[English Documentation](README_EN.md)

## 使用方法

### 前提--安装 UV 包管理工具

```bash
 pip install uv 
```

UV 是一个用 Rust 编写的 Python 包安装和依赖管理工具，比传统工具（如 pip）有着更快、更高效的体验。它主要关注两个核心目标：

速度: UV 在包安装、依赖解析和虚拟环境创建等方面进行了优化，速度有显著的提升。
效率: UV 可以减少资源消耗，尤其是在大型项目中。

后续我们会用到 UVX 命令，它的作用是"如果本地没有，先下载。再运行"，而且每次都是在单独的虚拟环境中，很适合大模型/Agent相关场景

### 在 Cursor 中使用（Cline / Claude 类似）

配置路径：Cursor -> 首选项 -> Cursor Settings -> MCP -> Add new global MCP server
配置内容：

```json
{
  "mcpServers": {
    "rc_im_native_mcp": {
      "name": "rongcloud-native-mcp-python",
      "type": "stdio",
      "command": "uvx",
      "args": [
        "rongcloud-native-mcp-python"
      ],
      "env": {
          "APP_KEY": "Your Rongcloud App Key",
          "TOKEN": "Your Rongcloud SDK Token (from Server API)",
          "NAVI_HOST": "Your Rongcloud SDK Nav URL"
      }
    }
  }
}

```

### 在 Cherry studio 中使用

先安装 UV 和 Bun（都需要安装），安装后重启 Cherry Studio。然后按照下图配置：
![Cherry Studio 界面示例](readme_img/cherry-studio-0.png)
![Cherry Studio 界面示例](readme_img/cherry-studio.png)

## 主要功能与工具（tools）说明（持续更新）

服务端通过 MCP 协议暴露以下工具：

### 1. `init_and_connect`

- **功能**：初始化 IM 引擎并连接到 IM 服务器
- **参数**：
  - `timeout_sec` (int, 默认30)：连接超时时间（秒）
- **返回**：
  - `code` (int)：0 表示成功，非0为失败
  - `message` (str)：结果说明
  - `init_success` (bool)：初始化是否成功
  - `connect_success` (bool)：连接是否成功

### 2. `send_message`

- **功能**：发送 IM 消息给指定用户（支持单聊/群聊）
- **参数**：
  - `receiver` (str)：消息接收者ID
  - `content` (str)：消息内容
  - `conversation_type` (int, 默认1)：会话类型，1=单聊，2=群聊
- **返回**：
  - 失败：`code`、`message`
  - 成功：`code`、`message_id`、`message`

### 3. `get_history_messages`

- **功能**：获取与指定用户的历史消息
- **参数**：
  - `user_id` (str)：用户ID
  - `count` (int, 默认10)：获取的消息数量
- **返回**：
  - 失败：`code`、`message`
  - 成功：`code`、`messages`（消息数组）

### 4. `disconnect`

- **功能**：断开与 IM 服务器的连接
- **参数**：无
- **返回**：
  - `code` (int)：0 表示成功，非0为失败
  - `message` (str)：结果说明

## 常见问题

### Q: 为什么配置了 Cursor 但是服务器列表中一直是黄色小圆点？

A: 服务器列表中显示黄色小圆点，尝试先安装 UV 命令，重启 Cursor 后重新开启服务开关。

### Q: 为什么 Cherry Studio 一直报错？

A: 确保 UV 和 Bun 安装成功，重启 Cherry Studio 后重新开启服务开关。

### Q: 为什么调用工具后返回错误？

A: 确保环境变量（APP_KEY、TOKEN、NAVI_HOST）正确设置，重启服务后重新调用工具。

## 技术支持

如果遇到问题，请：

1. 检查环境变量是否正确设置
2. 查看日志输出，了解具体错误信息
3. 在开源项目中提issue
