class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health =0
        self.energy =0  
    def sleep():
       self.energy+=25
    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"energy{self.energy}")
    def play(self):
        self.health += 5
        print(f"health{self.health}")
    def noise(self):
        print("The pet makes a noise.")