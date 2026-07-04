#Multiple Inheritance 
'''class Father:
    def __init__(self, father_name):
        self.father_name = father_name


class Mother:
    def __init__(self, mother_name):
        self.mother_name = mother_name


class Child(Father, Mother):
    def __init__(self, father_name, mother_name, child_name):
        Father.__init__(self, father_name)
        Mother.__init__(self, mother_name)

        self.child_name = child_name

    def show_details(self):
        print("Father Name:", self.father_name)
        print("Mother Name:", self.mother_name)
        print("Child Name:", self.child_name)


c = Child("Ramesh", "Sita", "Deepak")
c.show_details()'''


#Hierarchical Inheritance
'''class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def show_dog(self):
        print("Dog Name:", self.name)
        print("Dog Breed:", self.breed)


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def show_cat(self):
        print("Cat Name:", self.name)
        print("Cat Color:", self.color)


d = Dog("Bruno", "Labrador")
d.show_dog()

c = Cat("Kitty", "White")
c.show_cat()'''


#5. Hybrid Inheritance 
class A:
    def __init__(self, a_value):
        self.a_value = a_value


class B(A):
    def __init__(self, a_value, b_value):
        super().__init__(a_value)
        self.b_value = b_value


class C(A):
    def __init__(self, a_value, c_value):
        super().__init__(a_value)
        self.c_value = c_value


class D(B, C):
    def __init__(self, a_value, b_value, c_value, d_value):
        B.__init__(self, a_value, b_value)
        C.__init__(self, a_value, c_value)

        self.d_value = d_value

    def show_details(self):
        print("A Value:", self.a_value)
        print("B Value:", self.b_value)
        print("C Value:", self.c_value)
        print("D Value:", self.d_value)


obj = D(10, 20, 30, 40)
obj.show_details()