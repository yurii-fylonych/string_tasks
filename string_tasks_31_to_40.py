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



# 34


first_string = 'abs  123123'
second_string = 'ab3as  3'

condition = True

for char in second_string:
    n = second_string.count(char)
    if n == 2:
        condition = True
    elif n == 1 and first_string.find(char) != -1:
        condition = True
    else:
        condition = False
        break

if condition == True:
    print('Yes you can')
else:
    print('Do not regret. In next time you will be more lucky')



# 35.2

string = '12345ds673sdfs3'

for char in string:
    if char.isdigit():
        string = string.replace(char, '')

print(string)


# 36.1

string = '12345ds6!73sdfs3'

string.replace('!', '')


# 37


string = 'ab   aldlka;sd   abag   kjfdjaba'

lst = string.split()
string_without_several_spaces = ' '.join(lst)

print(string_without_several_spaces)


# 38.1

string = '1 23 45 ds6! 73sdf s3'

list_of_words = string.split(' ')

number_words = len(list_of_words)

print(number_words)



# 39

string = '1 23 45 ads6! 73sdbbf s3'

string_b_after_a = ''

for char in string:
    string_b_after_a += char
    if char == 'a':
        string_b_after_a += 'b'

print(string_b_after_a)


# 40

first_string = '1 23 45 ads6! 73sdb23bf s3'
second_string = '23'

result = first_string.replace(second_string, '', 1)
print(result)