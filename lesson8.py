# Lesson 8 Definite loop

x = [5, 4, 3, 2, 1]
y = 'Hello'

for i in x :
    print(i)

for j in y :
    print(j)

for i in ['hi', 'hello'] : 
    print(i)

try :
    print(i)
except :
    print('no i') # no except trigered means i exist outside local scope CAREFUL NOT TO OVERWRITE