import random
import datetime
import math
import os

# 1. Create a custom math module and import it
import my_math
print("  Custom Math Module ")
print(f"Add:      {my_math.add(10, 5)}")
print(f"Subtract: {my_math.subtract(10, 5)}")
print(f"Multiply: {my_math.multiply(10, 5)}")
print(f"Divide:   {my_math.divide(10, 5)}")
print(f"Power:    {my_math.power(2, 8)}")

# 2. Create a module to perform string operations
import my_strings
print("\n  String Operations Module ")
print(f"Reverse:    {my_strings.reverse('Python')}")
print(f"Palindrome: {my_strings.is_palindrome('madam')}")
print(f"Vowels:     {my_strings.count_vowels('Hello World')}")
print(f"Title:      {my_strings.capitalize_words('hello world')}")

# 3. Use random module to generate 5 random integers
print("\n Random Integers ")
random_nums = [random.randint(1, 100) for _ in range(5)]
print(f"5 Random integers: {random_nums}")

# 4. Use datetime module to display current date and time
print("\n  Current Date and Time")
now = datetime.datetime.now()
print(f"Date: {now.strftime('%d-%m-%Y')}")
print(f"Time: {now.strftime('%H:%M:%S')}")
print(f"Day:  {now.strftime('%A')}")

# 5. Use math module to find factorial
print("\nFactorial using math module ")
n = int(input("Enter a number for factorial: "))
print(f"Factorial of {n} = {math.factorial(n)}")

# 6. Create a package shapes with circle and rectangle
print("\nShapes ")
def circle_area(r):
    return round(math.pi * r ** 2, 2)

def rectangle_area(l, w):
    return l * w

print(f"Circle area (r=7):        {circle_area(7)}")
print(f"Rectangle area (5x10):    {rectangle_area(5, 10)}")

# 7. Import multiple functions from one module
print("\n Multiple Functions from Module ")
from my_math import add, multiply, power
print(f"add(3,4)       = {add(3, 4)}")
print(f"multiply(3,4)  = {multiply(3, 4)}")
print(f"power(2,10)    = {power(2, 10)}")

# 8. Shuffle a list using random module
print("\n Shuffle List ")
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Before shuffle: {my_list}")
random.shuffle(my_list)
print(f"After shuffle:  {my_list}")

# 9. Calculate difference between two dates
print("\n Difference Between Two Dates")
date1 = datetime.date(2003, 9, 15)
date2 = datetime.date.today()
diff = date2 - date1
print(f"Date 1: {date1}")
print(f"Date 2: {date2}")
print(f"Difference: {diff.days} days")

# 10. Use os module to list files in a directory
print("\n List Files in Directory ")
files = os.listdir(".")
print("Files in current directory:")
for f in files:
    print(f"  {f}")

print("\n All Modules & Libraries tasks completed!")