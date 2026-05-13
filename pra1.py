# 1. Calculate the remainder of two numbers
a=int(input("first no:"))
b=int(input("second no:"))
print(f"Remainder: {a%b}\n")

# 2. Check if a number is even or odd
n = int(input("enter a number:"))
print(f"{n} is {'even' if n%2 == 0 else 'odd'}\n")

# 3. Compare two numbers and print the larger one
x = int(input("first no:"))
y = int(input("second no:"))
print(f"Larger no:{max(x,y)}\n")

# 4. Calculate the square and cube of a number
num = int(input("enter a no:"))
print(f"square: {num ** 2}, cube: {num**3}\3")

# 5. Check if two entered numbers are equal
p = int(input("first no"))
q = int(input("second no:"))
print(f"are they equal ?{p == q}\n")

# 6. Take two numbers and print True if both are positive, else False
a1 =int(input("first no"))
a2 = int(input("second no:"))
print(f"both positive? {a1 > 0 and a2 > 0}")

# 7. Write a program to convert float to integer
f = float(input(" enter a float number: "))
print(f"Converted to int: {int(f)}\n")

# 8. Take a number as string, convert to int, and multiply by 10
s = input("enter a number (as string): ")
print(f"Multiplied by 10: {int(s) * 10}\n")

# 9. Use 'and' & 'or' operators to check multiple conditions
val = int(input("enter a number: "))
print(f"Greater than 0 AND less than 100? {val > 0 and val < 100}")
print(f"Less than 0 OR greater than 100?  {val < 0 or val > 100}\n")

# 10. Divide two numbers and print the quotient and remainder separately
d1 = int(input("enter dividend: "))
d2 = int(input("enter divisor: "))
print(f"Quotient: {d1 // d2}, Remainder: {d1 % d2}")