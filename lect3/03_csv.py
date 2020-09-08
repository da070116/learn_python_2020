import csv

if __name__ == '__main__':
    personal_data_list = [
        {'name': 'Masha', 'age': 25, 'job': 'Scientist'},
        {'name': 'Vasya', 'age': 8, 'job': 'Programmer'},
        {'name': 'Eduard', 'age': 48, 'job': 'Big boss'},
    ]
    with open('export.csv', 'w', encoding='utf-8', newline='') as csv_file:
        fields = personal_data_list[0].keys()
        writer = csv.DictWriter(csv_file, fields, delimiter=';')
        writer.writeheader()
        for person in personal_data_list:
            writer.writerow(person)
