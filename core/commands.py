from telegram import Update,InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext,CallbackQueryHandler
from core.tools.data_base import create_user,create_bot,update_user
from core.tools.tools import format_languages_str,enumerate_languages_dict
from dotenv import load_dotenv
import os

load_dotenv()
languages_options = os.getenv("LANGUAGES")
var_enumerate_languages_dict = enumerate_languages_dict(languages_options)
var_format_languages_str = format_languages_str(enumerate_languages_dict(languages_options))

def start(update: Update, context: CallbackContext) -> None:
    """
    Starts a simple text-based conversation with the user.
    """

    #languages_options=os.getenv("LANGUAGES")
    update.message.reply_text(
        "Hello welcome to IAzek"
        "What language do you want to learn?\n"+var_format_languages_str+"\n"
        "Please type the number of your choice (e.g., 1, 2, or 3)."
    )
    create_user(update.message.chat_id, bot_id=None, language=None, level=-1, weaknesses=None, strengths=None)
    context.user_data["state"] = "language_choice"  # Set the conversation state


# Step 2: Handle user responses
def handle_message(update: Update, context: CallbackContext) -> None:
    """
    Handles the user's responses based on the current conversation state.
    """
    user_message = update.message.text.strip()
    state = context.user_data.get("state")

    if state == "language_choice":
        # Handle the language choice
        languages = {"1": "English", "2": "Spanish", "3": "German"}
        chosen_language = languages.get(user_message)

        if chosen_language:
            context.user_data["language"] = chosen_language
            update.message.reply_text(
                f"Okay, you chose {chosen_language}. Do you want to personalize your bot?\n"
                "Type '1) yes' or '2) no'."
            )
            context.user_data["state"] = "personalize_bot"
        else:
            update.message.reply_text("Invalid choice. Please type 1, 2, or 3.")

    elif state == "personalize_bot":
        # Handle the bot personalization question
        if user_message.lower() == "yes":
            update.message.reply_text(
                "Great! What gender should your bot be?\n"
                "Type 'male' or 'female'."
            )
            context.user_data["state"] = "bot_gender"
        elif user_message.lower() == "no":
            update.message.reply_text("Got it! Your bot is ready to use. Have fun!")
            context.user_data.clear()  # End the conversation
        else:
            update.message.reply_text("Please type 'yes' or 'no'.")

    elif state == "bot_gender":
        # Handle the gender choice
        if user_message.lower() in ["male", "female"]:
            context.user_data["gender"] = user_message.lower()
            update.message.reply_text(
                f"Awesome! Your bot is {user_message.lower()}. Let's start chatting!"
            )
            context.user_data.clear()  # End the conversation
        else:
            update.message.reply_text("Please type 'male' or 'female'.")

    else:
        # If no state is set, restart the conversation
        update.message.reply_text("Type /start to begin.")
    update_user(chat_id, bot_id=None, language=None, level=None, weaknesses=None, strengths=None, modes=None, current_mode=None, sentiments=None)

def echo(update, context):
    pass