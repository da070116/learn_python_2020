import re
from random import shuffle
from typing import List
from urllib.request import urlopen
from bs4 import BeautifulSoup

from bot.settings import RESET, RESET_MSG, LETTER_MSG, WON_MSG, URL, ERR_MSG


def get_links_from_site() -> List[str]:
    soup = BeautifulSoup(
        urlopen(f'{URL}cityA'), 'html.parser'
    )
    return [a.get('href') for a in soup.find_all('a')
            if a.get('href').startswith('city')
            ]


def obtain_cities_list():
    cities_list = []
    tag_rem = re.compile(r'<[^>]+>')
    for link in get_links_from_site():
        soup = BeautifulSoup(
            urlopen(f'{URL}{link}'), 'html.parser'
        )
        for x in soup.find_all('td'):
            city_name = tag_rem.sub('', str(x))
            if '(' in city_name:
                city_name = city_name.split('(')[0]
            cities_list.append(city_name)
    return set(cities_list)


def get_last(city_val, city_list):
    for letter in city_val[::-1]:
        for item in city_list:
            if item.lower()[0] == letter:
                return letter


def game_logic(update, context):
    cities = None
    user_input = None
    reply = 'No'
    is_in_progress = context.user_data.get("progress")
    if len(context.args) > 0:
        user_input = context.args[0].strip()
    first_letter = context.user_data.get('first_letter')
    if not user_input:
        update.message.reply_text(ERR_MSG)
    elif user_input == RESET:
        context.user_data["first_letter"] = None
        context.user_data["progress"] = None
        update.message.reply_text(RESET_MSG)
    elif not is_in_progress:
        cities = obtain_cities_list()
    else:
        cities = context.user_data['cities']
    if user_input not in cities:
        reply = f'{user_input} не найден в списке'
    elif first_letter and first_letter != user_input.lower()[0]:
        reply = f'{LETTER_MSG} {first_letter}'
    else:
        cities.remove(user_input)
        ll = get_last(user_input, cities)
        answer_list = set(a for a in cities if a.lower().startswith(ll))
        if len(answer_list) == 0:
            reply = f"Не знаю больше городов на {ll}. {WON_MSG}"
            context.user_data['end_game'] = True
        else:
            shuffle(list(answer_list))
            answer = answer_list.pop()
            reply = f'Вы назвали {user_input}... "{answer}"'
            cities.remove(answer)
            context.user_data["first_letter"] = get_last(answer, cities)
            context.user_data["cities"] = cities
            context.user_data['progress'] = True

    update.message.reply_text(reply)
