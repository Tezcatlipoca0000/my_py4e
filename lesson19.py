# Lesson 19 Dictionaries II (Common Applications)

# if not found referencing will traceback
counts = dict()
names = ['ana', 'bob', 'ana', 'charly']
try :
    print(counts['ana'])
except :
    print('Traceback: keyError')

# Histogram
counts = dict()
names = ['ana', 'bob', 'ana', 'charly']
for name in names :
    if name not in counts :
        counts[name] = 1
    else :
        counts[name] = counts[name] + 1
print(counts) 

# get(key, default) method
counts = dict()
names = ['ana', 'bob', 'ana', 'charly']
for name in names :
    counts[name] = counts.get(name, 0) + 1
print(counts)