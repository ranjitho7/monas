"""
GoogleWorkspace.py
==================
Google Workspace tools from Agno, each as an independent @tool.
All require Google OAuth credentials / a service account JSON.

pip install agno google-api-python-client google-auth-httplib2 google-auth-oauthlib
"""

import os
from agno.tools import tool


@tool
def google_drive_search(query: str) -> str:
    """Search files in Google Drive.

    Args:
        query (str): The search query.
    """
    os.environ["GOOGLE_CLIENT_ID"] = "YOUR_GOOGLE_CLIENT_ID"
    os.environ["GOOGLE_CLIENT_SECRET"] = "YOUR_GOOGLE_CLIENT_SECRET"
    from agno.tools.google_drive import GoogleDriveTools
    return GoogleDriveTools().search_files(query)


@tool
def google_calendar_list_events(calendar_id: str = "primary") -> str:
    """List upcoming events on a Google Calendar.

    Args:
        calendar_id (str): The calendar ID. Defaults to "primary".
    """
    os.environ["GOOGLE_CLIENT_ID"] = "YOUR_GOOGLE_CLIENT_ID"
    os.environ["GOOGLE_CLIENT_SECRET"] = "YOUR_GOOGLE_CLIENT_SECRET"
    from agno.tools.googlecalendar import GoogleCalendarTools
    return GoogleCalendarTools().list_events(calendar_id=calendar_id)


@tool
def google_sheets_read(spreadsheet_id: str, range_name: str) -> str:
    """Read values from a Google Sheet.

    Args:
        spreadsheet_id (str): The spreadsheet ID.
        range_name (str): The A1 notation range to read, e.g. "Sheet1!A1:D10".
    """
    os.environ["GOOGLE_CLIENT_ID"] = "YOUR_GOOGLE_CLIENT_ID"
    os.environ["GOOGLE_CLIENT_SECRET"] = "YOUR_GOOGLE_CLIENT_SECRET"
    from agno.tools.googlesheets import GoogleSheetsTools
    return GoogleSheetsTools().read_sheet(spreadsheet_id, range_name)


@tool
def google_maps_search_places(query: str) -> str:
    """Search for places using Google Maps.

    Args:
        query (str): The place search query, e.g. "coffee shops in Bangalore".
    """
    os.environ["GOOGLE_MAPS_API_KEY"] = "YOUR_GOOGLE_MAPS_API_KEY"
    from agno.tools.googlemaps import GoogleMapTools
    return GoogleMapTools().search_places(query)


@tool
def google_bigquery_run_query(sql_query: str, project_id: str) -> str:
    """Run a SQL query against Google BigQuery.

    Args:
        sql_query (str): The SQL query to execute.
        project_id (str): Your Google Cloud project ID.
    """
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "YOUR_SERVICE_ACCOUNT_JSON_PATH"
    from agno.tools.google_bigquery import GoogleBigQueryTools
    return GoogleBigQueryTools(project=project_id).run_query(sql_query)
