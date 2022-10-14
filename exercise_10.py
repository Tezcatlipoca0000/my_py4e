# Exercise 10 print most common words

# make a file handler
while True :
    fname = input('Enter the file name or "quit" to exit: ')
    if fname == 'quit' :
        break
    else :
        try :
            fhandle = open(fname)
        except :
            print('Incorrect file name')
            continue
        break

# populate collection of words
import string
coll = dict()
for line in fhandle :
    line = line.lower()
    line = line.translate(line.maketrans('', '', string.punctuation))
    words = line.split()
    for word in words :
        coll[word] = coll.get(word, 0) + 1

# print 5 most common
print('The 5 most used words in your file are:')
for v,k in sorted([(v,k) for k,v in coll.items()], reverse=True)[:5] :
    print(k,v)