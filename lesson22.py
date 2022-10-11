# Lesson 22 Tuples II

# sorted built-in function
a = {'c': 10, 'a': 1, 'b': 2}
b = a.items()
print(b)
b = sorted(b)
print(b)

# sort by value
a = {'c': 10, 'a': 1, 'b': 2}
b = a.items()
c = list()
for k,v in b :
    c.append((v,k))
print(c)
c = sorted(c, reverse=True)
print(c)

# the most common words in a text
fhandle = open('testing.txt')
counts = dict()
for line in fhandle :
    words = line.split()
    for word in words :
        counts[word] = counts.get(word, 0) + 1

lst = list()
for key, val in counts.items() :
    lst.append((val, key))
lst = sorted(lst, reverse=True)
if len(lst) > 2 : print(lst[:3])

# list comprehension
a = {'c': 10, 'a': 1, 'b': 2}
print( sorted( [ (v,k) for k,v in a.items() ] ) )
print( sorted( [ (v,k) for k,v in a.items() ], reverse=True ) )