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


# 44.2

string = 'loloolo@gmail.ua'

n = len(string)
condition = True

dog_pos = string.find('@')
count_dot = string[dog_pos:].count('.')
dot_pos = string.rfind('.')
login = string[:dog_pos]
company = string[dog_pos + 1: dot_pos]
tail = string[dot_pos + 1:]
len_tail = len(tail)
len_login = len(login)
len_company = len(company)

if len_login < 1 or login[len_login - 1].isalnum() == False:
    condition = False
elif string.count('@') != 1 or string.count(' ') != 0:
    condition = False
elif company.isalpha() == False or len_company == 0:
    condition = False
elif dot_pos == -1 or count_dot != 1 or (dog_pos - dot_pos) == 1:
    condition = False
elif len_tail < 2  or tail.isalpha() == False:
    condition = False
else:
    condition = True


if condition == True:
   print('Correct email')
else:
    print('Try again')
