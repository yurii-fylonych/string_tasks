import random

# 1

string = 'qwerty'

for i in range(3):
    if i == 2:
        print(string)
    else:
        print(string, end=', ')


# 2

string = 'qwertyu'

k = len(string)
m = int(k / 2)

if k % 2 == 0:
    print(string[0: k: k - 1])
else:
    print(string[0: k: m])

# 3

string = 'qwer'

k = len(string)

if k <= 5:
    for i in range(k + 1):
        print(string[0], end=' ')

else:
    print(string[0: 3], string[k - 3: k])

# 4

string = 'qwejasd3qd'
result = ''

for i in range(10):
    if i % 2 == 0:
        result += random.choice('0123456789')
    else:
        result += random.choice('qwertyuiopasdfghjklzxc')

print(result)


# 5

string = 'qweqjjflsdjflsfjgdf'
k = len(string)

for i in range(k):
    if string[i] == string[k - 1]:
        print(i)

# 6

string = 'qweqjjflsdjflsfjgdf'
k = len(string)

print(string[3: k: 3])


# 7

string = '0qweqjjf+0ls+dj0f+lsf+jgdf'
n = 0
z = 0

for i in range(len(string)):
    if string[i] == ('+' or '-'):
        n += 1
        if string[i + 1] == '0':
            z += 1

print(n, z)

# 8

string = '0qweqjjf+yls+xdyj0fxx+lsf+jgwdf'

i = 0

if 'x' not in string:
    print('x is absent in your list')
if 'w' not in string:
    print('w is absent in your list')

while i < len(string):
    if string[i] == 'x':
        print('Char', string[i], 'was found earlier')
        break
    if string[i] == 'w':
        print('Char', string[i], 'was found earlier')
        break
    i += 1
