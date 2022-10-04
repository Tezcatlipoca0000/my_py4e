# Lesson 7 Loops and iterations

# break ends the loop
while True :
    line = input('>>> ')
    if line == 'done' :
        break
    print(line)
print('Done!')

# continue ends iteration
while True :
    line = input('>>> ')
    if line[0] == '#' :
        continue
    if line == 'done' :
        break
    print(line)
print('Done!')