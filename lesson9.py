# Lesson 9 Another chapter on iteration (patterns)

# Find the largest num
x = [1, 8, 42, 71, 15]
largest = 0

for num in x :
    if num > largest :
        largest = num

print("largest", largest)