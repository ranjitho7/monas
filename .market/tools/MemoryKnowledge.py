"""
MemoryKnowledge.py
==================
Memory / Knowledge tools from Agno, each as an independent @tool.

pip install agno mem0ai zep-cloud
"""

import os
from agno.tools import tool


@tool
def mem0_add_memory(user_id: str, content: str) -> str:
    """Store a memory for a user using Mem0.

    Args:
        user_id (str): Unique identifier for the user.
        content (str): The memory content to store.
    """
    os.environ["MEM0_API_KEY"] = "YOUR_MEM0_API_KEY"
    from agno.tools.mem0 import Mem0Tools
    return Mem0Tools().add_memory(user_id=user_id, content=content)


@tool
def mem0_search_memory(user_id: str, query: str) -> str:
    """Search a user's stored memories using Mem0.

    Args:
        user_id (str): Unique identifier for the user.
        query (str): The search query.
    """
    os.environ["MEM0_API_KEY"] = "YOUR_MEM0_API_KEY"
    from agno.tools.mem0 import Mem0Tools
    return Mem0Tools().search_memory(user_id=user_id, query=query)


@tool
def zep_add_memory(session_id: str, content: str) -> str:
    """Store a memory in a Zep session.

    Args:
        session_id (str): The Zep session identifier.
        content (str): The memory content to store.
    """
    os.environ["ZEP_API_KEY"] = "YOUR_ZEP_API_KEY"
    from agno.tools.zep import ZepTools
    return ZepTools().add_memory(session_id=session_id, content=content)


@tool
def knowledge_search(query: str) -> str:
    """Search the agent's connected knowledge base.

    Args:
        query (str): The search query.
    """
    from agno.tools.knowledge import KnowledgeTools
    return KnowledgeTools().search(query)
