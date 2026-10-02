"""
Finance.py
==========
Finance & Markets tools from Agno, each as an independent @tool.

pip install agno yfinance openbb financialdatasets
"""

import os
from agno.tools import tool


@tool
def yfinance_get_stock_price(symbol: str) -> str:
    """Get the current stock price for a ticker symbol using YFinance.

    Args:
        symbol (str): Stock ticker symbol, e.g. "AAPL".
    """
    from agno.tools.yfinance import YFinanceTools
    return YFinanceTools(stock_price=True).get_current_stock_price(symbol)


@tool
def yfinance_company_info(symbol: str) -> str:
    """Get company information and fundamentals using YFinance.

    Args:
        symbol (str): Stock ticker symbol, e.g. "AAPL".
    """
    from agno.tools.yfinance import YFinanceTools
    return YFinanceTools(company_info=True).get_company_info(symbol)


@tool
def openbb_search(query: str) -> str:
    """Search financial data and market information using OpenBB.

    Args:
        query (str): The financial data query, e.g. "AAPL income statement".
    """
    os.environ["OPENBB_PAT"] = "YOUR_OPENBB_PAT"
    from agno.tools.openbb import OpenBBTools
    return OpenBBTools().search(query)


@tool
def financial_datasets_get_income_statement(ticker: str) -> str:
    """Get a company's income statement using the Financial Datasets API.

    Args:
        ticker (str): Stock ticker symbol, e.g. "AAPL".
    """
    os.environ["FINANCIAL_DATASETS_API_KEY"] = "YOUR_FINANCIAL_DATASETS_API_KEY"
    from agno.tools.financial_datasets import FinancialDatasetsTools
    return FinancialDatasetsTools().get_income_statements(ticker)


@tool
def redshift_query_market_data(sql_query: str) -> str:
    """Run a SQL query against a Redshift warehouse holding market data.

    Args:
        sql_query (str): The SQL query to run.
    """
    os.environ["REDSHIFT_HOST"] = "YOUR_REDSHIFT_HOST"
    os.environ["REDSHIFT_USER"] = "YOUR_REDSHIFT_USER"
    os.environ["REDSHIFT_PASSWORD"] = "YOUR_REDSHIFT_PASSWORD"
    from agno.tools.redshift import RedshiftTools
    return RedshiftTools().run_query(sql_query)


@tool
def market_sentiment_analysis(symbol: str) -> str:
    """Get aggregated market sentiment for a ticker (news/social based).

    Args:
        symbol (str): Stock ticker symbol, e.g. "TSLA".
    """
    os.environ["ADANOS_API_KEY"] = "YOUR_ADANOS_API_KEY"
    from agno.tools.adanos import AdanosMarketSentimentTools
    return AdanosMarketSentimentTools().get_sentiment(symbol)
