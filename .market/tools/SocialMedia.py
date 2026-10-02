"""
SocialMedia.py
==============
Social Media tools from Agno, each as an independent @tool.

pip install agno tweepy praw spotipy
"""

import os
from agno.tools import tool


@tool
def x_post_tweet(text: str) -> str:
    """Post a tweet to X (Twitter).

    Args:
        text (str): The tweet text.
    """
    os.environ["X_CONSUMER_KEY"] = "YOUR_X_CONSUMER_KEY"
    os.environ["X_CONSUMER_SECRET"] = "YOUR_X_CONSUMER_SECRET"
    os.environ["X_ACCESS_TOKEN"] = "YOUR_X_ACCESS_TOKEN"
    os.environ["X_ACCESS_TOKEN_SECRET"] = "YOUR_X_ACCESS_TOKEN_SECRET"
    from agno.tools.x import XTools
    return XTools().create_post(text)


@tool
def reddit_search_posts(subreddit: str, query: str) -> str:
    """Search posts within a subreddit.

    Args:
        subreddit (str): The subreddit name (without "r/").
        query (str): The search query.
    """
    os.environ["REDDIT_CLIENT_ID"] = "YOUR_REDDIT_CLIENT_ID"
    os.environ["REDDIT_CLIENT_SECRET"] = "YOUR_REDDIT_CLIENT_SECRET"
    os.environ["REDDIT_USER_AGENT"] = "YOUR_APP_NAME/1.0"
    from agno.tools.reddit import RedditTools
    return RedditTools().search_posts(subreddit, query)


@tool
def spotify_search_track(query: str) -> str:
    """Search for a track on Spotify.

    Args:
        query (str): The search query, e.g. "Bohemian Rhapsody Queen".
    """
    os.environ["SPOTIFY_CLIENT_ID"] = "YOUR_SPOTIFY_CLIENT_ID"
    os.environ["SPOTIFY_CLIENT_SECRET"] = "YOUR_SPOTIFY_CLIENT_SECRET"
    from agno.tools.spotify import SpotifyTools
    return SpotifyTools().search_track(query)
