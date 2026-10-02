"""
Communication.py
================
Communication / Messaging tools from Agno, each as an independent @tool.

pip install agno slack-sdk discord.py python-telegram-bot twilio boto3 resend
"""

import os
from agno.tools import tool


@tool
def slack_send_message(channel: str, text: str) -> str:
    """Send a message to a Slack channel.

    Args:
        channel (str): Slack channel name or ID, e.g. "#general".
        text (str): The message text to send.
    """
    os.environ["SLACK_TOKEN"] = "YOUR_SLACK_BOT_TOKEN"
    from agno.tools.slack import SlackTools
    return SlackTools().send_message(channel, text)


@tool
def discord_send_message(channel_id: str, message: str) -> str:
    """Send a message to a Discord channel.

    Args:
        channel_id (str): The Discord channel ID.
        message (str): The message text to send.
    """
    os.environ["DISCORD_BOT_TOKEN"] = "YOUR_DISCORD_BOT_TOKEN"
    from agno.tools.discord import DiscordTools
    return DiscordTools().send_message(channel_id, message)


@tool
def telegram_send_message(chat_id: str, text: str) -> str:
    """Send a message via a Telegram bot.

    Args:
        chat_id (str): The Telegram chat ID.
        text (str): The message text to send.
    """
    os.environ["TELEGRAM_TOKEN"] = "YOUR_TELEGRAM_BOT_TOKEN"
    from agno.tools.telegram import TelegramTools
    return TelegramTools(chat_id=chat_id).send_message(text)


@tool
def whatsapp_send_message(to_number: str, message: str) -> str:
    """Send a WhatsApp message via the WhatsApp Business API.

    Args:
        to_number (str): Recipient phone number in international format.
        message (str): The message text to send.
    """
    os.environ["WHATSAPP_ACCESS_TOKEN"] = "YOUR_WHATSAPP_ACCESS_TOKEN"
    os.environ["WHATSAPP_PHONE_NUMBER_ID"] = "YOUR_WHATSAPP_PHONE_NUMBER_ID"
    from agno.tools.whatsapp import WhatsAppTools
    return WhatsAppTools().send_message(to_number, message)


@tool
def webex_send_message(room_id: str, text: str) -> str:
    """Send a message to a Webex room.

    Args:
        room_id (str): The Webex room ID.
        text (str): The message text to send.
    """
    os.environ["WEBEX_ACCESS_TOKEN"] = "YOUR_WEBEX_ACCESS_TOKEN"
    from agno.tools.webex import WebexTools
    return WebexTools().send_message(room_id, text)


@tool
def email_send(to_email: str, subject: str, body: str) -> str:
    """Send an email via SMTP.

    Args:
        to_email (str): Recipient email address.
        subject (str): Email subject line.
        body (str): Email body text.
    """
    os.environ["EMAIL_SENDER_ADDRESS"] = "YOUR_EMAIL_ADDRESS"
    os.environ["EMAIL_SENDER_PASSKEY"] = "YOUR_EMAIL_APP_PASSWORD"
    from agno.tools.email import EmailTools
    return EmailTools().email_user(subject=subject, body=body, receiver_email=to_email)


@tool
def aws_ses_send_email(to_email: str, subject: str, body: str) -> str:
    """Send an email using Amazon SES.

    Args:
        to_email (str): Recipient email address.
        subject (str): Email subject line.
        body (str): Email body text.
    """
    os.environ["AWS_ACCESS_KEY_ID"] = "YOUR_AWS_ACCESS_KEY_ID"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "YOUR_AWS_SECRET_ACCESS_KEY"
    os.environ["AWS_REGION"] = "us-east-1"
    from agno.tools.aws_ses import AWSSESTool
    return AWSSESTool().send_email(to_email, subject, body)


@tool
def resend_send_email(to_email: str, subject: str, body: str) -> str:
    """Send an email using Resend.

    Args:
        to_email (str): Recipient email address.
        subject (str): Email subject line.
        body (str): Email body text (HTML supported).
    """
    os.environ["RESEND_API_KEY"] = "YOUR_RESEND_API_KEY"
    from agno.tools.resend import ResendTools
    return ResendTools().send_email(to_email, subject, body)


@tool
def plivo_send_sms(to_number: str, message: str) -> str:
    """Send an SMS message using Plivo.

    Args:
        to_number (str): Recipient phone number in international format.
        message (str): The SMS text to send.
    """
    os.environ["PLIVO_AUTH_ID"] = "YOUR_PLIVO_AUTH_ID"
    os.environ["PLIVO_AUTH_TOKEN"] = "YOUR_PLIVO_AUTH_TOKEN"
    from agno.tools.plivo import PlivoTools
    return PlivoTools().send_sms(to_number, message)


@tool
def twilio_send_sms(to_number: str, message: str) -> str:
    """Send an SMS message using Twilio.

    Args:
        to_number (str): Recipient phone number in international format.
        message (str): The SMS text to send.
    """
    os.environ["TWILIO_ACCOUNT_SID"] = "YOUR_TWILIO_ACCOUNT_SID"
    os.environ["TWILIO_AUTH_TOKEN"] = "YOUR_TWILIO_AUTH_TOKEN"
    from agno.tools.twilio import TwilioTools
    return TwilioTools().send_sms(to_number, message)


@tool
def zoom_create_meeting(topic: str, start_time: str, duration_minutes: int = 30) -> str:
    """Schedule a Zoom meeting.

    Args:
        topic (str): The meeting topic/title.
        start_time (str): ISO 8601 start time, e.g. "2026-09-10T15:00:00".
        duration_minutes (int): Meeting duration in minutes. Defaults to 30.
    """
    os.environ["ZOOM_ACCOUNT_ID"] = "YOUR_ZOOM_ACCOUNT_ID"
    os.environ["ZOOM_CLIENT_ID"] = "YOUR_ZOOM_CLIENT_ID"
    os.environ["ZOOM_CLIENT_SECRET"] = "YOUR_ZOOM_CLIENT_SECRET"
    from agno.tools.zoom import ZoomTools
    return ZoomTools().schedule_meeting(topic=topic, start_time=start_time, duration=duration_minutes)
