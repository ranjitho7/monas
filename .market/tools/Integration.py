"""
Integration.py
==============
Integration Platform tools from Agno, each as an independent @tool.

pip install agno composio-core mcp
"""

import os
from agno.tools import tool


@tool
def composio_run_action(action_name: str, params: dict) -> str:
    """Run a Composio action (integrates with 100+ third-party apps).

    Args:
        action_name (str): The Composio action name, e.g. "GITHUB_CREATE_ISSUE".
        params (dict): Parameters required by the action.
    """
    os.environ["COMPOSIO_API_KEY"] = "YOUR_COMPOSIO_API_KEY"
    from agno.tools.composio import ComposioTools
    return ComposioTools().run_action(action_name, params)


@tool
def mcp_call_tool(server_url: str, tool_name: str, params: dict) -> str:
    """Call a tool exposed by an MCP (Model Context Protocol) server.

    Args:
        server_url (str): The MCP server's URL.
        tool_name (str): Name of the tool to call on the MCP server.
        params (dict): Parameters to pass to the tool.
    """
    from agno.tools.mcp import MCPTools
    return MCPTools(url=server_url).call_tool(tool_name, params)
