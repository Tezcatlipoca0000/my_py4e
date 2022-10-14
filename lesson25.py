# Lesson 25 Regexp III String parsing examples
# Extract the host

import re
data = 'From something.else@elh.uth.itc Sat Jun Whatever'
# find() method
atpos = data.find('@')
sppos = data.find(' ', atpos)
host = data[atpos+1 : sppos]
print('1',host)

# split() method
words = data.split()
word = words[1].split('@')
host = word[1]
print('2',host)

# the regexp way
host = re.findall('@([^ ]*)', data)
print('3',host[0])

# more precise regexp
host = re.findall('From .*@([^ ]*)', data)
print('4',host[0])