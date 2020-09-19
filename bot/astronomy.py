from datetime import datetime
import ephem


def full_moon(update, context):
    """
    Print the closest full moon date
    :return: Next full moon will be on %date%
    """
    date_string = context.args[0].strip()
    try:
        date = datetime.strptime(date_string, '%Y-%m-%d')
        response = f'Next full moon will be on {ephem.next_full_moon(date)}'
    except ValueError:
        response = 'Date should be in YYYY-mm-dd format'
    update.message.reply_text(response)


def planet_location(update, context):
    """
    In which constellation the requested planet is today?
    :return:
    """
    planet = context.args[0].strip()
    possible_planets = [n for _0, _1, n in ephem._libastro.builtin_planets()]
    if planet in possible_planets:
        planet_function = getattr(ephem, planet)
        planet = planet_function(str(update.message.date))
        constellation = ephem.constellation(planet)[1]
        response = f"Today {planet} is in {constellation}"
    else:
        response = f"{planet} is not in our solar system."
    update.message.reply_text(response)
