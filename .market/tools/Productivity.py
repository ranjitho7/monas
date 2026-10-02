"""
Productivity.py
===============
Productivity / Project Management tools from Agno, each as an independent @tool.

pip install agno notion-client jira atlassian-python-api PyGithub
"""

import os
from agno.tools import tool


@tool
def notion_search(query: str) -> str:
    """Search pages and databases in Notion.

    Args:
        query (str): The search query.
    """
    os.environ["NOTION_API_KEY"] = "YOUR_NOTION_API_KEY"
    from agno.tools.notion import NotionTools
    return NotionTools().search(query)


@tool
def jira_search_issues(jql_query: str) -> str:
    """Search Jira issues using JQL.

    Args:
        jql_query (str): A Jira Query Language string, e.g. "project = ENG AND status = Open".
    """
    os.environ["JIRA_SERVER_URL"] = "YOUR_JIRA_SERVER_URL"
    os.environ["JIRA_USERNAME"] = "YOUR_JIRA_USERNAME"
    os.environ["JIRA_API_TOKEN"] = "YOUR_JIRA_API_TOKEN"
    from agno.tools.jira import JiraTools
    return JiraTools().search_issues(jql_query)


@tool
def linear_search_issues(query: str) -> str:
    """Search issues in Linear.

    Args:
        query (str): The search query.
    """
    os.environ["LINEAR_API_KEY"] = "YOUR_LINEAR_API_KEY"
    from agno.tools.linear import LinearTools
    return LinearTools().search_issues(query)


@tool
def clickup_get_tasks(list_id: str) -> str:
    """Get tasks from a ClickUp list.

    Args:
        list_id (str): The ClickUp list ID.
    """
    os.environ["CLICKUP_API_KEY"] = "YOUR_CLICKUP_API_KEY"
    from agno.tools.clickup_tool import ClickUpTools
    return ClickUpTools().get_tasks(list_id)


@tool
def trello_get_boards() -> str:
    """List all Trello boards for the authenticated user."""
    os.environ["TRELLO_API_KEY"] = "YOUR_TRELLO_API_KEY"
    os.environ["TRELLO_API_TOKEN"] = "YOUR_TRELLO_API_TOKEN"
    from agno.tools.trello import TrelloTools
    return TrelloTools().list_boards()


@tool
def todoist_get_tasks() -> str:
    """Get all active tasks from Todoist."""
    os.environ["TODOIST_API_TOKEN"] = "YOUR_TODOIST_API_TOKEN"
    from agno.tools.todoist import TodoistTools
    return TodoistTools().get_active_tasks()


@tool
def confluence_search(query: str) -> str:
    """Search pages in Confluence.

    Args:
        query (str): The search query.
    """
    os.environ["CONFLUENCE_URL"] = "YOUR_CONFLUENCE_URL"
    os.environ["CONFLUENCE_USERNAME"] = "YOUR_CONFLUENCE_USERNAME"
    os.environ["CONFLUENCE_API_TOKEN"] = "YOUR_CONFLUENCE_API_TOKEN"
    from agno.tools.confluence import ConfluenceTools
    return ConfluenceTools().search_page(query)


@tool
def bitbucket_list_repos(workspace: str) -> str:
    """List repositories in a Bitbucket workspace.

    Args:
        workspace (str): The Bitbucket workspace name.
    """
    os.environ["BITBUCKET_USERNAME"] = "YOUR_BITBUCKET_USERNAME"
    os.environ["BITBUCKET_APP_PASSWORD"] = "YOUR_BITBUCKET_APP_PASSWORD"
    from agno.tools.bitbucket import BitbucketTools
    return BitbucketTools().list_repositories(workspace)


@tool
def github_search_repos(query: str) -> str:
    """Search GitHub repositories.

    Args:
        query (str): The search query, e.g. "agno framework".
    """
    os.environ["GITHUB_ACCESS_TOKEN"] = "YOUR_GITHUB_ACCESS_TOKEN"
    from agno.tools.github import GithubTools
    return GithubTools().search_repositories(query)
