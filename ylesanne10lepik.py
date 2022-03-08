#ylesanne 10
#henri lepik
#08.03.22

import re
e = open('ylesanne10.txt')
for line in e:
    if re.search('^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$', line):
         print(line,end='')

l = open('ylesanne10.txt')
for line in l:
    if re.search('^.*(?=.{8,10})(?=.*[a-zA-Z])(?=.*?[A-Z])(?=.*\d)[a-zA-Z0-9[\]]+$', line):
         print(line,end='')
         