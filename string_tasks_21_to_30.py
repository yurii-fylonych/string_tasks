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

