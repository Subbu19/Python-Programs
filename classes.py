class Employee:

        def __init__(self, name, number, place):
                self.name = name
                self.number = number
                self.place = place


        def display(self):
                print(self.name)
                print(self.number)
                print(self.place)

        #this is called a a class method.
        @classmethod
        def static_method(cls):
                cls.bu = "Dell Digital"
                return Employee("")

        @staticmethod
        def static_function():
                print("we are in Static method")


e = Employee("Subhash", 24, "Kolar")
print(e.__dict__)
