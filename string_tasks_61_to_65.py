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