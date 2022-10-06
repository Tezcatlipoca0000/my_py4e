# Lesson 12 Strings II

# colon operator
string = 'Hello Bob'
sub1 = string[1:5] # ello
sub2 = string[6:20] # Bob
sub3 = string[:5] # Hello
sub4 = string[6:] # Bob
print(sub1, sub2, sub3, sub4)

# "in" as logical operator
print('H' in string) # True
print('w' in string) # False
if 'ell' in string :
    print('found it!')

# ! check out "string library" for built-in methods for strings
print(dir(string)) # all built in methods of string

# .capitalize() >>> returns a new string with the first letter capitilized
print("hello bob. how are you?".capitalize()) # Hello bob. how are you?

# .center(width[, fillchar]) >>> centers a string in a given width
centered = string.center(50)
centered2 = string.center(50, '*')
print(centered)
print(centered2)

# .endswith(suffix[, start[, end]]) >>> returns boolean
print(string.endswith('ob')) # True
print(string.endswith('lo', 0, 5)) # True
print(string.endswith(' B', 4, 7)) # True

# .find(sub[, start[, end]]) >>> returns first index position of ocurrance in string
print(string.find('Bob')) # 6
print(string.find('o')) # 4 
print(string.find('o', 5)) # 7

# .lstrip([chars]) >>> returns a new str where all specified consecutive characters positioned to the left are removed (default is whitespace)
print('       Hello Bob'.lstrip()) # Hello Bob
print('*********** Hello Bob'.lstrip('*')) #  Hello Bob (notice the extra whitespace)

# .replace(old, new[, count]) >>> returns a new str where 'old' is replaced by 'new' and count refer to the number of ocurrances default is all
print(string.replace('Bob', 'Chuck')) # Hello Chuck
print(string.replace('o', '')) # Hell Bb
print(string.replace('o', '', 1)) # Hell Bob

# .lower() >>> returns a new string with lowercase
lower = string.lower()
print(lower)
print('Hello'.lower())

# .rstrip([chars]) >>> returns a new str where all specified consecutive characters positioned to the right are removed (default is whitespace)
print('Hello Bob          '.rstrip()) # 'Hello Bob'
print('Hello Bob**************'.rstrip('*')) # 'Hello Bob'

# .strip([chars]) >>> returns a new string removing specified char (default is whitespace) from the left and right of the str.
print('      Hello Bob      '.strip()) # 'Hello Bob'
print('*******Hello Bob*******'.strip('*')) # 'Hello Bob'
print('      Hello Bob'.strip()) # 'Hello Bob'
print(' Hello Bob       '.strip()) # 'Hello Bob'

# .upper() >>> returns a new string with all letters in upper case
print(string.upper()) # 'HELLO BOB'

# DOCUMENTATION >>> https://docs.python.org/3/library/stdtypes.html#string-methods