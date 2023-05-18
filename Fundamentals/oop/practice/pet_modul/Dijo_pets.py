class Ninja:
  def __init__(self,first_name,last_name,pet,treats,pet_food):
    self.first_name=first_name
    self.last_name=last_name
    self.pet=pet
    self.treats=treats
    self.pet_food=pet_food
  def walk(self):
    self.pet.play()
  def feed(self):
    self.pet.eat()
  def bathe(self):
    self.pet.noise()
      
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
cat=Pet("lea","seamoi","sleep")
dog=Ninja("John","Doe",cat,"invisibla","pizza")        
dog.feed()
dog.walk()
dog.bathe()
