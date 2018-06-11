# 61

string = 'c:\WebServers\home\testsite\www\myfile.txt'

pos_slash = string.rfind('\\')
pos_dot = string.rfind('.')

result = string[pos_slash + 1: pos_dot]

print(result)


# 62

string = 'abcdxs'

word_list = list(string)
list_in_order = sorted(word_list)

i = 0
condition = True

while i < len(word_list) and condition == True :
    if word_list[i] != list_in_order[i]:
        print(word_list[i], end=' ')
        condition = False
    i += 1

if condition == False:
    print('Incorrect alphabet order')
else:
    print('Yes')

# 63

sentance = 'You can cou333nt 221 33 on me like 33 one 222 two 33  555 444 three, i'

def find_max_len(lst):
    max_len_word = lst[0]

    for item in lst:
        if len(item) > len(max_len_word):
            max_len_word = item

    return max_len_word

len_words_list = list(filter(lambda word: word.isdigit(), sentance.split()))

if len(len_words_list) > 0:
    result = find_max_len(len_words_list)
    print(result)
else:
    print('In your text absent numbers')


# 64.1


first_sentance = 'You can count on me like one two three, i'
second_sentance = 'I will be there, And I know when I need it. can '
third_sentance = 'I can count on you like four three two You will be there.'

first_words_list = list(filter(lambda word: word.isalnum(), sentance.lower().split()))

identical_words = list(filter(lambda word: second_sentance.lower().find(word) != -1
                                           and third_sentance.lower().find(word) != -1, first_words_list))

if len(identical_words) > 0:
    max_len_word = identical_words[0]

    for item in identical_words:
        if len(item) > len(max_len_word):
            max_len_word = item
    print(max_len_word)
else:
    print('In you sentance absent identical words')


# 64.2


first_sentance = 'You can count on me like one two three, i'
second_sentance = ' will be there, And I know when  need it. can '
third_sentance = ' count on you like four three two You will be there.'


def correct_sentance(sentance):
    return list(filter(lambda word: word.isalnum(), sentance.lower().split()))


first_words_list = correct_sentance(first_sentance)
second_words_list = correct_sentance(second_sentance)
third_words_list = correct_sentance(third_sentance)

ident_words = list(set(first_words_list).intersection(set(second_words_list)).intersection(set(third_words_list)))

if len(ident_words) > 0:
    max_len_word = ident_words[0]

    for item in ident_words:
        if len(item) > len(max_len_word):
            max_len_word = item
    print(max_len_word)
else:
    print('In you sentance absent identical words')

# 65


sentance = 'You can cou333nt 221 33 on me like 33 one 222 two 33  555 444 three, i'

def remove_words(sentance, n):
    for word in sentance.split():
        if word.isalnum() and sentance.count(word) > n:
            sentance = sentance.replace(word, '')

    return sentance


print(remove_words(sentance, 2))
