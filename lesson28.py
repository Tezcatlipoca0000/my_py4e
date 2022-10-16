# Lesson 28 Networking III urllib

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand :
    line = line.decode()
    line = line.strip()
    print(line)


fhand2 = urllib.request.urlopen('https://www.dr-chuck.com/page1.htm')
for line in fhand2 :
    line = line.decode()
    line = line.strip()
    print(line)