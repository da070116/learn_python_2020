import logging
from datetime import datetime

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


def full_moon(update, context):
    date_string = update.message.text.split("/fm")[1].strip()
    dt = datetime.strptime(date_string, "%Y-%m-%d")
    print(dt)
    update.message.reply_text("ok")


def planet_location(update, context):
    planet = update.message.text.split("/planet")[1].strip()
    possible_planets = [n for _0, _1, n in ephem._libastro.builtin_planets()]
    if planet in possible_planets:
        planet_function = getattr(ephem, planet)
        planet = planet_function(str(update.message.date))
        constellation = ephem.constellation(planet)[1]
        update.message.reply_text(f"Today {planet} is in {constellation}")
    else:
        msg = ' is not in our solar system. Live and prosper, friend!'
        update.message.reply_text(f"{planet} {msg}")


def word_count(update, context):
    test_str = update.message.text.split("/wordcount")[1].strip()
    if test_str:
        update.message.reply_text(
            f"{len([x for x in test_str.split(' ') if x.strip()])} words"
        )
    else:
        update.message.reply_text('The string is not valid')


def main():
    tlgrmbot = Updater(settings.API_KEY, use_context=True)
    dispatcher = tlgrmbot.dispatcher
    dispatcher.add_handler(CommandHandler('start', greet))
    dispatcher.add_handler(CommandHandler('wordcount', word_count))
    dispatcher.add_handler(CommandHandler('planet', planet_location))
    dispatcher.add_handler(CommandHandler('fm', full_moon))
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
