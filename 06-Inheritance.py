# parent class

class Worker:
    def __init__(self, name, lastname, id):
        self.name = name
        self.lastName = lastname
        self.id = id

    def work(self):
        print('I am working')

    def rest(self):
        print('I am resting')

# child class

class Director(Worker):
    def __init__(self, name, lastname, id, department_name):
        self.department_name = department_name
        Worker.__init__(self, name, lastname, id)
         
    def direct(self):
        print(f"I'm director of {self.department_name}.")   

# create objects

worker_bilge = Worker("Bilge", "Kutluk", 22)

print(worker_bilge.name) # Bilge

worker_bilge.work() # I am working

director_mustafa = Director("Mustafa", "Gokturk", 22, "Future innovations")

print(director_mustafa.lastName)    # Gokturk  

director_mustafa.direct() # I'm director of Future innovations.     
