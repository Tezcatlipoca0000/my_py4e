# Lesson 16 List II

# concatenating
a = [1, 2, 3]
b = [4, 5, 6,]
c = a + b
d = b + a 
print(a, b, c, d)

# slicing 
e = a[:1]
f = b[1:]
print(e, f)

# list method
g = list()
print(g)
print(type(g))
print(dir(g))

# append method
g.append('first append')
g.append(99)
g.append(10.15)
print(g)

# logical operators
print(99 in g)
print(100 in g)
print(101 not in g)

# sort
h = [55, 81, 15, 2]
i = ['barney', 'ariel', 'carlos']
# j = ['daniel', 1, 'arnoldo', 0] # TypeError: '<' not supported between instances of 'int' and 'str'
h.sort()
i.sort()
print(h)
print(i)

# built-in functions
print(len(h))
print(max(h))
print(min(h))
print(sum(h))