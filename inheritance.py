class Parent:
    def __init__(self, p_name, p_age):
        self.p_name = p_name
        self.p_age = p_age

    def show_parent(self):
        print(f"Parent Name: {self.p_name}")
        print(f"Parent Age: {self.p_age}")


class Child(Parent):
    def __init__(self, p_name, p_age, child_name, child_age):
        super().__init__(p_name, p_age)  # calls Parent constructor

        self.child_name = child_name
        self.child_age = child_age

    def show_child(self):
        print(f"Child Name: {self.child_name}")
        print(f"Child Age: {self.child_age}")


obj = Child("Ramesh", 45, "Deepak", 20)

obj.show_parent()
obj.show_child()