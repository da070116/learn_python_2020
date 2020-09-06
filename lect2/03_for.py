list_digit = range(5, 55, 5)[0:10]
print(*[x+1 for x in list_digit], sep=", ")

input_string = input("Input something: ").strip()
print(*[x for x in input_string], sep='\n')

marks_list = [
    {'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
    {'school_class': '4b', 'scores': [5, 5, 4, 5, 4, 5, 5]},
    {'school_class': '4v', 'scores': [5, 2, 4, 2, 4, 3, 2, 5, 5, 2]},
    {'school_class': '5a', 'scores': [5, 3, 4, 4]},
              ]

total_sum = 0
total_count = 0
for class_journal in marks_list:
    avg = sum(class_journal['scores']) / len(class_journal['scores'])
    total_sum += avg
    total_count += len(class_journal['scores'])
    print(f"Average value for {class_journal['school_class']} is {avg}")
print(f"School average is {total_sum / total_count}")