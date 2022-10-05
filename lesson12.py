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

# .lower()
lower = string.lower()
print(lower)
print('Hello'.lower())

# .capitalize()
print('hello'.capitalize()) # Hello

# .endswith(suffix[, start[, end]])
print(string.endswith('ob')) # True
print(string.endswith('lo', 0, 5)) # True
print(string.endswith(' B', 4, 7)) # True

# .find(sub[, start[, end]])
print(string.find('Bob')) # 6
