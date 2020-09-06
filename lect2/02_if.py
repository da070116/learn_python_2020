def string_comparator(first_str: str, second_str: str):
    print(f'Comparing "{first_str}" and "{second_str}"')
    if not type(first_str) == type(second_str) == str:
        return 0
    if len(first_str) == len(second_str):
        return 1
    elif second_str == 'learn':
        return 3
    elif len(first_str) > len(second_str):
        return 2


print(string_comparator(1, "e"))
print(string_comparator("1", "e"))
print(string_comparator("1qw", "e"))
print(string_comparator("1qw", "learn"))
print(string_comparator("definately_longer_string", "learn"))
print(string_comparator("learn", "learn"))
