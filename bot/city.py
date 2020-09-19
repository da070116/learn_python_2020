import re
from random import randint
from typing import List
from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_links_from_site() -> List[str]:
    soup = BeautifulSoup(
        urlopen('http://www.1000mest.ru/cityA'), 'html.parser'
    )
    return [a.get('href') for a in soup.find_all('a')
            if a.get('href').startswith('city')
            ]


def obtain_cities_list():
    cities_list = []
    tag_rem = re.compile(r'<[^>]+>')
    for link in get_links_from_site():
        soup = BeautifulSoup(
            urlopen(f'http://www.1000mest.ru/{link}'), 'html.parser'
        )
        for x in soup.find_all('td'):
            city_name = tag_rem.sub('', str(x))
            if '(' in city_name:
                city_name = city_name.split('(')[0]
            cities_list.append(city_name)
    return cities_list


def get_last(city_val, city_list):
    for letter in city_val[::-1]:
        for item in city_list:
            if item.lower()[0] == letter:
                return letter


def initialize(data):
    _cities = None
    _first_letter = None
    _user_city = None
    if len(data.args) > 0:
        _user_city = data.args[0].strip()
    if not data.user_data.get("progress") or data.user_data.get("end_game"):
        data.user_data['end_game'] = False
        _cities = obtain_cities_list()
        _first_letter = _user_city.lower()[0] if _user_city else None
    else:
        _cities = data.user_data['cities']
        _first_letter = data.user_data['first_letter']
    data.user_data["progress"] = True
    return _user_city, _first_letter, _cities


def game(update, context):
    (user_city, first_letter, cities) = initialize(context)
    if None in (user_city, first_letter, cities):
        result = "Critical error"
        context.user_data['end_game'] = True
        context.user_data["progress"] = False
    elif not user_city.lower()[0] == first_letter:
        result = f"First letter of your city should be {first_letter}"
    else:
        cities.remove(user_city)
        ll = get_last(user_city, cities)
        answer_list = [a for a in cities if a.lower().startswith(ll)]
        if len(answer_list) == 0:
            result = "No city left. You win"
            context.user_data['end_game'] = True
        else:
            answer = answer_list[randint(0, len(answer_list)-1)]
            result = f'Your city was {user_city}. I reply with "{answer}"'
            cities.remove(answer)
            context.user_data["first_letter"] = get_last(answer, cities)
            context.user_data["cities"] = cities
    update.message.reply_text(result)
