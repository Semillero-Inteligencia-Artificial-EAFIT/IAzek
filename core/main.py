#!/usr/bin/env python 
# -*- coding: utf-8 -*-"
"""
IAzek - 2024 - por MLEAFIT
IAzek - 2024 - by MLEAFIT
"""
from core.commands import * 
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
 


def main():

    updater = Updater("8193948058:AAGDL6nFJRAColy2H32bqHgKdxEHtqZZib0", use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))


    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    #dp.add_handler(CallbackQueryHandler(choose_language))
    #dp.add_handler(CallbackQueryHandler(choose_bot_type, pattern="^generic_|^custom_bot"))
    #dp.add_handler(CallbackQueryHandler(set_style, pattern="^style_"))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
