# Lesson 20 Dictionaries III (loops)

# example: counting words
counter = dict()
line = input('Please enter a line of text: ')
words = line.split()
for word in words :
    counter[word] = counter.get(word, 0) + 1
print(counter)

# definite loops
for key in counter :
    print(key, counter[key])

# list() built-in function
print(list(counter)) # returns a list with all the keys

# keys() method
print(counter.keys()) # returns a list with all the keys

# values() method
print(counter.values()) # returns a list of all values in a list

# ! NOTICE if you run keys and values methods one after the other the order of the results will match  

# items() method
print(counter.items()) # returns a "tuple" a list of key:value pairs

# looping items
for key,value in counter.items() :
    print(key, value)

# example: print the most common word and the frecuency in a text 
# ADVANCED PARSING: notice the import string statement and translate method 
import string # to call string.punctuation
counter = dict()
while True :
    fname = input('Enter a file name: ')
    try :
        fhandle = open(fname)
    except :
        input('File not found.')
        continue
    break
for line in fhandle :
    line = line.translate(line.maketrans('', '', string.punctuation)) # for removing punctuation
    line = line.lower()
    words = line.split()
    for word in words :
        counter[word] = counter.get(word, 0) + 1
bigWord = None
bigCount = None
for key,value in counter.items() :
    if bigCount is None or value > bigCount :
        bigCount = value
        bigWord = key
print(bigWord, bigCount)
