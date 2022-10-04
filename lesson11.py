# Lesson 11 Strings 

# bracket notation
string = 'banana'
letter = string[1] # a

# len() built-in function
length = len(string) 

# indefinite loop to a string
index = 0
while index < length :
    letter = string[index]
    index = index + 1
    print(letter)

# definite loop
for letter in string :
    print(letter)

# count number of ocurrances in a string
counter = 0
for letter in string :
    if letter == 'a' :
        counter = counter + 1
print(counter)