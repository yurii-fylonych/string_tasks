# 21.1

string = 'ab-aa;sd-ab-ka'
symbols = '-;'
result = ''
k = 0

for index, char in enumerate(string):
    for i in symbols:
        if i == char:
            result += string[k: index] + ' '
            k = index + 1

list_of_word = result.split()

for word in list_of_word:
    print(word, end=' ')


# 21.2

string = 'ab-aa;sd-ab-ka'
symbols = '-;'

for char in symbols:
    string = string.replace(char, ' ')

result = string.split()

for word in result:
    print(word, end=' ')


# 22

text = "qweeqw a333sa3 333 qwe333qew13 asdaasd"
digit = '0123456789'
letter = 'qwetryuioopasdfghjklzxsacvbnm '
n = 0
max_number = 0

for char in text:
    if n > max_number:
        max_number = n
    if char in digit:
        n += 1
    else:
        n = 0

print(max_number)

# 23

string = 'ab-aldlka;sd-a123bag-kj11fdjaba'
sum_digits = 0

for char in string:
    if char.isdigit():
        sum_digits += int(char)

print(sum_digits)


# 24.1
string = 'ab-aldlka;sd-a123bag-kj11fdjaba'

k = string.split(' ')
sum_digit = 0

for i in k:
    try:
        sum_digit += int(i)
    except:
        pass

print(sum_digit)

# 24.2

sum_digit = 0
current = ''

for ch in string:
    if ch.isdigit():
        current += ch
    elif current != '':
        sum_digit += int(current)
        current = ''

print(sum_digit)


# 24.3

string = 'abbaldlka 21 31   bsd-a123bag kj11fdjaba'
sum = 0
words_list = string.split()

for word in words_list:
    if word.isdigit() == True:
        sum += int(word)


print(sum)



# 25.1

string = 'abbaldlka 21 31   bsd-a123bag kj11fdjaba'

max_space = 0
n = 0

for i in range(len(string)):
    if string[i] == ' ':
        n += 1
    else:
        if n > max_space:
            max_space = n
        n = 0

print(max_space)



# 26

first_word = 'abbAdlkma'
second_word = 'asdvfmj'
signs = ''

for i in first_word.lower():
    count_first = first_word.lower().count(i)
    count_second = second_word.lower().count(i)
    if count_first == count_second == 1:
        signs += i

print(signs)


# 27

list_str = ['abbaldlka', '21', '323', 'bsd-a123bag', 'kj11fdjaba']

result = sorted(list_str, key = len)

print(result)


# 28

list_strings = ['abbAdlka', 'abbAdlka', 'asd44444vfj', 'asdvfd2ej', 'asdvf123j']

list_digit_in_word = []

list_strings = ['3333333', 'abb333Adlka', 'asd44444vfj', 'asdvfd2ej', 'asdvf123j']


list_digit_in_word = list(map(lambda word: len(list(filter(lambda x: x.isdigit(), word))), list_strings))


for i in range(len(list_digit_in_word) - 1):
    for j in range(len(list_digit_in_word) - 1 - i):
        if list_digit_in_word[j] > list_digit_in_word[j + 1]:
            list_digit_in_word[j], list_digit_in_word[j + 1] = list_digit_in_word[j + 1], list_digit_in_word[j]
            list_strings[j], list_strings[j + 1] = list_strings[j + 1], list_strings[j]

i = 0
d = {}

while i < len(list_digit_in_word):
    if list_digit_in_word[i] in d.keys():
        d[list_digit_in_word[i]].append(list_strings[i])
    else:
        d[list_digit_in_word[i]] = [list_strings[i]]
    i += 1

d = dict(d)

print(d)


# 29

string = 'abbAdlka 21 323 bsB-a1Dbag kaj11Baba'

str = string.replace('a', 'A').replace('b', 'B')
print(str)