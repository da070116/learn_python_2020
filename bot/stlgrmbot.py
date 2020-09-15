import logging
import re
# from random import randint
from typing import List
from urllib.request import urlopen
from datetime import datetime
import ephem
from telegram.ext import CommandHandler, Updater, MessageHandler, Filters
from bot import settings
from bs4 import BeautifulSoup


def get_links() -> List[str]:
    soup = BeautifulSoup(
        urlopen('http://www.1000mest.ru/cityA'), 'html.parser'
    )
    return [a.get('href')
            for a in soup.find_all('a') if a.get('href').startswith('city')
            ]


def obtain_cities_list():
    get_links()
    cities_list = []
    tag_rem = re.compile(r'<[^>]+>')
    for link in get_links():
        soup = BeautifulSoup(
            urlopen(f'http://www.1000mest.ru/{link}'), 'html.parser'
        )
        for x in soup.find_all('td'):
            city_name = tag_rem.sub('', str(x))
            if '(' in city_name:
                city_name = city_name.split('(')[0]
            cities_list.append(city_name)
    return cities_list


def city(update, context):
    if context.user_data.get('game') is None:
        context.user_data['game'] = True
        cities = ['A1', 'A2', 'A3', 'A4', 'A5']
    else:
        cities = context.user_data['cities']
    user_input = context.args[0].lower()
    if user_input.strip() in [c.lower() for c in cities]:
        cities.pop()
        context.user_data['cities'] = cities
        update.message.reply_text(len(context.user_data['cities']))
    else:
        update.message.reply_text(f'{user_input} is unknown')

    # try_city = context.args[0].lower().strip()
    # if not context.user_data.get('game'):
    #     context.user_data['game'] = 'playing'
    #     all_cities = obtain_cities_list()
    # else:
    #     all_cities = context.user_data['cities']
    # if try_city in all_cities:
    #     letter = try_city[-1]
    #     available_cities = [c for c in all_cities if c[0].lower == letter]
    #     rand_num = randint(len(available_cities))
    #     answer = available_cities[rand_num]
    #     all_cities.remove(answer)
    #     context.user_data['cities'] = all_cities
    #     update.message.reply_text(answer)
    # else:
    #     update.message.reply_text(f'{try_city} is unknown')


def greet(update, context):
    update.message.reply_text(
        f"Hello, {update.effective_user.first_name}! I'm started"
    )


def echo(update, context):
    received_message = update.message.text
    update.message.reply_text(received_message)


def full_moon(update, context):
    date_string = update.message.text.split("/fm")[1].strip()
    try:
        date = datetime.strptime(date_string, '%Y-%m-%d')
        update.message.reply_text(
            f'Next full moon will be {ephem.next_full_moon(date)}'
        )
    except ValueError:
        update.message.reply_text('Date should be in YYYY-mm-dd format')


def planet_location(update, context):
    planet = update.message.text.split("/planet")[1].strip()
    possible_planets = [n for _0, _1, n in ephem._libastro.builtin_planets()]
    if planet in possible_planets:
        planet_function = getattr(ephem, planet)
        planet = planet_function(str(update.message.date))
        constellation = ephem.constellation(planet)[1]
        update.message.reply_text(f"Today {planet} is in {constellation}")
    else:
        update.message.reply_text(
            f"{planet} is not in our solar system. Live and prosper, friend!"
        )


def word_count(update, context):
    test_string = update.message.text.split("/wordcount")[1].strip()
    if test_string:
        update.message.reply_text(
            f"{len([x for x in test_string.split(' ') if x.strip()])} words"
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
    dispatcher.add_handler(CommandHandler('c', city))
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
