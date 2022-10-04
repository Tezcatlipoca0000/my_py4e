# Lesson 10 Yet another chapter on iteration (patterns II)

x = [1, 58, 8, 91, 72, 14]

# Count
count = 0
print('Count')
print('Before', count)
for num in x :
    count = count + 1
    print(count, num)
print('After', count)

# Sum
sum = 0
print('Sum')
print('Before', sum)
for num in x :
    sum = sum + num
    print(sum, num)
print('After', sum)

# Average 
count = 0
sum = 0
print('Average')
print('Before', count, sum)
for num in x :
    count = count + 1
    sum = sum + num
    print(count, sum, num)
print('After', count, sum, sum / count)

# filter
print('filtering')
for num in x :
    if num > 20 :
        print('filtered', num)

# Searching
found = False
print('Search')
print('Before', found)
for num in x :
    if num == 8:
        found = True
        print('found my love')
    print('found?', found, num)
print('After', found)

# smallest value
smallest = None
print('Smallest')
print('Before', smallest)
for num in x :
    if smallest is None :
        smallest = num
    elif num < smallest :
        smallest = num
    print(smallest, num)
print('After', smallest)

# is and is not operators
print(' "is" is stronger that "==" ')
print(' 0 == 0.0 ', 0 == 0.0)
print(' 0 is 0.0 ', 0 is 0.0)
print('use "is" for boolean and none types only')