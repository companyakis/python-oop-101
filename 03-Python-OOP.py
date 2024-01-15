# Create Car class

class Car:
    
    # We can add class attributes
  
    price = "0" # Be careful. String!
    
    def __init__(self, color):
        self.color = color
    
    # Add two methods   
  
    def start(self):
        print("The car was started.")
        
    def stop(self):
        print("The car was stopped.")
        
red_tesla = Car("red")

red_tesla.price = int("100000")

print(red_tesla.price) # 100000

blue_toyota = Car("blue")

print(blue_toyota.price) # 0
 
