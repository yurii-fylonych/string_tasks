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

if not 'x' in string:
    print('x is absent in your list')
if not 'w' in string:
    print('w is absent in your list')

while i < len(string):
    if string[i] == 'x':
        print('Char', string[i], 'was found earlier')
        break
    if string[i] == 'w':
        print('Char', string[i], 'was found earlier')
        break
    i += 1

# 9

a = '0qweqjjf+yls+xdyj0fxx+lsf+jgdf'
b = 'asdlasl;kd;alskfk;sdkf;sdflf12312321'

k = len(a)
m = len(b)
diff = abs(m - k)

def print_string(string, n):
    for i in range(n):
        print(string)

if k == m:
    print('String a and b have equal number of chars')
elif k < m:
    print_string(b, diff)
else:
    print_string(a, diff)

# 10

string = '0qweqjjf+yls+xdyj0fxx+lsf+jgdf'


if string[0:2] == 'abc':
    changed_string = 'www' + string[2:]
else:
    changed_string = string + 'zzz'

print(changed_string)
