# single inheritance 
'''class Animal:
    def __init__(self, name):
        self.name = name

    def show_animal(self):
        print("Animal Name:", self.name)


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def show_dog(self):
        print("Dog Breed:", self.breed)


d = Dog("Bruno", "Labrador")
d.show_animal()
d.show_dog()'''


#multi-level inheritance
class Grandparent:
    def __init__(self, gp_name):
        self.gp_name = gp_name


class Parent(Grandparent):
    def __init__(self, gp_name, parent_name):
        super().__init__(gp_name)
        self.parent_name = parent_name


class Child(Parent):
    def __init__(self, gp_name, parent_name, child_name):
        super().__init__(gp_name, parent_name)
        self.child_name = child_name

    def show_details(self):
        print("Grandparent Name:", self.gp_name)
        print("Parent Name:", self.parent_name)
        print("Child Name:", self.child_name)


c = Child("Raju", "Ramesh", "Deepak")
c.show_details()
print(c.child_name)
print(c.p_name)