"""
Research.py
===========
Research / Academic tools from Agno, each as an independent @tool.
Neither requires an API key.

pip install agno arxiv biopython
"""

from agno.tools import tool


@tool
def arxiv_search(query: str, num_results: int = 5) -> str:
    """Search academic papers on ArXiv.

    Args:
        query (str): The search query, e.g. "transformer attention mechanism".
        num_results (int): Number of results to return. Defaults to 5.
    """
    from agno.tools.arxiv import ArxivTools
    return ArxivTools().search_arxiv_and_return_articles(query, num_articles=num_results)


@tool
def pubmed_search(query: str, num_results: int = 5) -> str:
    """Search medical/biomedical literature on PubMed.

    Args:
        query (str): The search query, e.g. "CRISPR gene editing".
        num_results (int): Number of results to return. Defaults to 5.
    """
    from agno.tools.pubmed import PubmedTools
    return PubmedTools().search_pubmed(query, max_results=num_results)
