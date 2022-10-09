# Lesson 18 Python Dictionaries

a = {}
b = dict()
c = {'ana': 1, 'bob': 2, 'clay': 3}
print(a)
print(b)
print(c)
print(dir(b))

a['hello'] = 10
a['next'] = 'who'
a['what'] = 'ok'
print(a)
print(a['what'])

a['hello'] = a['hello'] + 10
a['next'] = 'how'
print(a)