"""
CRM_Ecommerce.py
================
CRM / E-commerce tools from Agno, each as an independent @tool.

pip install agno ShopifyAPI zenpy
"""

import os
from agno.tools import tool


@tool
def shopify_get_products(limit: int = 10) -> str:
    """Get a list of products from a Shopify store.

    Args:
        limit (int): Max number of products to return. Defaults to 10.
    """
    os.environ["SHOPIFY_API_KEY"] = "YOUR_SHOPIFY_API_KEY"
    os.environ["SHOPIFY_API_PASSWORD"] = "YOUR_SHOPIFY_API_PASSWORD"
    os.environ["SHOPIFY_STORE_NAME"] = "YOUR_SHOPIFY_STORE_NAME"
    from agno.tools.shopify import ShopifyTools
    return ShopifyTools().get_products(limit=limit)


@tool
def zendesk_search_tickets(query: str) -> str:
    """Search support tickets in Zendesk.

    Args:
        query (str): The search query.
    """
    os.environ["ZENDESK_EMAIL"] = "YOUR_ZENDESK_EMAIL"
    os.environ["ZENDESK_API_TOKEN"] = "YOUR_ZENDESK_API_TOKEN"
    os.environ["ZENDESK_SUBDOMAIN"] = "YOUR_ZENDESK_SUBDOMAIN"
    from agno.tools.zendesk import ZendeskTools
    return ZendeskTools().search_tickets(query)
