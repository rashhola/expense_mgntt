##OOp AKA Class, object, methods, inheritance, polymorphism, encapsulation

class car:
    model = "Honda"
    wheels = 4
    color = "red"
my_car = car() #an object is an instatenous of a class
print(f"My car is a {my_car.model}")



class car:
    wheels = 4

#methods are functions defined inside the class. You need to pass in the self atttribute

def __init__(self, model, color):
    self.model = model
    self.color = color 

def display_info(self):
    print("my car is a {self.color} {self.model}")

def change_color(self, color):
    self.color = color

my_car = car(model = "Toyota", color = "blue")
print(my_car.display_info())
my_car.change_color("White")
print(my_car.display_info())


