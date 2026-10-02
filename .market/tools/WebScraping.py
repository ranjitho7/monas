"""
WebScraping.py
==============
Web Scraping / Automation tools from Agno, each as an independent @tool.
Required API keys are set inside each function. Replace placeholders.

pip install agno firecrawl-py crawl4ai agentql scrapegraph-py trafilatura
pip install newspaper4k lxml_html_clean requests apify-client docling
"""

import os
from agno.tools import tool


@tool
def firecrawl_scrape(url: str) -> str:
    """Scrape a webpage's content using Firecrawl.

    Args:
        url (str): The URL to scrape.
    """
    os.environ["FIRECRAWL_API_KEY"] = "YOUR_FIRECRAWL_API_KEY"
    from agno.tools.firecrawl import FirecrawlTools
    return FirecrawlTools(scrape=True).scrape_website(url)


@tool
def crawl4ai_scrape(url: str) -> str:
    """Crawl and extract a webpage's content using Crawl4AI.

    Args:
        url (str): The URL to crawl.
    """
    from agno.tools.crawl4ai import Crawl4aiTools
    return Crawl4aiTools().web_crawler(url)


@tool
def agentql_scrape(url: str, query: str) -> str:
    """Extract structured data from a webpage using AgentQL.

    Args:
        url (str): The URL to scrape.
        query (str): AgentQL query describing what data to extract.
    """
    os.environ["AGENTQL_API_KEY"] = "YOUR_AGENTQL_API_KEY"
    from agno.tools.agentql import AgentQLTools
    return AgentQLTools().scrape_website(url, query)


@tool
def scrapegraph_markdownify(url: str) -> str:
    """Convert a webpage into clean Markdown using ScrapeGraph.

    Args:
        url (str): The URL to convert.
    """
    os.environ["SGAI_API_KEY"] = "YOUR_SCRAPEGRAPH_API_KEY"
    from agno.tools.scrapegraph import ScrapeGraphTools
    return ScrapeGraphTools(markdownify=True).markdownify(url)


@tool
def trafilatura_extract(url: str) -> str:
    """Extract the main article text from a webpage using Trafilatura.

    Args:
        url (str): The page URL.
    """
    from agno.tools.trafilatura import TrafilaturaTools
    return TrafilaturaTools().extract_article(url)


@tool
def newspaper4k_extract(url: str) -> str:
    """Extract a news article's title, text, and metadata.

    Args:
        url (str): The article URL.
    """
    from agno.tools.newspaper4k import Newspaper4kTools
    return Newspaper4kTools().get_article_text(url)


@tool
def website_read(url: str) -> str:
    """Read and return the content of a website.

    Args:
        url (str): The website URL.
    """
    from agno.tools.website import WebsiteTools
    return WebsiteTools().read_url(url)


@tool
def webbrowser_open(url: str) -> str:
    """Open a URL in a browser and return the rendered content.

    Args:
        url (str): The URL to open.
    """
    from agno.tools.webbrowser import WebBrowserTools
    return WebBrowserTools().open_page(url)


@tool
def jina_reader_read(url: str) -> str:
    """Read a URL and return clean Markdown content using Jina Reader.

    Args:
        url (str): The URL to read.
    """
    os.environ["JINA_API_KEY"] = "YOUR_JINA_API_KEY"
    from agno.tools.jina import JinaReaderTools
    return JinaReaderTools().read_url(url)


@tool
def spider_crawl(url: str) -> str:
    """Crawl a website using Spider.

    Args:
        url (str): The URL to crawl.
    """
    os.environ["SPIDER_API_KEY"] = "YOUR_SPIDER_API_KEY"
    from agno.tools.spider import SpiderTools
    return SpiderTools().crawl(url)


@tool
def oxylabs_scrape(url: str) -> str:
    """Scrape a webpage using Oxylabs' scraping API (handles proxies/anti-bot).

    Args:
        url (str): The URL to scrape.
    """
    os.environ["OXYLABS_USERNAME"] = "YOUR_OXYLABS_USERNAME"
    os.environ["OXYLABS_PASSWORD"] = "YOUR_OXYLABS_PASSWORD"
    from agno.tools.oxylabs import OxylabsTools
    return OxylabsTools().scrape_url(url)


@tool
def brightdata_scrape(url: str) -> str:
    """Scrape a webpage using Bright Data's Web Unlocker.

    Args:
        url (str): The URL to scrape.
    """
    os.environ["BRIGHTDATA_API_KEY"] = "YOUR_BRIGHTDATA_API_KEY"
    from agno.tools.brightdata import BrightDataTools
    return BrightDataTools().scrape_url(url)


@tool
def apify_run_actor(actor_id: str, run_input: dict) -> str:
    """Run an Apify actor to scrape or automate a task.

    Args:
        actor_id (str): The Apify actor ID (e.g. "apify/website-content-crawler").
        run_input (dict): Input parameters for the actor.
    """
    os.environ["APIFY_API_TOKEN"] = "YOUR_APIFY_API_TOKEN"
    from agno.tools.apify import ApifyTools
    return ApifyTools().run_actor(actor_id, run_input)


@tool
def browserbase_navigate(url: str) -> str:
    """Navigate to and read a page using a hosted Browserbase browser session.

    Args:
        url (str): The URL to navigate to.
    """
    os.environ["BROWSERBASE_API_KEY"] = "YOUR_BROWSERBASE_API_KEY"
    os.environ["BROWSERBASE_PROJECT_ID"] = "YOUR_BROWSERBASE_PROJECT_ID"
    from agno.tools.browserbase import BrowserbaseTools
    return BrowserbaseTools().navigate_to(url)


@tool
def docling_convert(file_path_or_url: str) -> str:
    """Convert a document (PDF, DOCX, HTML, etc.) into structured text using Docling.

    Args:
        file_path_or_url (str): Local file path or URL of the document.
    """
    from agno.tools.docling import DoclingTools
    return DoclingTools().convert_document(file_path_or_url)
