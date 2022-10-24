# Lesson 34 Inheritance

class PartyAnimal :
    x = 0
    name = ""

    def __init__(self, n) :
        print(n, 'constructed')
        self.name = n
    
    def party(self) :
        self.x = self.x + 1
        print(self.name, "party count:", self.x)
    
class FootballPlayer(PartyAnimal) :
    score = 0

    def touchdown(self) :
        self.score = self.score + 7
        print(self.name, "scored!")
        self.party()
        print(self.name, "score:", self.score, "parties:", self.x)

s = PartyAnimal('Sally')
s.party()

j = FootballPlayer("Joe")
j.party()
j.touchdown()