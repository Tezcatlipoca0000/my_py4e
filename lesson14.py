# Lesson 14 Files

print('1') # notice the extra new lines 
fhand = open('testing.txt')
for line in fhand :
    print(line)

print('2') # newline erased by rstrip()
fhand = open('testing.txt')
for line in fhand :
    line = line.rstrip()
    print(line)

print('3') # the whole text is passed to a variable (not recommended for huge files)
fhand = open('testing.txt')
txt = fhand.read()
print(txt)
print('length', len(txt))
print('starts with: ', txt[:20])

print('4') # a counter of lines
fhand = open('testing.txt')
counter = 0
for line in fhand :
    counter = counter + 1
print('num of lines:', counter)

print('5') # using if
fhand = open('testing.txt')
for line in fhand :
    line = line.rstrip()
    if line.startswith('good') :
        print('selected line: ', line)

print('6') # using if not & continue
fhand = open('testing.txt')
for line in fhand :
    line = line.rstrip()
    if not line.startswith('good') :
        continue
    print('selected line: ', line)

print('7') # using in
fhand = open('testing.txt')
for line in fhand :
    line = line.rstrip()
    if 'good' in line :
        print('selected line: ', line)

print('8') # using input
while True :
    fname = input('Please write the file name to read or "quit" to exit >>>')
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
    print(line)