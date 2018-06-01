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
lst = []

for i in range(10):
    if i % 2 == 0:
        lst.append(random.choice('0123456789'))
    else:
        lst.append(random.choice('qwertyuiopasdfghjklzxc'))

print(''.join(lst))

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
