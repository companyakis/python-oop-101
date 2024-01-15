# Create Car class

class Car:
    def __init__(self, color):
        self.color = color
    
    # Add two methods   
  
    def start(self):
        print("The car was started.")
        
    def stop(self):
        print("The car was stopped.")
        
red_tesla = Car("red")

blue_toyota = Car("blue")

red_tesla.start() # The car was started.

red_tesla.stop() # The car was stopped.

