"""
Simple Bot to change description for today's date
"""

from typing import Optional, Tuple
from telegram import Chat, ChatMember, ChatMemberUpdated, Update
from telegram.constants import ParseMode
from telegram.ext import (Application, ChatMemberHandler, CommandHandler, ContextTypes, MessageHandler, filters)
import calendar
import datetime

# Function to change description
async def change_description(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Setting ID
    channel_id = "CHAT'S ID OR CHANNEL NICKNAME HERE"
    # Getting today's date
    today = datetime.date.today()
    # Making it human-readable
    date_in_words = str(today.day) + ' ' + calendar.month_name[today.month]
    # You can change it
    description = 'Happy ' + date_in_words + '!!🎉'
    # Updating chat description
    await context.bot.setChatDescription(channel_id, description)
    # Printing success message
    print("\n*Description successfully updated*\n")

def main() -> None:
    print("*The bot was started*\n\n")
    """Start the bot."""

    # Create the Application and pass it your bot's token.
    application = Application.builder().token("YOUR TOKEN HERE").build()

    # Set command for bot to change desc
    application.add_handler(CommandHandler("run", change_description))

    # Run the bot
    application.run_polling(allowed_updates=Update.ALL_TYPES)

# Calling main 
if __name__ == "__main__":
    main()