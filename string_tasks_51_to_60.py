# 51

import random

string = 'ab  123123  asdasd'
string_with_signes = ''
k = 'qwertyuiopasdfgfdjhkklj;jzcxvbvcnmn,m,/'

for char in string:
    string_with_signes += char + ''.join([random.choice(k) for x in range(2)])

result = string_with_signes

print(result)


# 52

import random

string = 'It'
digit_letters = '1234567890qwertyuiopasdfghjklzxcvbnm'

individ_char = ''.join(set(string))

if len(individ_char) >= 3:
    random_chars = ''.join(random.sample(individ_char, 3))
    for char in random_chars:
        string = string.replace(char, '', 1)
else:
    char_list = list(string)
    diff_chars = ''.join(set(digit_letters).difference(string))
    random_chars = ''.join(random.sample(diff_chars, 3))
    k = 0
    for i in random_chars:
        random_pos = random.randint(0, len(string) + k)
        char_list.insert(random_pos, i)
        k += 1
        print(char_list)
    string = ''.join(char_list)

print()
