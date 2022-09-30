import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!"
    )


if __name__ == "__main__":
    application = (
        ApplicationBuilder()
        .token("5639894858:AAFi9dcbODywn645Oy1XcvNxEo5ZVmy_8wI")
        .build()
    )

    start_handler = CommandHandler("start", start)
    application.add_handler(start_handler)

    application.run_polling()

# https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions-%E2%80%93-Your-first-Bot
# pip install python-telegram-bot --pre
