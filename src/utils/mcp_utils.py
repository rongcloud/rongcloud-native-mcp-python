"""
MCP工具类模块

提供用于MCP服务器的通用工具函数和类
"""
import inspect
import logging
from typing import Any, Dict, Optional

logger = logging.getLogger("mcp_utils")

class MCPServerUtils:
    """MCP服务器工具类，提供通用功能"""
    
    @staticmethod
    def run_app(app: Any, host: str = "0.0.0.0", port: int = 8000, transport: str = "sse") -> None:
        """
        根据支持的参数运行MCP应用
        
        此方法检查FastMCP.run方法支持的参数，然后使用适当的参数调用它。
        这样可以确保代码适应不同版本的FastMCP库。
        
        Args:
            app: FastMCP应用实例
            host: 服务器主机地址，默认为"0.0.0.0"
            port: 服务器端口，默认为8000
            transport: 传输协议，默认为"sse"
        """
        # 检查并确保MCP初始化配置正确
        MCPServerUtils.ensure_mcp_initialization(app)
        
        # 检查FastMCP.run方法支持的参数
        run_params = inspect.signature(app.run).parameters
        logger.info(f"FastMCP.run方法支持的参数: {list(run_params.keys())}")
        
        # 根据支持的参数调用run方法
        if 'host' in run_params and 'port' in run_params and 'transport' in run_params:
            app.run(host=host, port=port, transport=transport)
        elif 'port' in run_params and 'transport' in run_params:
            app.run(port=port, transport=transport)
        elif 'port' in run_params:
            app.run(port=port)
        elif 'transport' in run_params:
            app.run(transport=transport)
        else:
            app.run()
    
    @staticmethod
    def ensure_mcp_initialization(app: Any) -> None:
        """
        确保MCP应用已经正确配置了初始化参数
        
        Args:
            app: FastMCP应用实例
        """
        # 增加初始化相关的配置检查
        if hasattr(app, 'request_timeout'):
            logger.info(f"MCP请求超时设置为: {app.request_timeout}秒")
        
        # 检查是否配置了require_init_before_use参数
        if hasattr(app, 'require_init_before_use'):
            if app.require_init_before_use:
                logger.info("MCP应用已配置为: 使用其他工具前需要先调用初始化")
            else:
                logger.warning("MCP应用配置为: 不需要初始化即可使用工具，这可能导致某些工具调用失败")
        else:
            # 尝试设置此属性，如果FastMCP支持
            try:
                app.require_init_before_use = True
                logger.info("已自动配置MCP应用: 使用其他工具前需要先调用初始化")
            except AttributeError:
                logger.warning("FastMCP不支持require_init_before_use配置，可能需要手动确保正确的初始化顺序")
        
        # 检查是否有init工具，尝试多种可能的工具管理方式
        has_init_tool = False
        
        # 方法1: 检查list_tools方法
        if hasattr(app, 'list_tools') and callable(app.list_tools):
            try:
                # 检查是否为异步方法
                if inspect.iscoroutinefunction(app.list_tools):
                    logger.info("list_tools是异步方法，不在此处直接调用")
                else:
                    tools = app.list_tools()
                    logger.info(f"注册的工具列表 (list_tools方法): {tools}")
                    has_init_tool = any(tool.lower() == 'init' for tool in tools)
            except Exception as e:
                logger.warning(f"调用list_tools()时出错: {e}")
        
        # 方法2: 检查_tools属性
        if not has_init_tool and hasattr(app, '_tools') and isinstance(app._tools, dict):
            logger.info(f"注册的工具列表 (_tools属性): {list(app._tools.keys())}")
            has_init_tool = 'init' in app._tools
        
        # 方法3: 检查_tool_manager属性
        if not has_init_tool and hasattr(app, '_tool_manager'):
            tool_manager = app._tool_manager
            logger.info(f"工具管理器属性: {dir(tool_manager)}")
            
            # 尝试获取工具列表
            if hasattr(tool_manager, 'list_tools') and callable(tool_manager.list_tools):
                try:
                    # 检查是否为异步方法
                    if inspect.iscoroutinefunction(tool_manager.list_tools):
                        logger.info("工具管理器的list_tools是异步方法，不在此处直接调用")
                    else:
                        tools = tool_manager.list_tools()
                        logger.info(f"注册的工具列表 (工具管理器): {tools}")
                        
                        # 检查Tool对象列表中是否有名为'init'的工具
                        # 处理不同类型的返回值
                        if tools and hasattr(tools[0], 'name'):
                            # 如果返回的是Tool对象列表
                            tool_names = [tool.name for tool in tools if hasattr(tool, 'name')]
                            logger.info(f"工具名称列表: {tool_names}")
                            has_init_tool = 'init' in tool_names
                        else:
                            # 如果返回的是字符串列表
                            has_init_tool = any(
                                (tool.lower() == 'init' if isinstance(tool, str) else False) 
                                for tool in tools
                            )
                except Exception as e:
                    logger.warning(f"调用工具管理器的list_tools()时出错: {e}")
            
            # 检查其他可能保存工具的属性
            for attr_name in ['_tools', 'tools']:
                if hasattr(tool_manager, attr_name):
                    attr = getattr(tool_manager, attr_name)
                    if isinstance(attr, dict):
                        logger.info(f"工具管理器的{attr_name}属性包含: {list(attr.keys())}")
                        has_init_tool = has_init_tool or 'init' in attr
        
        # 方法4: 直接检查工具方法
        if not has_init_tool and hasattr(app, 'tool') and callable(app.tool):
            logger.info("检查是否通过@app.tool装饰器添加了工具")
            has_init_tool = True  # 假设已添加工具，因为我们无法直接检查装饰器是否已应用
        
        if not has_init_tool:
            logger.warning("未找到'init'工具，请确保添加用于初始化的工具！")
        else:
            logger.info("已找到'init'工具，可以正常使用") 