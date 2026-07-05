#Encapsulation code
class Student:
    def __init__(self,name,age,marks):
        self.name=name 
        self._age=age
        self.__marks=marks

    def show_details(self):
        print("Name:",self.name)
        print("Age:",self._age)
        print("Marks:",self.__marks)

    def update_marks(self,new_marks):
        if 0 <= new_marks <= 100:
            self.__marks=new_marks
            print("Marks updated sucessfully")
        else:
            print("Invalid marks")
stu1=Student("Deepak",22,95)
print(stu1.name)
print(stu1._Student__marks)
print(stu1._age)
stu1.show_details()
stu1.update_marks(99)
stu1.show_details()
