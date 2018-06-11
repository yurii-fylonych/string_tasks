# 61

string = 'c:\WebServers\home\testsite\www\myfile.txt'

pos_slash = string.rfind('\\')
pos_dot = string.rfind('.')

result = string[pos_slash + 1: pos_dot]

print(result)