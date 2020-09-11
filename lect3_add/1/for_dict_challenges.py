# Задание 1
# Дан список учеников, нужно посчитать
# количество повторений каждого имени ученика.
print("Task 1. Name frequency_dict count")
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
print(f'{students=}')
list_names = [student["first_name"] for student in students]
frequency_dict = {}
for name in list_names:
    if name in frequency_dict:
        frequency_dict[name] += 1
    else:
        frequency_dict[name] = 1
for r in frequency_dict.items():
    print(f"{r[0]}: {r[1]}")
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2
print('===')

# Задание 2
# Дан список учеников, нужно вывести самое часто повторяющееся имя.
print("Task 2. Print the most popular name")
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
print(f'{students=}')
list_names = [student["first_name"] for student in students]
frequency_dict = {}
for name in list_names:
    if name in frequency_dict:
        frequency_dict[name] += 1
    else:
        frequency_dict[name] = 1
most_popular_name = max(frequency_dict, key=lambda k: frequency_dict[k])
print(f"The most popular name is {most_popular_name}")
print('===')

# Задание 3
# Есть список учеников в нескольких классах,
# нужно вывести самое частое имя в каждом классе.
print("Task 3. Print the most popular name in each class")
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
for cl_idx, students in enumerate(school_students, start=1):
    list_names = [student["first_name"] for student in students]
    frequency_dict = {}
    for name in list_names:
        if name in frequency_dict:
            frequency_dict[name] += 1
        else:
            frequency_dict[name] = 1
    most_popular_name = max(frequency_dict, key=lambda k: frequency_dict[k])
    print(f"The most popular name in class {cl_idx} is {most_popular_name}")
print('===')

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
print("Task 4. Boys and girls amount in each class.")
school = [
    {'class': '2a',
     'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]
     },
    {'class': '3c',
     'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]
     },
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
print(f'{school=} \n {is_male=}')
for class_data in school:
    gender_dict = {'boys': 0, 'girls': 0}
    for student in class_data['students']:
        if is_male[student['first_name']]:
            gender_dict['boys'] += 1
        else:
            gender_dict['girls'] += 1
    print(f" In {class_data['class']}"
          f" there are {gender_dict['girls']} girls"
          f" and {gender_dict['boys']} boys")
print('===')

# Задание 5
# По информации о учениках разных классов нужно найти класс,
# в котором больше всего девочек и больше всего мальчиков.
print("Task 5. Print class with maximal boys and girls amount.")
school = [
    {'class': '2a',
     'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]
     },
    {'class': '3b',
     'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]
     },
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
print(f'{school=} \n {is_male=}')
gender_total_dict = {}
for class_data in school:
    gender_class_dict = {'boys': 0, 'girls': 0}
    for student in class_data['students']:
        if is_male[student['first_name']]:
            gender_class_dict['boys'] += 1
        else:
            gender_class_dict['girls'] += 1
    gender_total_dict[class_data['class']] = gender_class_dict
boys_max = max(gender_total_dict, key=lambda k: gender_total_dict[k]['boys'])
girls_max = max(gender_total_dict, key=lambda k: gender_total_dict[k]['girls'])
print(f'The maximum boys amount is in "{boys_max}"')
print(f'The maximum girls amount is in "{girls_max}"')
print('===')
