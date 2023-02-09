"""
Simple Bot to change description for today's date
"""
from typing import Optional, Tuple

from telegram import __version__ as TG_VER

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)
from telegram import Chat, ChatMember, ChatMemberUpdated, Update
from telegram.constants import ParseMode
from telegram.ext import (
    Application,
    ChatMemberHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)
import calendar
import datetime

async def greet_chat_members(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Greets new users in chats and announces when someone leaves"""
    result = extract_status_change(update.chat_member)
    if result is None:
        return

    was_member, is_member = result
    member_name = update.chat_member.new_chat_member.user.mention_html()

    if not was_member and is_member:
        await update.effective_chat.send_message(
            f"{member_name} joined us!",
            parse_mode=ParseMode.HTML,
        )
    elif was_member and not is_member:
        await update.effective_chat.send_message(
            f"{member_name} left us.",
            parse_mode=ParseMode.HTML,
        )



async def change_description(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    channel_id = "CHAT'S ID OR CHANNEL NICKNAME HERE"
    today = datetime.date.today()
    date_in_words = str(today.day) + ' ' + calendar.month_name[today.month]
    description = 'Happy ' + date_in_words + '!!🎉'
    await context.bot.setChatDescription(channel_id, description)
    print("\ndescription successfully changed\n")

def main() -> None:
    print("bot was started\n\n")
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("YOUR TOKEN HERE").build()

    #set command for bot to change desc
    application.add_handler(CommandHandler("run", change_description))

    # Handle members joining/leaving chats.
    application.add_handler(ChatMemberHandler(greet_chat_members, ChatMemberHandler.CHAT_MEMBER))

    # Run the bot
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()