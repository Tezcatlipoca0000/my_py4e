# Lesson 17 Lists & Strings

# split() method
abc = 'With three words'
list1 = abc.split()
print(list1)
print(len(list1))
print(list1[1])
for w in list1 :
    print(w)

# split default is to remove all white-space 
abc2 = 'A lot          of spaces'
list2 = abc2.split()
print(list2) # All spaces are deleted

# you can specify which delimiter
abc3 = 'One;Two;three'
list3 = abc3.split()
list4 = abc3.split(';')
print(list3) # One item in list
print(list4) # Three items list

# common way of reading files
fhandle = open('testing.txt')
for line in fhandle :
    line = line.rstrip()
    if 'good' in line :
        words = line.split()
        print(words[1])