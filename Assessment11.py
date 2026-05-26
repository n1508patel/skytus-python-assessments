# 1. Animal, Dog and Cat Class
class Animal:
    def sound(self):
        print("Animal makes sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


class Cat(Animal):
    def sound(self):
        print("Cat meows")


d = Dog()
c = Cat()

d.sound()
c.sound()


# 2. Vehicle -> Car -> ElectricCar
class Vehicle:
    def info(self):
        print("This is a vehicle")


class Car(Vehicle):
    def car_info(self):
        print("This is a car")


class ElectricCar(Car):
    def electric_info(self):
        print("This is an electric car")


e1 = ElectricCar()
e1.info()
e1.car_info()
e1.electric_info()


# 3. Method Overriding
class Parent:
    def show(self):
        print("This is parent class")


class Child(Parent):
    def show(self):
        print("This is child class")


obj = Child()
obj.show()


# 4. Multiple Inheritance
class Father:
    def skills1(self):
        print("Father: Driving")


class Mother:
    def skills2(self):
        print("Mother: Cooking")


class Child(Father, Mother):
    def skills3(self):
        print("Child: Coding")


c1 = Child()
c1.skills1()
c1.skills2()
c1.skills3()


# 5. Polymorphism with Shapes
class Rectangle:
    def area(self):
        print("Rectangle Area = Length × Width")


class Circle:
    def area(self):
        print("Circle Area = πr²")


def display_area(shape):
    shape.area()


r = Rectangle()
c = Circle()

display_area(r)
display_area(c)


# 6. Bank System
class BankAccount:
    def display(self):
        print("Bank Account")


class SavingsAccount(BankAccount):
    def interest(self):
        print("Savings Account Interest")


class CurrentAccount(BankAccount):
    def overdraft(self):
        print("Current Account Overdraft Facility")


s = SavingsAccount()
c = CurrentAccount()

s.display()
s.interest()

c.display()
c.overdraft()


# 7. Private Attributes with Getter/Setter
class Student:
    def __init__(self):
        self.__marks = 0

    def set_marks(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks


s1 = Student()
s1.set_marks(85)

print("Marks:", s1.get_marks())


# 8. Teacher and Student Class
class Person:
    def display(self):
        print("This is a person")


class Teacher(Person):
    def teach(self):
        print("Teacher teaches")


class Student(Person):
    def study(self):
        print("Student studies")


t = Teacher()
s = Student()

t.display()
t.teach()

s.display()
s.study()


# 9. MusicPlayer and Spotify
class MusicPlayer:
    def play(self):
        print("Playing music")


class Spotify(MusicPlayer):
    def play(self):
        print("Playing music on Spotify")


sp = Spotify()
sp.play()


# 10. Use of super()
class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def display(self):
        print("Name:", self.name)
        print("Breed:", self.breed)


d1 = Dog("Tommy", "Labrador")
d1.display()