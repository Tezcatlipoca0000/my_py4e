# Lesson 15 python lists (collection | list == Array)

friends = ['Arnold', 'Bob', 'Chuck']
print('the collection', friends)
for friend in friends :
    print(friend)

print('the range function', range(5))
for i in range(len(friends)) :
    print('iteration', i)
    print('friend', friends[i])

# list are mutable unlike string
friends[1] = ['Benjamin', 'Barney']
print(friends)