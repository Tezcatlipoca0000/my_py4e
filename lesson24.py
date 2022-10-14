# Lesson 24 Regexp II

# findall() re method
import re
x = '1 of my 2 favourite numbers are 8 and 7'
y = 'From: more text : whatever@nonsense.com some more text-here'
a = re.findall('[0-9]+', x)
b = re.findall('[AEIOU]', x)
c = re.findall('^F.+:', y)
d = re.findall('^F.+?:', y)
e = re.findall('\S+@\S+', y)
f = re.findall('^From: [a-z]+ [a-z]+ : (\S+@\S+)', y)

print(a) # ['1', '2', '8', '7']
print(b) # []
print(c) # ['From: more text :']
print(d) # ['From:']
print(e) # ['whatever@nonsense.com']
print(f) # ['whatever@nonsense.com']