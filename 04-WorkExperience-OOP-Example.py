# Let's calculate how many years of work experience our employees have

# We need current year info

from datetime import datetime

current_time = datetime.now() # 2024-01-16 22:32:16.956803

current_year = current_time.year

print(current_year) # 2024


class Employee:
    def __init__(self, name, start_year):
        self.name = name
        self.start_year = start_year
        
    def calculate_work_experience(self):
        work_experience = current_year - self.start_year
        print(f"Employee {self.name} has {work_experience} years of work experience.")

# Create an employee

department_it_bilge = Employee("Bilge", 2008)

department_it_bilge.calculate_work_experience() # Employee Bilge has 16 years of work experience.
