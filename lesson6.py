# Lesson 6 Defined functions

# Void (non-fruitful) function does not return a value
def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')

greet('es')
greet('fr')
greet('en')

# Fruitful functions return a value
def greets(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

print(greets('es'))
print(greets('fr'))
print(greets('en'))

# experimentation

print('begin experimentation... ')

x = greet('es') # function gets invoked here (prints 'Hola')
y = greets('es')
print('1', x, y) # x == None

a = greet() # Traceback error: missing 1 req. arg. program exits here
b = greets()
print('2', a, b)