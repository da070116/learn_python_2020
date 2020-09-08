# Вывести последнюю букву в слове
word = 'Архангельск'
print(f"The last letter in '{word}' is '{word[-1]}'\n")

# Вывести количество букв "а" в слове
word = 'Архангельск'
print(f"There are {word.lower().count('а')} 'a' letters in '{word}'\n")

# Вывести количество гласных букв в слове
word = 'Архангельск'
total_count = 0
for vowel in set('аеиоуыэяю'):
    total_count += word.lower().count(vowel)
print(f"There are {total_count} vowels in '{word}'\n")

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(f'Word count in "{sentence}" is equal to {len(sentence.split(" "))}\n')

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
print(f'The first letter of each word in "{sentence}"')
print(*[x[0] for x in sentence.split(' ')], sep='\n')
print('')


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
words = sentence.split(' ')
avg_len = sum([len(w) for w in words]) / len(words)
print(f'Average word length in "{sentence}" is equal to {avg_len}')
