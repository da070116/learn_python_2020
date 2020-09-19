import logging
from telegram.ext import CommandHandler, Updater, MessageHandler, Filters
from bot import settings, astronomy, city


def greet(update, context):
    """
    Greeting message
    :param update:
    :param context: Variables of this chat
    :return: "Hello, %name%"
    """
    update.message.reply_text(
        f"Hello, {update.effective_user.first_name}! I'm started"
    )


def echo(update, context):
    """
    Print the same message that user send
    :param update:
    :param context:
    :return:
    """
    received_message = update.message.text
    update.message.reply_text(received_message)


def word_count(update, context):
    """
    Count the number of words in message
    :param update:
    :param context:
    :return:
    """
    test_string = update.message.text.split("/wordcount")[1].strip()
    if test_string:
        update.message.reply_text(
            f"{len([x for x in test_string.split(' ') if x.strip()])} words"
        )
    else:
        update.message.reply_text('The string is not valid')


def main():
    telegram_bot = Updater(settings.API_KEY, use_context=True)
    dispatcher = telegram_bot.dispatcher
    dispatcher.add_handler(CommandHandler('start', greet))
    dispatcher.add_handler(CommandHandler('wordcount', word_count))
    dispatcher.add_handler(CommandHandler('planet', astronomy.planet_location))
    dispatcher.add_handler(CommandHandler('fm', astronomy.full_moon))
    dispatcher.add_handler(CommandHandler('c', city.game))
    dispatcher.add_handler(MessageHandler(Filters.text, echo))
    logging.info("Bot started")
    telegram_bot.start_polling()
    telegram_bot.idle()


if __name__ == '__main__':
    formatter = '%(levelname)s at %(asctime)s:%(name)s:%(message)s'
    logging.basicConfig(
        filename='tlgrm.log',
        level=logging.INFO,
        format=formatter
    )
    main()
