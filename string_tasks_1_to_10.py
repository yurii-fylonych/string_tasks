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
