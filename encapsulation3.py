#This program demonstrates encapsulation, inheritance, 
#private, protected, and public members in a simple Student 
#Management System.
# Parent Class
class Student:
    def __init__(self, student_id, name, course, marks):
        self.__student_id = student_id      
        self.name = name                    
        self._course = course              
        self.__marks = marks                

    def get_student_id(self):
        return self.__student_id

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid Marks! Marks should be between 0 and 100.")

    def get_marks(self):
        return self.__marks

    def _display_course(self):
        print("Course     :", self._course)


    def display_details(self):
        print("\nStudent Details")
        print("-" * 30)
        print("Student ID :", self.get_student_id())
        print("Name       :", self.name)
        print("Course     :", self._course)
        print("Marks      :", self.get_marks())


# Child Class
class Result(Student):

    def show_result(self):
        print("\nResult")
        print("-" * 30)

        print("Course     :", self._course)
        
        self._display_course()

        if self.get_marks() >= 35:
            print("Status     : Pass")
        else:
            print("Status     : Fail")

student = Result(101, "Deepak", "Data Science", 80)

student.set_marks(95)
student.display_details()
student.show_result()