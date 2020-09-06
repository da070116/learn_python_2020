import logging
from telegram.ext import CommandHandler, Updater, MessageHandler, Filters
from . import settings


def greet(update, context):
    update.message.reply_text(f"Hello, {update.effective_user.first_name}! I'm started")


def echo(update, context):
    received_message = update.message.text
    update.message.reply_text(received_message)


def main():
    tlgrmbot = Updater(settings.API_KEY, use_context=True)
    dispatcher = tlgrmbot.dispatcher
    dispatcher.add_handler(CommandHandler('start', greet))
    dispatcher.add_handler(MessageHandler(Filters.text, echo))
    logging.info("Bot started")
    tlgrmbot.start_polling()
    tlgrmbot.idle()


if __name__ == '__main__':
    formatter = '%(levelname)s at %(asctime)s:%(name)s:%(message)s'
    logging.basicConfig(filename='tlgrm.log', level=logging.INFO, format=formatter)
    main()
