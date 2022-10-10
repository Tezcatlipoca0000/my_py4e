# Lesson 21 Tuples

# very similar to lists
a = (1, 2, 3)
b = tuple()
print(type(a))
print(a)
print(a[1])
print(max(a))
for v in a :
    print(v)

# but...
try :
    a[1] = 10
except :
    print('tuples are inmutable')
print(dir(a)) # not one mutable method exists (append, sort, reverse, etc. will not work)

# NOTICE: Tuples are MORE EFFICIENT in terms of memory use and performance than lists
# NOTICE: Tuples are preffered over lists for "temporary variables"

# tuples in assignment 
(c, d) = (10, 20)
e, f = 30, 40 # Parentheses are optional
(g, h, i, j) = (41, 42, 43, 44)
print(c)
print(d)
print(e)
print(f)
print(g, h, i, j)

# the items() method returns a list of tuples [ (k,v), (k,v) ]
di = {'hey': 'hello', 'oi': 99}
tu = di.items()
print(tu)
for k,v in tu :
    print(k,v)

# comparison
# checks first value with first value, then second with second, etc.
# if 1st comparison is undetermined(not true nor false) continue
# if comparison returns true or false break
print((0,1,2) < (5,1,5)) # True !!!! NOTICE: 2 is not less than 5 but it never run cause 0 < 5