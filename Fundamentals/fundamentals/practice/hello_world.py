
#1
print("Hello World")
#2a
my_name="Souha Karoui"
print("Hello",my_name,"!")
#2b
my_name="Souha Karoui"
print("Hello "+ my_name +"!")
#3a
num=20
print("Hello",num,"!")
#3b
"""num=20
print("Hello"+ num +"!")"""
# we can only concatenate str to str(not "int")
#Ninja Bonus:
num=20
print("Hello"+str(num)+"!")
#4a
fave_food1= "sushi"
fave_food2 = "pizza"
print("I love to eat {} and {}".format(fave_food1,fave_food2))
#4b
fave_food1= "sushi"
fave_food2 = "pizza"
print(f"I love to eat {fave_food1} and {fave_food2}")
#NINJA BONUS
food_one = "pizza"
food_two = "sushi"
print("I love to eat", food_one, "and", food_two + ".")



"""
class Shoe:
    # now our method has 4 parameters (including self)!
    def __init__(self, brand, shoe_type, price):
    	# we assign them accordingly
        self.brand = brand
        self.type = shoe_type
        self.price = price
        # the status is set to True by default
        self.in_stock = True

skater_shoe = Shoe("Vans", "Low-top Trainers", 59.99)
dress_shoe = Shoe("Jack & Jill Bootery", "Ballet Flats", 29.99)
print(skater_shoe.type)	# output: Low-top Trainers
print(dress_shoe.type)	# output: Ballet Flats
"""
"""
class Shoe:
    # now our method has 4 parameters (including self)!
    def __init__(self, brand, shoe_type, price):
    	# we assign them accordingly
        self.brand = brand
        self.type = shoe_type
        self.price = price
        # the status is set to True by default
        self.in_stock = False
        
        
skater_shoe = Shoe("Nike", "nike_air", 49.99)
print(skater_shoe.type)	
"""