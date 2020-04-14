# Write a Person class with an instance variable, and a constructor that takes an integer,as a parameter.
# The constructor must assign to after confirming the argument passed as is not negative;
# if a negative argument is passed as, the constructor should set to and print Age is not valid, setting age to 0..
# In addition, you must write the following instance methods:

# yearPasses() should increase the instance variable by 1.
# amIOld() should perform the following conditional actions:
# print You are young.. print You are a teenager.. Otherwise, print You are old..

class Person():
    def __init__(self, age):
        if age > 0:
            self.age = age
        else:
            print("Age is not valid ! Age set to 0 again.")
            self.age = 0

    def yearPasses(self):
            print(self.age, "years passed!", self.age + 1, "Running")

    def amIOld(self):
        if self.age <= 12:
            print("You are young")
        elif self.age in range(13, 19):
            print("You are a teenager")
        elif self.age in range(19,61):
            print("You are an adult")
        else:
            print("You are old")

p = Person(int(input("Enter your age : ")))
p.yearPasses()
p.amIOld()
