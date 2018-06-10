# 51

import random

string = 'ab  123123  asdasd'
string_with_signes = ''
k = 'qwertyuiopasdfgfdjhkklj;jzcxvbvcnmn,m,/'

for char in string:
    string_with_signes += char + ''.join([random.choice(k) for x in range(2)])

result = string_with_signes

print(result)


# 52

import random

string = 'It'
digit_letters = '1234567890qwertyuiopasdfghjklzxcvbnm'

individ_char = ''.join(set(string))

if len(individ_char) >= 3:
    random_chars = ''.join(random.sample(individ_char, 3))
    for char in random_chars:
        string = string.replace(char, '', 1)
else:
    char_list = list(string)
    diff_chars = ''.join(set(digit_letters).difference(string))
    random_chars = ''.join(random.sample(diff_chars, 3))
    k = 0
    for i in random_chars:
        random_pos = random.randint(0, len(string) + k)
        char_list.insert(random_pos, i)
        k += 1
        print(char_list)
    string = ''.join(char_list)


# 53

def create_pass(n):
    if n < 8:
        n = 8

    digit = '0123456789'
    letters = 'zxcvbnmasdfghjklqwertyuiop'
    upper_letter = letters.upper()

    sign_for_pass = letters + upper_letter + digit

    return ''.join([random.choice(sign_for_pass) for x in range(n)])

print(create_pass(10))


# 54

import random

def create_pass():
    letters = 'zxcvbnmasdfghjklqwertyuiop'
    digit = '0123456789'
    pass_4_digits = ''.join([random.choice(digit) for x in range(4)])
    pass_2_letters = ''.join(random.sample(letters, 2))
    pass_4_0_1 = ''.join([random.choice('01') for x in range(4)])

    k = pass_4_0_1.find('1')

    if k == -1:
        pass_4_0_1 = ''.join([random.shafle(0, 0, 0, 1)])

    password = pass_4_digits + pass_2_letters + pass_4_0_1

    return password


print(create_pass())

# 55

import random

def create_pass():
    letters = 'zxcvbnmasdfghjklqwertyuiop'
    digit = '02468'
    pass_5_digits = ''.join([random.choice(digit) for x in range(5)])
    pass_5_letters = ''.join([random.choice(letters) for x in range(5)])

    if pass_5_digits.find('8') == -1:
        last_2_sign = 'AB'
    else:
        last_2_sign = 'XY'

    password = pass_5_digits + pass_5_letters + last_2_sign

    return password


print(create_pass())

# 56.2

string = 'It would be   grade if I did not make a mistakes'

words_list = string.split()
len_words = list(map(lambda x: len(x), words_list))

max_len, min_len = max(len_words), min(len_words)
max_index, min_index = len_words.index(max_len), len_words.index(min_len)

words_list[max_index], words_list[min_index] = words_list[min_index], words_list[max_index]

print(' '.join(words_list))
