class Student:
    def greet(self):
        print("Hello")

stud1 = Student()
stud1.greet()


#Program 26: Create a class and object

class Student:

    def __init__(self, name, age):
        self.name=name
        self.age=age

    def display(self):
        print(self.name)
        print(self.age)


Student = Student("Monika", 24)

Student.display()



#Program 27: Encapsulation

class BankAcc:

    def __init__(self, bal):
        self.__bal = bal

    def get_bal(self):
        return self.__bal
acc = BankAcc(5000)

print(acc.get_bal())

#Program 28: Inheritance

class Animal:

    def speak(self):
        print("Animal Barks")


class Dog(Animal):

    def bark(self):
        print("Barks")


d = Dog()

d.speak()
d.bark()