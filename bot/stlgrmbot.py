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


def get_last_letter(city, city_list):
    for letter in city[::-1]:
        for item in city_list:
            if item.lower()[0] == letter:
                return letter


def city(update, context):
    user_input = context.args[0].lower().strip()
    if context.user_data.get('game') is None or context.user_data.get('end_game') is True:
        context.user_data['game'] = True
        cities = {'Москва', 'Санкт-Петербург', 'Казань', 'Миасс', 'Никольск', 'Астана'}
        first_letter = user_input[0]
        print(f'First letter from input {first_letter=}')
    else:
        cities = context.user_data['cities']
        first_letter = context.user_data['first_letter']
        print(f'First letter from context {first_letter=}')
    if user_input in [city_name.lower() for city_name in cities]:
        if first_letter == user_input[0]:
            last_letter = get_last_letter(user_input, cities)
            answer_list = [answer_city.lower() for answer_city in cities
                           if answer_city.lower()[0] == last_letter
                           and not answer_city.lower() == user_input
                           ]
            if len(answer_list) > 0:
                update.message.reply_text(f'Your city is {user_input}, {first_letter=}, {last_letter=}')
            else:
                update.message.reply_text("No city left to reply")
                context.user_data['end_game'] = True

            context.user_data['cities'] = cities
            context.user_data['first_letter'] = last_letter
        else:
            update.message.reply_text(f'Your city should start with {first_letter}')
    else:
        context.user_data['cities'] = cities
        update.message.reply_text(f'Your city ({user_input}) is not in known list')
    # if context.user_data.get('game') is None:
    #     context.user_data['game'] = True
    #     cities = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5']
    # else:
    #     cities = context.user_data['cities']
    # user_input = context.args[-1]
    # print(f"{cities=}, {user_input=}")
    # if user_input in cities:
    #     print("Match")
    #     cities.pop()
    #     context.user_data['cities'] = cities
    #     update.message.reply_text(len(context.user_data['cities']))
    # else:
    #     update.message.reply_text(f'{user_input} is unknown')



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
