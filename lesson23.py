# Lesson 23 Regular Expressions

import re
print(re)
print(dir(re))

line1 = 'Mock line of text to iterate and search for values'
print(re.search('search', line1))
x = re.search('search', line1)
if x :
    print('search eval to True')
    print(dir(x))
    print(x.end()) # 39
    print(x.endpos) # 50
    print(x.expand('x')) # x
    print(x.group()) # search
    print(x.groupdict()) # {}
    print(x.groups()) # ()
    print(x.lastgroup) # None
    print(x.lastindex) # None
    print(x.pos) # 0
    print(x.re) # re.compile('search')
    print(x.regs) # ((33, 39),)
    print(x.span()) # (33, 39)
    print(x.start()) # 33
    print(x.string) # Mock line of text to iterate and search for values

y = re.search('^M[a-z]+\s.', line1) #start with 'M' followed by one or more lowercase alphabet-character and one whitespace and one any-character
if y :
    print(y) # <re.Match object; span=(0, 6), match='Mock l'>