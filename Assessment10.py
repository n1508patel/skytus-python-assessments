# 1. Car Class
class Car:
    def __init__(self, brand, model, speed):
        self.brand = brand
        self.model = model
        self.speed = speed

    def accelerate(self):
        self.speed += 10
        print("Speed after acceleration:", self.speed)

    def brake(self):
        self.speed -= 10
        print("Speed after brake:", self.speed)


c1 = Car("Toyota", "Fortuner", 80)
c1.accelerate()
c1.brake()


# 2. BankAccount Class
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Balance after deposit:", self.balance)

    def withdraw(self, amount):
        self.balance -= amount
        print("Balance after withdrawal:", self.balance)


b1 = BankAccount(5000)
b1.deposit(2000)
b1.withdraw(1000)


# 3. Student Class
class Student:
    def __init__(self, marks1, marks2, marks3):
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def average(self):
        avg = (self.marks1 + self.marks2 + self.marks3) / 3
        print("Average Marks:", avg)


s1 = Student(80, 75, 90)
s1.average()


# 4. Rectangle Class
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Area:", self.length * self.width)

    def perimeter(self):
        print("Perimeter:", 2 * (self.length + self.width))


r1 = Rectangle(10, 5)
r1.area()
r1.perimeter()


# 5. Employee Class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee Name:", self.name)
        print("Salary:", self.salary)


e1 = Employee("Jay", 50000)
e1.display()


# 6. Book Class
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)


book1 = Book("Python", "ABC", 450)
book1.display()


# 7. Circle Class
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Area:", 3.14 * self.radius * self.radius)

    def circumference(self):
        print("Circumference:", 2 * 3.14 * self.radius)


c = Circle(7)
c.area()
c.circumference()


# 8. Laptop Class
class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def discount(self, percent):
        final_price = self.price - (self.price * percent / 100)
        print("Price after discount:", final_price)


l1 = Laptop("HP", 60000)
l1.discount(10)


# 9. Flight Class
class Flight:
    def __init__(self, seats):
        self.seats = seats

    def book_seat(self):
        if self.seats > 0:
            self.seats -= 1
            print("Seat booked. Remaining seats:", self.seats)
        else:
            print("No seats available")


f1 = Flight(5)
f1.book_seat()
f1.book_seat()


# 10. Shop Class
class Shop:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def list_products(self):
        print("Products List:")
        for p in self.products:
            print(p)


shop1 = Shop()
shop1.add_product("Mobile")
shop1.add_product("Laptop")
shop1.list_products()