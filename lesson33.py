# Lesson 33 Objects

class Counter :
    x = 0

    def count(self) :
        self.x = self.x + 1
        print('count:', self.x)

y = Counter()
print('type:', type(y))
print('dir:', dir(y))
y.count()
y.count()

class Counter2 :
    x = 0
    name = ""

    def __init__(self, n) :
        print("I'm just now constructed!", self.x)
        self.name = n
    
    def count(self) :
        self.x = self.x + 1
        print("count:", self.x)

    def __del__(self) :
        print("I'm being destroyed!", self.x)

z = Counter2('z')
z.count()
z.count()
z = 'A new value!'
print("it now has", z)