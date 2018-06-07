# 41

string = '333'

condition = string.isdigit()


if condition == False:
    print('String does not quantity')
else:
    print('String is quantity')


# 42

string = 'ab      aldsdedqweqwqwe   abag   kjtertrertfdjaba'

lst = string.split()

max_len_word = 0
max_word = ''

for word in lst:
    if len(word) > max_len_word:
        max_len_word = len(word)
        max_word = word

print(max_word)

# 43.2

string = '8'

d = {1: 'I',
     2: 'II',
     3: 'III',
     4: 'IV',
     5: 'V',
     6: 'VI',
     7: 'VII',
     8: 'VIII',
     9: 'IX',
     10: 'X'
     }

print(d[int(string)])
