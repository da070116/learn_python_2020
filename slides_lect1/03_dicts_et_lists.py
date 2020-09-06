dict_temperature = {'city': 'Moscow', 'temperature': 20}
print(dict_temperature['city'])
dict_temperature['temperature'] -= 5
print(dict_temperature)

print(dict_temperature.get('country'))
dict_temperature.setdefault('country', 'Russia')
dict_temperature['date'] = '27.05.2019'

print(f'{len(dict_temperature)=}')
