#!/usr/bin/env python 
# -*- coding: utf-8 -*-"
"""
IAzek - 2024 - por MLEAFIT
IAzek - 2024 - by MLEAFIT
"""

from core.commands import * 
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import os

def main():
    """
    Initialize and run the Telegram bot application.

    This function performs the following steps:
      1. Creates a new Application instance using the Telegram bot token retrieved from the environment variable "TOKEN".
      2. Registers various handlers:
         - A CommandHandler for the "/start" command that triggers the `start` function.
         - A MessageHandler for text messages (excluding commands) that triggers the `handle_message` function.
         - A MessageHandler for document messages that triggers the `handle_document` function.
      3. (Optional) Additional CallbackQueryHandlers can be added by uncommenting and adjusting the provided examples.
      4. Starts the bot in polling mode to continuously listen for and process incoming updates.

    Returns:
        None
    """
    app = Application.builder().token(os.getenv("TOKEN")).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(MessageHandler(filters.Document.ALL, handle_document))

    # Uncomment and adjust these if needed
    # app.add_handler(CallbackQueryHandler(choose_language))
    # app.add_handler(CallbackQueryHandler(choose_bot_type, pattern="^generic_|^custom_bot"))
    # app.add_handler(CallbackQueryHandler(set_style, pattern="^style_"))

    app.run_polling()

if __name__ == "__main__":
    main()


