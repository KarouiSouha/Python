import pet
class Ninja(pet.Pet):
  def __init__(self,first_name,last_name,treats,pet_food,name, type, tricks):
    super().__init__(name, type, tricks)
    self.first_name=first_name
    self.last_name=last_name
    self.treats=treats
    self.pet_food=pet_food
  def walk(self):
    super().play()
  def feed(self):
    super().eat()
  def bathe(self):
    super().noise()
    

    
bird=pet.Pet("ziwziw","canalou","sing")
ninja=Ninja("John","Doe","invisibla","pizza","ziwziw","canalou","sing")
ninja.feed()
ninja.walk()
ninja.bathe()