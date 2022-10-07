# Lesson 13 Reading files

# handler >>> open(filename[, mode]) >>> mode: r = read, w = write
file_handler = open('testing.txt', 'r')
print(file_handler)

# the newline character is \n 
paragraph = 'Hello there \n I am in a new line'
length_is_3 = 'X\nY'
print(paragraph)
print(length_is_3)
print(len(length_is_3))
