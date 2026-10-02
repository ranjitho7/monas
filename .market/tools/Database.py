"""
Database.py
===========
Data / Database tools from Agno, each as an independent @tool.

pip install agno sqlalchemy psycopg2-binary duckdb pandas neo4j
pip install google-cloud-bigquery redshift-connector
"""

import os
from agno.tools import tool


@tool
def sql_run_query(sql_query: str, db_url: str) -> str:
    """Run a raw SQL query against a database.

    Args:
        sql_query (str): The SQL query to execute.
        db_url (str): SQLAlchemy-style connection string, e.g. "sqlite:///data.db".
    """
    from agno.tools.sql import SQLTools
    return SQLTools(db_url=db_url).run_sql_query(sql_query)


@tool
def postgres_run_query(sql_query: str) -> str:
    """Run a SQL query against a Postgres database.

    Args:
        sql_query (str): The SQL query to execute.
    """
    os.environ["POSTGRES_HOST"] = "YOUR_POSTGRES_HOST"
    os.environ["POSTGRES_USER"] = "YOUR_POSTGRES_USER"
    os.environ["POSTGRES_PASSWORD"] = "YOUR_POSTGRES_PASSWORD"
    os.environ["POSTGRES_DB"] = "YOUR_POSTGRES_DB"
    from agno.tools.postgres import PostgresTools
    return PostgresTools().run_query(sql_query)


@tool
def duckdb_run_query(sql_query: str, db_path: str = ":memory:") -> str:
    """Run a SQL query using DuckDB (in-memory or file-based).

    Args:
        sql_query (str): The SQL query to execute.
        db_path (str): Path to a DuckDB database file, or ":memory:" (default).
    """
    from agno.tools.duckdb import DuckDbTools
    return DuckDbTools(db_path=db_path).run_query(sql_query)


@tool
def pandas_run_query(csv_path: str, pandas_expression: str) -> str:
    """Load a CSV into a Pandas DataFrame and run a Pandas expression on it.

    Args:
        csv_path (str): Path to the CSV file.
        pandas_expression (str): A Pandas expression to evaluate, e.g. "df.describe()".
    """
    from agno.tools.pandas import PandasTools
    return PandasTools().run_query(csv_path, pandas_expression)


@tool
def csv_read(csv_path: str) -> str:
    """Read and return the contents of a CSV file.

    Args:
        csv_path (str): Path to the CSV file.
    """
    from agno.tools.csv_toolkit import CsvTools
    return CsvTools().read_csv(csv_path)


@tool
def bigquery_run_query(sql_query: str, project_id: str) -> str:
    """Run a SQL query against Google BigQuery.

    Args:
        sql_query (str): The SQL query to execute.
        project_id (str): Your Google Cloud project ID.
    """
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "YOUR_SERVICE_ACCOUNT_JSON_PATH"
    from agno.tools.google_bigquery import GoogleBigQueryTools
    return GoogleBigQueryTools(project=project_id).run_query(sql_query)


@tool
def neo4j_run_query(cypher_query: str) -> str:
    """Run a Cypher query against a Neo4j graph database.

    Args:
        cypher_query (str): The Cypher query to execute.
    """
    os.environ["NEO4J_URI"] = "YOUR_NEO4J_URI"
    os.environ["NEO4J_USERNAME"] = "YOUR_NEO4J_USERNAME"
    os.environ["NEO4J_PASSWORD"] = "YOUR_NEO4J_PASSWORD"
    from agno.tools.neo4j import Neo4jTools
    return Neo4jTools().run_query(cypher_query)


@tool
def redshift_run_query(sql_query: str) -> str:
    """Run a SQL query against an Amazon Redshift warehouse.

    Args:
        sql_query (str): The SQL query to execute.
    """
    os.environ["REDSHIFT_HOST"] = "YOUR_REDSHIFT_HOST"
    os.environ["REDSHIFT_USER"] = "YOUR_REDSHIFT_USER"
    os.environ["REDSHIFT_PASSWORD"] = "YOUR_REDSHIFT_PASSWORD"
    from agno.tools.redshift import RedshiftTools
    return RedshiftTools().run_query(sql_query)
