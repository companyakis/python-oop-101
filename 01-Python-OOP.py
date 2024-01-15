#Create Car class

class Car:
    def __init__(self, color):
        self.color = color
        
        
red_tesla = Car("red")

blue_toyota = Car("blue")

print(red_tesla) # <__main__.Car object at 0x000001D586024910>

print(red_tesla.color) # red
