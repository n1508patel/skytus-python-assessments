# 1. Write a program to print your name, age, and city in one line
name = "Nistha Patel"
age = 21
city = "Bharuch"
print(f"Name: {name}, Age: {age}, City: {city}")

# 2. Take user input for two numbers and print their sum
a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
print(f"Sum: {a + b}")

# 3. Write a program to convert temperature from Celsius to Fahrenheit
celsius = float(input("\nEnter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")

# 4. Store your name in a variable and print it in uppercase
my_name = "Nistha Patel"
print(f"\nUppercase: {my_name.upper()}")

# 5. Ask the user for their birth year and calculate their current age
birth_year = int(input("\nEnter your birth year: "))
current_age = 2026 - birth_year
print(f"Your age is: {current_age} years")

# 6. Write a program to swap the values of two variables
x = int(input("\nEnter value of x: "))
y = int(input("Enter value of y: "))
print(f"Before swap: x = {x}, y = {y}")
x, y = y, x
print(f"After swap:  x = {x}, y = {y}")

# 7. Create a program to calculate the area of a rectangle from user inputs
length = float(input("\nEnter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
area = length * width
print(f"Area of rectangle: {area}")

# 8. Write a program to check if a number is positive or negative
num = int(input("\nEnter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# 9. Ask for two numbers and print their average
n1 = float(input("\nEnter first number: "))
n2 = float(input("Enter second number: "))
average = (n1 + n2) / 2
print(f"Average: {average}")