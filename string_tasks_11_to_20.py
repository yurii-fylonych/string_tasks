# 11

string = '0qw'

if len(string) > 10:
    b = string[0:6]
else:
    k = int(12 - len(string))
    b = string + k * 'o'


# 12

import random

string = "abcbcaabcaaabbbccc"
divided_string = ''
i = 0
k = 'qweyuuriyweyuropsdf[psdfjlkvnnfd;l13249085-'

while i < len(string) - 1:
    if string[i + 1] != string[i] and string[i + 2]:
        divided_string += string[i] + string[i + 1] + string[i + 2] + ' '
    else:
        while True:
            random_sign = random.choice(k)
            if random_sign != string[i] or string[i + 2]:
                break

        divided_string += string[i] + random_sign + string[i + 2] + ' '
    i += 3

print(divided_string)

# 13

string = 'aaaaajkfsjdabvb'

b = list(string)

for index, item in enumerate(b):
    if index % 2 == 0:
        if item == ('a' or 'b'):
            b[index] = 'c'
        else:
            b[index] = 'a'

changed_string = ''.join(b)
