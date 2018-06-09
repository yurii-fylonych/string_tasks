# 51

import random

string = 'ab  123123  asdasd'
string_with_signes = ''
k = 'qwertyuiopasdfgfdjhkklj;jzcxvbvcnmn,m,/'

for char in string:
    string_with_signes += char + ''.join([random.choice(k) for x in range(2)])

result = string_with_signes

print(result)
