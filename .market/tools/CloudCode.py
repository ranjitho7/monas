"""
CloudCode.py
============
Cloud / Code Execution tools from Agno, each as an independent @tool.

pip install agno boto3 daytona-sdk e2b-code-interpreter docker
"""

import os
from agno.tools import tool


@tool
def aws_lambda_invoke(function_name: str, payload: dict) -> str:
    """Invoke an AWS Lambda function.

    Args:
        function_name (str): The name of the Lambda function.
        payload (dict): JSON-serializable payload to send to the function.
    """
    os.environ["AWS_ACCESS_KEY_ID"] = "YOUR_AWS_ACCESS_KEY_ID"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "YOUR_AWS_SECRET_ACCESS_KEY"
    os.environ["AWS_REGION"] = "us-east-1"
    from agno.tools.aws_lambda import AWSLambdaTools
    return AWSLambdaTools().invoke_function(function_name, payload)


@tool
def daytona_run_code(code: str, language: str = "python") -> str:
    """Run code in an isolated Daytona sandbox.

    Args:
        code (str): The source code to execute.
        language (str): Programming language, e.g. "python". Defaults to "python".
    """
    os.environ["DAYTONA_API_KEY"] = "YOUR_DAYTONA_API_KEY"
    from agno.tools.daytona import DaytonaTools
    return DaytonaTools().run_code(code, language=language)


@tool
def e2b_run_code(code: str) -> str:
    """Run Python code in an isolated E2B sandbox.

    Args:
        code (str): The Python code to execute.
    """
    os.environ["E2B_API_KEY"] = "YOUR_E2B_API_KEY"
    from agno.tools.e2b import E2BTools
    return E2BTools().run_python_code(code)


@tool
def docker_run_container(image: str, command: str) -> str:
    """Run a command inside a Docker container.

    Args:
        image (str): The Docker image to use, e.g. "python:3.11".
        command (str): The command to run inside the container.
    """
    from agno.tools.docker import DockerTools
    return DockerTools().run_container(image=image, command=command)


@tool
def shell_run_command(command: str) -> str:
    """Run a shell command on the local machine.

    Args:
        command (str): The shell command to execute.
    """
    from agno.tools.shell import ShellTools
    return ShellTools().run_shell_command(command)


@tool
def python_run_code(code: str) -> str:
    """Execute a snippet of Python code and return the result.

    Args:
        code (str): The Python code to execute.
    """
    from agno.tools.python import PythonTools
    return PythonTools().run_python_code(code)
