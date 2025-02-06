#!/usr/bin/env python 
# -*- coding: utf-8 -*-"
"""
IAzek - 2024 - por MLEAFIT
IAzek - 2024 - by MLEAFIT
"""

from telegram import Update, InputFile
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext,CallbackQueryHandler
from telegram import Update, InputFile

import json
import logging

from core.tools.data_base import create_user,create_bot,update_user
from core.tools.tools import format_languages_str,enumerate_languages_dict
from dotenv import load_dotenv
import os

logging.basicConfig(level=logging.INFO)
load_dotenv()

languages_options = os.getenv("LANGUAGES")
var_enumerate_languages_dict = enumerate_languages_dict(languages_options)
var_format_languages_str = format_languages_str(enumerate_languages_dict(languages_options))

async def start(update: Update, context: CallbackContext) -> None:
    """
    Send a JSON template file to the user when the bot starts.

    This function is triggered by the "/start" command. It retrieves the JSON template file
    path from the environment variable "JSONEXAMPLE" and sends it to the user's chat as a document.
    The message includes a caption instructing the user to fill out the template and resend it.

    Args:
        update (Update): The incoming update containing message data.
        context (CallbackContext): The context provided by the dispatcher, including the bot instance.

    Returns:
        None
    """
    chat_id = update.effective_chat.id
    json_filename = str(os.getenv("JSONEXAMPLE"))  # Path to your pre-existing JSON file
    await context.bot.send_document(
        chat_id, 
        document=open(json_filename, "rb"),
        caption="Here is your JSON template for creating your user while we make the app\nFill it and resend it to this chat."
    )

async def handle_document(update: Update, context: CallbackContext) -> None:
    """
    Process a JSON document sent by the user and create a bot and user based on its contents.

    This function handles incoming documents. If the document's MIME type is "application/json",
    it downloads the file, validates and loads the JSON data, and extracts the "bot_data" section.
    The extracted data is used to create a bot via the `create_bot` function. It then creates a user
    with the returned bot_id by calling `create_user`. If the JSON is invalid, a fallback example JSON is used.
    If the document is not a JSON file, the function sends a message instructing the user to send a valid JSON file.

    Args:
        update (Update): The incoming update containing the document.
        context (CallbackContext): The context provided by the dispatcher, including the bot instance.

    Returns:
        None
    """
    document = update.message.document
    if document.mime_type == "application/json":
        file = await document.get_file()
        await file.download_to_drive(str(os.getenv("JSONDOWNLOAD")))
        # Load JSON and validate
        try:
            with open(str(os.getenv("JSONDOWNLOAD")), "r", encoding="utf-8") as f:
                data = json.load(f)
            
            if not isinstance(data, dict):
                raise ValueError("Invalid JSON structure")
        except (json.JSONDecodeError, ValueError):
            # Fallback: read the JSON data from the file specified in the environment variable "JSONEXAMPLE"
            fallback_path = str(os.getenv("JSONEXAMPLE"))
            with open(fallback_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        print(data)
        # Extract bot data from JSON
        bot_data = data.get("bot_data", {})
        # Now pass the correct parameters to create_bot using the unpacked bot_data dict
        bot_id = create_bot(**bot_data)
        # Create user with chat_id and bot_id (update as needed for your update_data)
        create_user(chat_id=update.message.chat_id, bot_id=bot_id)
        await update.message.reply_text(f"Bot and user created successfully with Bot ID: {bot_id}")
    else:
        await update.message.reply_text("Please send a valid JSON file.")


async def handle_message(update, context):
    pass