
#Exploring attribute properties, and various methods to set the values of them
#and exploring 2 different ways which you can do so.

#THIS WILL WORK, BUT ITS NOT 'PYTHONIC'
class Product:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value

#setting an attribute with incorrect properties
try:
    negative_value_product = Product(50)
except ValueError as error:
    print(error)



#NOW LETS DO IT THE PYTHONIC WAY
class PythonicProduct:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value



pyproduct = PythonicProduct(10)

print(pyproduct.price)

pyproduct.price = 100

print(pyproduct.price)
