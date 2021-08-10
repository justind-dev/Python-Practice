class Animal:
    def __init__(self):
        self.age = 1
        
    def eat(self):
        print("eat")

# Animal: Parent, Base
# Mammal: Child, Sub
class Mammal(Animal):
    def walk(self):
        print("walk")

# Animal: Parent, Base
# Fish: Child, Sub
class Fish(Animal):

    def swim(self):
        print("swim")

# Define our objects
man = Mammal()
salmon = Fish()

# Check that they inherited parent class methods
man.eat()
salmon.eat()

# Check that they inherited parent class attributes
print(man.age)

# modify attribs
salmon.age = 99

# and finally check
print(salmon.age)