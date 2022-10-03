# Lesson 2
# Operators and some built-in functions
a = 1 + 1 # addition
b = 1 - 1 # substraction
c = 2 * 2 # multiplication
d = 4 / 2 # division
e = 4 ** 2 # exponentiation
f = 4 % 2 # remainder
g = 4 // 2 # floored (integer) division (the res. from a div, an int. truncated down)
y = x + 5.5 
z = 'string' 
w = '123'

# function type
# gives the type of variable
print(type(x)) # int
print(type(y)) # float
print(type(z)) # str

# function int
# forces variable to be an integer
print(int(y)) # outputs 15 meaning the result got rounded down
print(int(w)) # converts string to int only if string contains numbers

# function float
# forces variable to be a float number
print(float(x)) # 10.0
print(float(y)) # 15.5

# function input
# waits for user input gives back a string
inp = input('What is your name? ')
print('Hello', inp)