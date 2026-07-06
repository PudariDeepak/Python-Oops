#Encapsulation of private variable using the getter and setter
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.__marks=marks

    def get_marks(self):
        return self.__marks
    
    def update_marks(self,new_marks):
        if 0 <= new_marks <= 100:
            self.__marks=new_marks
            print("Marks updated successfully")
        else:
            print("Invalid marks Marks must be between 0 and 100")

stu=Student("Cherry",80)

print("Student name is:",stu.name)
print("student marks is :",stu.get_marks())
stu.update_marks(95)
print("updated marks:",stu.get_marks())