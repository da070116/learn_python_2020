import logging
from telegram.ext import CommandHandler, Updater

logging.basicConfig(filename='tlgrm.log', level=logging.INFO)


def greet(update, context):
    update.message.reply_text(f"Hello, {update.effective_user.first_name}! I'm started")


def main():
    tlgrmbot = Updater("1183917859:AAHU7oW4BB1GJBIICeHl6Hqbcq22m0LVzsw", use_context=True)
    dispatcher = tlgrmbot.dispatcher
    dispatcher.add_handler(CommandHandler('start', greet))
    tlgrmbot.start_polling()
    tlgrmbot.idle()


if __name__ == '__main__':
    main()
