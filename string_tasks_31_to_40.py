# 31

string = '1234567'

k = int(input())

string_without_el = string[:k - 1] + string[k:]

print(string_without_el)