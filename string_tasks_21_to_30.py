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
