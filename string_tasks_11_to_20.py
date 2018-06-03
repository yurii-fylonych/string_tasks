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

# 14.1

string = '123kjlakjaslda1'
digit = '0123456789'
n = 0

for i in range(len(string)):
    if string[i] in digit:
        n += 1

# 14.2

string = '123kjlakjaslda1'
n = 0

for char in string:
    if char.isdigit() == True:
        n += 1

print(n)

# 15.1

string = 'aaaadasd'

condition = True

for i in string:
    if i != ('a' or 'b' or 'c'):
        condition = False

if condition == False:
    print('Either char located in string')
else:
    print('String contain only a, b, c chars')

# 15.2.

string = 'aaaaaee3'

condition = True
i = 0

while i < len(string):
    if string[i] != ('a' or 'b' or 'c'):
        condition = False
        break
    i += 1

if condition == False:
    print('Either char located in string')
else:
    print('String contain only a, b, c chars')

# 15.3

string = 'aaaaae3'
string_abc = 'abc'

result = set(string).difference(string_abc)

if bool(result):
    print('Either char located in string')
else:
    print('String contain only a, b, c chars')


# 16

string = 'basdj4word8dbword4'

changed_string = string .replace('word', 'letter')

print(changed_string)

"""If only one word need to change you can use code located below"""

string = 'I like to use only polite words'

location = string.find('words')
n = len('words')

changed_lst = string[:location] + 'letters' + string[(location + n):]

# 17.1

string = 'xabcx aa abc aabcx'
abc = 'xabc'

changed_string = string.replace(abc, 'x')

print(changed_string)

# 17.2

'''If remove only one letter'''

string = 'basabcdj4word8dbwxxxord4'
abc = 'abc'
k = string.find(abc)

changed_string = string[:k] + string[k:].replace('x','')

print(changed_string)


# 17.3

string = 'abxabcldxabclka;sdabagkjfdjaba'

lst = list(string)

for index, item in enumerate(lst):
    k = ['a', 'b', 'c']
    if item == 'x' and lst[index + 1: index + 4] == k:
        lst.remove(lst[index])

changed_string = ''.join(lst)

print(changed_string)

# 18.1

string = '3 abcabcab abc3 abc abc3'

for index, char in enumerate(string):
    if char.isdigit() == True:
        if string[index - 3: index] == 'abc':
            result = string.replace('abc' + char, char)

print(result)

# 18.2.

string = 'abxabc3dlabc33333'
digit = '0123456789'
lst = list(string)
index = 0

while index < len(lst):
    k = ['a', 'b', 'c']
    if lst[index] in digit:
        if lst[index - 3: index] == k:
            del lst[index - 3: index]
            index -= 3
    index += 1

new_string = ''.join(lst)
print(lst)