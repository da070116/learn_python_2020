import logging
import ephem
from telegram.ext import CommandHandler, Updater, MessageHandler, Filters
from bot import settings


def greet(update, context):
    update.message.reply_text(
        f"Hello, {update.effective_user.first_name}! I'm started"
    )


def echo(update, context):
    received_message = update.message.text
    update.message.reply_text(received_message)


def planet_location(update, context):
    planet = update.message.text.split("/planet")[1].strip()
    try:
        planet_function = getattr(ephem, planet)
    except AttributeError:
        update.message.reply_text("No such planet.")
    if planet_function:
        planet = planet_function(str(update.message.date))
        constellation = ephem.constellation(planet)[1]
        update.message.reply_text(f"Today {planet} is in {constellation}")


def main():
    tlgrmbot = Updater(settings.API_KEY, use_context=True)
    dispatcher = tlgrmbot.dispatcher
    dispatcher.add_handler(CommandHandler('start', greet))
    dispatcher.add_handler(CommandHandler('planet', planet_location))
    dispatcher.add_handler(MessageHandler(Filters.text, echo))
    logging.info("Bot started")
    tlgrmbot.start_polling()
    tlgrmbot.idle()


if __name__ == '__main__':
    formatter = '%(levelname)s at %(asctime)s:%(name)s:%(message)s'
    logging.basicConfig(
        filename='tlgrm.log',
        level=logging.INFO,
        format=formatter
    )
    main()
