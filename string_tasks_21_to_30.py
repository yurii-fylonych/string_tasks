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
