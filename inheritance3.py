#Inheritance problem with the multilevel inheritance
'''class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
    
    def person_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Employee(Person):
    def __init__(self,name,age,salary,emp_id):
        super().__init__(name,age)
        self.salary = salary 
        self.emp_id = emp_id 
    
    def employee_details(self):
        print(f"Salary:{self.salary}")
        print(f"Employee id: {self.emp_id}")

class Manager(Employee):
    def __init__(self,name,age,salary,emp_id,department):
        super().__init__(name,age,salary,emp_id)
        self.department = department

    def manager_details(self):
        print(f"Department: {self.department}")

m = Manager("Cherry",22,250000,101,"Sales")
m.person_details()
m.employee_details()
m.manager_details()'''

#Inheritance problem on the multiple inheritance
class Camera:
    def __init__(self,pixels):
        self.pixels = pixels 

    def photo(self):
        print("Taking a Photo")
    
class Music:
    def __init__(self,storage):
        self.storage = storage 
    
    def music(self):
        print("Listening a Music.")

class SmartPhone(Camera,Music):
    def __init__(self,pixel,storage,brand):
        Camera.__init__(self,pixel)
        Music.__init__(self,storage)
        self.brand = brand 
    
    def info(self):
        print(f"Brand: {self.brand}")
        print(f"pixels: {self.pixels}")
        print(f"Storage: {self.storage}")

s = SmartPhone(101,256,"Vivo")
s.photo()
s.music()
s.info()