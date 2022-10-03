# Lesson 4 More conditional structures

# elif
x = 5
if x > 5:
    print('too bad')
elif x > 0:
    print('elif 1')
elif x < 0:
    print('elif 2')
else:
    print('else')

# try / except
number = input('Enter a digit please: ')
try:
    digit = float(number)
except:
    digit = -1
if digit > 0:
    print('Thank you!')
elif digit == -1:
    print('Bad!')