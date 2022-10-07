# Exercise 7.1 Write a program to read through a file and print the contents of the file (line by line) all in upper case.

while True :
    fname = input('Enter a file name or "quit" to exit >>>')
    if fname == 'quit' :
        break
    try :
        fhand = open(fname)
    except :
        print('error. name invalid.')
        continue
    break

for line in fhand :
    line = line.rstrip()
    print(line.upper())