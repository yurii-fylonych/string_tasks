# 31

string = '1234567'

k = int(input())

string_without_el = string[:k - 1] + string[k:]

print(string_without_el)


# 32

first_string = '1234567'
second_string = '4335'

if len(first_string) > len(second_string):
    result = first_string.find(second_string)
else:
    result = second_string.find(first_string)

if result == -1:
    print('First string does not include second string')
else:
    print('First string includes second string')


# 33

first_string = '1234567'
second_string = '1234'
condition = True

for letter in second_string:
    if letter in first_string:
        condition = True
    else:
        condition = False
        break

if condition == True:
    print('Yes, using words from first string it is possible create second')
else:
    print('Cry, it is impossible')