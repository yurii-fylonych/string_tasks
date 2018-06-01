# 1

a = 'qwerty'

for i in range(3):
    if i == 2:
        print(a)
    else:
        print(a, end=', ')


# 2

a = 'qwertyu'

k = len(a)
m = int(k / 2)

if k % 2 == 0:
    print(a[0: k: k - 1])
else:
    print(a[0: k: m])

# 3

a = 'qwer'

k = len(a)

if k <= 5:
    for i in range(k + 1):
        print(a[0], end=' ')

else:
    print(a[0: 3], a[k - 3: k])
