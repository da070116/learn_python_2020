# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
from tornado.autoreload import start

students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
list_names = [student["first_name"] for student in students]
repeats = {}
for name in list_names:
    if name in repeats:
        repeats[name] += 1
    else:
        repeats[name] = 1
for r in repeats.items():
    print(f"{r[0]}: {r[1]}")
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
#
list_names = [student["first_name"] for student in students]
repeats = {}
for name in list_names:
    if name in repeats:
        repeats[name] += 1
    else:
        repeats[name] = 1

most_frequent_name = max(repeats, key=lambda k: repeats[k])
print(f"The most frequent name is {most_frequent_name}")
# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]

for class_idx, students in enumerate(school_students, start=1):
    list_names = [student["first_name"] for student in students]
    repeats = {}
    for name in list_names:
        if name in repeats:
            repeats[name] += 1
        else:
            repeats[name] = 1
    most_frequent_name = max(repeats, key=lambda k: repeats[k])
    print(f"The most frequent name in class {class_idx} is {most_frequent_name}")

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

for class_data in school:
    gender_dict = {'boys': 0, 'girls': 0}
    for student in class_data['students']:
        if is_male[student['first_name']]:
            gender_dict['boys'] += 1
        else:
            gender_dict['girls'] += 1
    print(f"In {class_data['class']} there are {gender_dict['girls']} girls and {gender_dict['boys']} boys")
# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3b', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
gender_school_dict = {}
for class_data in school:
    gender_class_dict = {'boys': 0, 'girls': 0}
    for student in class_data['students']:
        if is_male[student['first_name']]:
            gender_class_dict['boys'] += 1
        else:
            gender_class_dict['girls'] += 1
    gender_school_dict[class_data['class']] = gender_class_dict

print(gender_school_dict)


# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a