"""
IM MCP客户端

用于连接IM MCP服务器的客户端

支持通过HTTP或stdio与MCP服务器通信
"""
import asyncio
import logging
import json
import uuid
import time
import subprocess
import sys
import os
import aiohttp
from typing import Dict, Any, List, Optional, Callable

# 导入MCP客户端
try:
    from mcp import ClientSession
    # 注意：最新版本的mcp库可能没有直接导出HTTPTransport，需要确认正确的导入路径
    try:
        from mcp.transport import HTTPTransport
    except ImportError:
        # 如果HTTPTransport不在transport模块中，可能在其他地方
        try:
            from mcp import HTTPTransport
        except ImportError:
            # 如果无法直接导入，则自行实现HTTP通信
            HTTPTransport = None
    
    HAS_MCP_CLIENT = True
except ImportError:
    HAS_MCP_CLIENT = False
    print("警告：未安装MCP客户端库，将使用HTTP API直接通信")

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("mcp_im_client")

class IMClient:
    """
    IM客户端，封装与IM服务器的通信
    """
    
    def __init__(self, server_url: str = "http://127.0.0.1:8000", use_stdio: bool = True):
        """
        初始化IM客户端
        
        Args:
            server_url: MCP服务器的URL地址（HTTP模式）
            use_stdio: 是否使用stdio与服务器通信，如果为True，则忽略server_url
        """
        self.server_url = server_url
        self.use_stdio = use_stdio
        self.client_id = str(uuid.uuid4())  # 生成唯一客户端ID
        self.message_callback = None  # 消息回调函数
        self.server_process = None  # 服务器进程（仅stdio模式）
        
        # 初始化MCP客户端
        self.mcp_client = None  # 在第一次需要时创建
        self.http_session = None  # HTTP会话（仅在直接HTTP模式下使用）
        self.http_mode = False  # 是否使用直接HTTP模式（不使用MCP客户端库）
        
        if use_stdio:
            logger.info(f"已初始化IM客户端，使用stdio模式与服务器通信，客户端ID: {self.client_id}")
        else:
            logger.info(f"已初始化IM客户端，连接到服务器: {server_url}, 客户端ID: {self.client_id}")
    
    async def _ensure_client(self):
        """确保MCP客户端已初始化"""
        if self.mcp_client is None and self.http_session is None:
            try:
                if not HAS_MCP_CLIENT:
                    # 如果没有MCP客户端库，使用直接HTTP模式
                    self.http_session = aiohttp.ClientSession()
                    self.http_mode = True
                    logger.info(f"已初始化HTTP会话，连接到服务器: {self.server_url}")
                    return True
                
                if self.use_stdio:
                    # 启动服务器进程
                    if self.server_process is None:
                        # 默认服务器路径
                        current_dir = os.path.dirname(os.path.abspath(__file__))
                        project_root = os.path.abspath(os.path.join(current_dir, "../.."))
                        server_path = os.path.join(project_root, "src/server/mcp_im_server.py")
                        
                        # 使用Python解释器启动服务器脚本，指定stdio模式
                        self.server_process = subprocess.Popen(
                            [sys.executable, server_path, "--transport", "stdio"],
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            text=True,
                            bufsize=1
                        )
                        logger.info(f"已启动服务器进程，使用stdio模式")
                    
                    # 创建基于标准输入/输出的ClientSession
                    # 尝试多种可能的初始化方式
                    try:
                        # 方式1：通过stdio工厂方法
                        if hasattr(ClientSession, 'stdio'):
                            self.mcp_client = ClientSession.stdio(
                                self.server_process.stdin,
                                self.server_process.stdout
                            )
                        # 方式2：直接传递stdin/stdout给构造函数
                        else:
                            self.mcp_client = ClientSession(
                                stdin=self.server_process.stdin,
                                stdout=self.server_process.stdout
                            )
                    except Exception as e:
                        logger.error(f"创建stdio模式MCP客户端失败: {e}")
                        # 如果创建失败，回退到直接HTTP模式
                        self.http_session = aiohttp.ClientSession()
                        self.http_mode = True
                    
                    logger.info("已初始化MCP客户端，使用stdio与服务器通信")
                else:
                    # 使用HTTP模式
                    # 创建HTTP客户端会话
                    # 由于不同版本的MCP库API可能有差异，我们使用异常处理来适应不同版本
                    try:
                        # 最新版本可能直接支持URL初始化
                        self.mcp_client = ClientSession(self.server_url)
                        logger.info(f"已初始化MCP客户端(直接URL初始化)，连接到服务器: {self.server_url}")
                    except Exception as e:
                        # 如果直接使用URL初始化失败，尝试其他方法
                        logger.warning(f"直接URL初始化MCP客户端失败: {e}")
                        
                        try:
                            # 尝试使用HTTPTransport
                            if HTTPTransport is not None:
                                transport = HTTPTransport(self.server_url)
                                self.mcp_client = ClientSession(transport)
                                logger.info(f"已初始化MCP客户端(使用HTTPTransport)，连接到服务器: {self.server_url}")
                            else:
                                # 尝试使用ClientSession的http工厂方法，如果存在
                                if hasattr(ClientSession, 'http'):
                                    self.mcp_client = ClientSession.http(self.server_url)
                                    logger.info(f"已初始化MCP客户端(使用http工厂方法)，连接到服务器: {self.server_url}")
                                else:
                                    # 如果所有方法都失败，回退到直接HTTP模式
                                    logger.warning("无法初始化MCP客户端，回退到直接HTTP模式")
                                    self.http_session = aiohttp.ClientSession()
                                    self.http_mode = True
                                    logger.info(f"已初始化HTTP会话，连接到服务器: {self.server_url}")
                        except Exception as e2:
                            logger.error(f"所有MCP客户端初始化方法都失败: {e2}")
                            # 回退到直接HTTP模式
                            self.http_session = aiohttp.ClientSession()
                            self.http_mode = True
                            logger.info(f"已初始化HTTP会话，连接到服务器: {self.server_url}")
                
                return True
            except Exception as e:
                logger.error(f"初始化客户端失败: {e}")
                self.mcp_client = None  # 重置客户端
                
                # 清理HTTP会话
                if self.http_session:
                    try:
                        await self.http_session.close()
                    except:
                        pass
                    self.http_session = None
                
                # 如果是stdio模式且服务器进程存在，尝试关闭它
                if self.use_stdio and self.server_process:
                    try:
                        self.server_process.terminate()
                        self.server_process.wait(timeout=5)
                    except Exception as e:
                        logger.error(f"关闭服务器进程失败: {e}")
                        # 强制关闭
                        try:
                            self.server_process.kill()
                        except:
                            pass
                    finally:
                        self.server_process = None
                
                return False
        return True
    
    async def call_tool(self, tool_name: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        调用MCP服务器上的工具
        
        Args:
            tool_name: 工具名称
            params: 调用参数
            
        Returns:
            调用结果
        """
        logger.info(f"调用MCP工具: {tool_name}, 参数: {params}")
        
        # 确保MCP客户端已初始化
        client_ok = await self._ensure_client()
        
        if not client_ok:
            return {
                "success": False,
                "error": "无法初始化客户端"
            }
        
        try:
            if self.http_mode:
                # 使用直接HTTP调用
                # MCP API端点有两种可能格式: /call/{tool_name} 或 /api/_mcp_/v1/tools/{tool_name}
                tool_url = f"{self.server_url}/api/_mcp_/v1/tools/{tool_name}"
                
                # 尝试调用MCP API
                try:
                    async with self.http_session.post(tool_url, json=params) as response:
                        if response.status == 200:
                            result = await response.json()
                            logger.info(f"成功调用工具 {tool_name}")
                        else:
                            # 如果标准MCP路径失败，尝试替代路径
                            alt_url = f"{self.server_url}/call/{tool_name}"
                            logger.warning(f"使用标准MCP API路径失败，状态码: {response.status}，尝试替代路径: {alt_url}")
                            
                            async with self.http_session.post(alt_url, json=params) as alt_response:
                                if alt_response.status == 200:
                                    result = await alt_response.json()
                                    logger.info(f"使用替代路径成功调用工具 {tool_name}")
                                else:
                                    error_text = await alt_response.text()
                                    logger.error(f"所有路径均调用失败，状态码: {alt_response.status}, 错误: {error_text}")
                                    result = {
                                        "success": False,
                                        "error": f"HTTP错误: {alt_response.status} - {error_text}"
                                    }
                except Exception as http_error:
                    logger.error(f"HTTP请求过程中出错: {http_error}")
                    result = {
                        "success": False,
                        "error": f"HTTP请求错误: {http_error}"
                    }
            else:
                # 使用MCP客户端调用工具
                result = await self.mcp_client.call_tool(tool_name, params)
                logger.info(f"成功调用工具 {tool_name}")
            
            # 确保返回结果是一个字典并包含success字段
            if isinstance(result, dict):
                if "success" not in result:
                    result["success"] = True
            else:
                # 如果返回结果不是字典，封装成字典
                result = {
                    "success": True,
                    "result": result
                }
                
            return result
        except Exception as e:
            logger.error(f"调用工具失败: {e}")
            return {
                "success": False,
                "error": f"调用工具失败: {e}"
            }
    
    async def register_message_listener(self, callback: Callable) -> Dict[str, Any]:
        """
        注册消息监听器并开始接收消息通知
        
        Args:
            callback: 收到新消息时的回调函数，参数为消息对象
        
        Returns:
            注册结果
        """
        logger.info("注册消息监听器并开始接收消息通知")
        
        # 检查是否已经有回调
        if self.message_callback:
            logger.warning("消息通知已经在运行中，将更新回调函数")
        
        try:
            # 确保MCP客户端已初始化
            client_ok = await self._ensure_client()
            
            if not client_ok:
                return {
                    "success": False,
                    "error": "无法初始化MCP客户端"
                }
            
            # 保存回调函数
            self.message_callback = callback
            
            # 调用服务端注册函数
            result = await self.call_tool("registerMessageListener", {
                "client_id": self.client_id
            })
            
            if not result.get("success", False):
                logger.error(f"消息监听器注册失败: {result}")
                self.message_callback = None  # 注册失败时清除回调
                return result
                
            logger.info(f"消息监听器注册结果: {result}")
            
            # 如果使用HTTP模式，注册客户端回调
            if not self.use_stdio:
                # 在HTTP模式下，我们需要使用消息轮询或SSE
                await self._start_message_polling()
            
            logger.info("消息通知监听已启动")
            
            return {
                "success": True,
                "message": "消息监听器注册成功并开始接收通知"
            }
        except Exception as e:
            logger.error(f"注册消息监听器失败: {e}")
            self.message_callback = None  # 出错时清除回调
            return {
                "success": False,
                "error": str(e)
            }
    
    async def _start_message_polling(self):
        """开始轮询消息（HTTP模式下使用）"""
        async def polling_task():
            try:
                while self.message_callback:
                    try:
                        # 调用服务端获取消息
                        messages = await self.call_tool("pullMessages", {
                            "client_id": self.client_id,
                            "max_count": 20
                        })
                        
                        if messages.get("success", False) and messages.get("messages"):
                            # 处理每条消息
                            for message in messages.get("messages", []):
                                try:
                                    await self.message_callback(message)
                                except Exception as e:
                                    logger.error(f"执行消息回调时出错: {e}")
                    except Exception as e:
                        logger.error(f"轮询消息时出错: {e}")
                    
                    # 等待一段时间再次轮询
                    await asyncio.sleep(1)
            except asyncio.CancelledError:
                logger.info("消息轮询已取消")
            except Exception as e:
                logger.error(f"消息轮询任务出错: {e}")
        
        # 创建并启动轮询任务
        self.polling_task = asyncio.create_task(polling_task())
        logger.info("已启动消息轮询任务")
    
    async def unregister_message_listener(self) -> Dict[str, Any]:
        """
        注销消息监听器并停止接收消息通知
        
        Returns:
            注销结果
        """
        logger.info("注销消息监听器并停止接收消息通知")
        
        if self.message_callback is None:
            return {
                "success": True,
                "message": "没有正在运行的消息监听"
            }
        
        # 清除回调函数
        self.message_callback = None
        
        # 如果有轮询任务，取消它
        if hasattr(self, 'polling_task') and self.polling_task and not self.polling_task.done():
            self.polling_task.cancel()
            try:
                await self.polling_task
            except asyncio.CancelledError:
                pass
            self.polling_task = None
            logger.info("已停止消息轮询")
        
        # 调用服务端注销函数
        try:
            result = await self.call_tool("unregisterMessageListener", {
                "client_id": self.client_id
            })
            
            logger.info(f"消息监听器注销结果: {result}")
            return result
        except Exception as e:
            logger.error(f"注销消息监听器失败: {e}")
            return {
                "success": False,
                "error": f"注销消息监听器失败: {e}"
            }
    
    async def close(self) -> None:
        """关闭客户端连接和资源"""
        await self.unregister_message_listener()
        
        # 关闭MCP客户端
        if self.mcp_client:
            try:
                await self.mcp_client.aclose()
            except Exception as e:
                logger.error(f"关闭MCP客户端时出错: {e}")
        
        # 如果在stdio模式下有服务器进程，关闭它
        if self.use_stdio and self.server_process:
            try:
                self.server_process.terminate()
                self.server_process.wait(timeout=5)
            except Exception as e:
                logger.error(f"关闭服务器进程失败: {e}")
                # 强制关闭
                try:
                    self.server_process.kill()
                except:
                    pass
            finally:
                self.server_process = None
        
        logger.info("IM客户端资源已关闭")
    
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
            result = await self.call_tool("sendMessage", {
                "receiver": receiver,
                "content": content,
                "conversation_type": 1  # 默认为单聊
            })
            logger.info(f"消息发送成功: {result}")
            return result
        except Exception as e:
            logger.error(f"发送消息失败: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    async def get_history_messages(self, user_id: str, count: int = 10) -> Dict[str, Any]:
        """
        获取与指定用户的历史消息
        
        Args:
            user_id: 用户ID，获取与该用户的历史消息
            count: 要获取的消息数量，默认为10条
            
        Returns:
            包含历史消息列表的字典
        """
        logger.info(f"正在获取与用户 {user_id} 的 {count} 条历史消息")
        try:
            result = await self.call_tool("getHistoryMessages", {
                "user_id": user_id,
                "count": count
            })
            
            # 确保返回结果是正确的格式
            if isinstance(result, list):
                return {
                    "success": True,
                    "messages": result
                }
            elif isinstance(result, dict) and "messages" in result:
                return result
            else:
                return {
                    "success": True,
                    "messages": result
                }
        except Exception as e:
            logger.error(f"获取历史消息失败: {e}")
            return {
                "success": False,
                "error": str(e),
                "messages": []
            }

    async def initAndConnect(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        初始化并连接IM客户端
        
        Args:
            params: 包含初始化和连接参数，需包含:
                   - app_key: 应用标识
                   - device_id: 设备ID
                   - token: 连接令牌
                   - timeout_sec: 连接超时时间（可选）
            
        Returns:
            包含连接结果的字典
        """
        logger.info("开始初始化和连接IM客户端")
        
        try:
            # 确保MCP客户端已初始化
            client_ok = await self._ensure_client()
            
            if not client_ok:
                return {
                    "success": False,
                    "error": "无法初始化MCP客户端",
                    "init_success": False,
                    "connect_success": False
                }
            
            # 直接调用服务器端的initAndConnect工具
            init_connect_result = await self.call_tool("initAndConnect", {
                "app_key": params.get("app_key", ""),
                "device_id": params.get("device_id", f"device_{self.client_id}"),
                "token": params.get("token", ""),
                "timeout_sec": params.get("timeout_sec", 30)
            })
            
            logger.info(f"初始化和连接结果: {init_connect_result}")
            
            # 确保返回值包含初始化和连接标志
            if "init_success" not in init_connect_result:
                init_connect_result["init_success"] = init_connect_result.get("success", False)
                
            if "connect_success" not in init_connect_result:
                init_connect_result["connect_success"] = init_connect_result.get("success", False)
            
            return init_connect_result
        except Exception as e:
            error_msg = f"初始化和连接过程中发生异常: {e}"
            logger.error(error_msg)
            return {
                "success": False,
                "error": error_msg,
                "init_success": False,
                "connect_success": False
            }

async def demo():
    """演示使用IM客户端的示例"""
    

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="运行IM MCP客户端演示")
    parser.add_argument("--server", default="http://127.0.0.1:8000", help="MCP服务器的URL地址")
    
    args = parser.parse_args()
    
    asyncio.run(demo()) 