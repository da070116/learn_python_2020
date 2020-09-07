import logging
import ephem
from telegram.ext import CommandHandler, Updater, MessageHandler, Filters
from bot import settings


def greet(update, context):
    update.message.reply_text(f"Hello, {update.effective_user.first_name}! I'm started")


def echo(update, context):
    received_message = update.message.text
    update.message.reply_text(received_message)


def planet_location(update, context):
    requested_planet = update.message.text.split("/planet")[1].strip()
    if requested_planet == 'Moon':
        p = ephem.Moon(str(update.message.date))
    elif requested_planet == 'Mars':
        p = ephem.Mars(str(update.message.date))
    elif requested_planet == 'Venus':
        p = ephem.Venus(str(update.message.date))
    elif requested_planet == 'Mercury':
        p = ephem.Mercury(str(update.message.date))
    elif requested_planet == 'Jupiter':
        p = ephem.Jupiter(str(update.message.date))
    elif requested_planet == 'Saturn':
        p = ephem.Saturn(str(update.message.date))
    elif requested_planet == 'Uranus':
        p = ephem.Uranus(str(update.message.date))
    elif requested_planet == 'Neptune':
        p = ephem.Neptune(str(update.message.date))
    elif requested_planet == 'Pluto':
        p = ephem.Pluto(str(update.message.date))
    elif requested_planet == 'Earth':
        pass
    else:
        update.message.reply_text(f"There is no planet {requested_planet} in our solar system")
    constellation = ephem.constellation(p)[1]
    update.message.reply_text(f"Today {requested_planet} is in {constellation} that won't affect on your fate")



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
    logging.basicConfig(filename='tlgrm.log', level=logging.INFO, format=formatter)
    main()
