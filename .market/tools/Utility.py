"""
Utility.py
==========
Core Utility tools from Agno, each as an independent @tool. None require
an API key.

pip install agno
"""

import time
from agno.tools import tool


@tool
def calculator_evaluate(expression: str) -> str:
    """Evaluate a basic math expression.

    Args:
        expression (str): A math expression, e.g. "23 * (4 + 5)".
    """
    from agno.tools.calculator import CalculatorTools
    return str(CalculatorTools().evaluate(expression))


@tool
def file_read(file_path: str) -> str:
    """Read and return the contents of a local file.

    Args:
        file_path (str): Path to the file.
    """
    from agno.tools.file import FileTools
    return FileTools().read_file(file_path)


@tool
def file_save(file_path: str, content: str) -> str:
    """Save text content to a local file.

    Args:
        file_path (str): Path to write the file to.
        content (str): The text content to save.
    """
    from agno.tools.file import FileTools
    return FileTools().save_file(content, file_path)


@tool
def sleep_wait(seconds: float) -> str:
    """Pause execution for a given number of seconds.

    Args:
        seconds (float): Number of seconds to sleep.
    """
    time.sleep(seconds)
    return f"Slept for {seconds} seconds."


@tool
def custom_api_call(url: str, method: str = "GET", payload: dict = None) -> str:
    """Make a raw HTTP call to a custom API endpoint.

    Args:
        url (str): The API endpoint URL.
        method (str): HTTP method, e.g. "GET" or "POST". Defaults to "GET".
        payload (dict): Optional JSON body for POST/PUT requests.
    """
    import requests
    response = requests.request(method=method, url=url, json=payload)
    return response.text


@tool
def visualization_plot_chart(data_json: str, chart_type: str = "bar") -> str:
    """Generate a simple chart from JSON data using visualization tools.

    Args:
        data_json (str): JSON string of the data to plot.
        chart_type (str): Chart type, e.g. "bar", "line", "pie". Defaults to "bar".
    """
    from agno.tools.visualization import VisualizationTools
    return VisualizationTools().create_chart(data_json, chart_type=chart_type)
