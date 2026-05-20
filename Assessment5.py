# 1. Check if a person is eligible to vote
age = int(input("Enter your age: "))
print("Eligible to vote!" if age >= 18 else "Not eligible to vote.")

# 2. Grade calculator based on marks
marks = int(input("\nEnter your marks (0-100): "))
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
else:
    grade = "C"
print(f"Grade: {grade}")

# 3. Simulate a traffic light
light = input("\nEnter traffic light color (Red/Yellow/Green): ").strip().lower()
if light == "red":
    print("Stop!")
elif light == "yellow":
    print("Wait!")
elif light == "green":
    print("Go!")
else:
    print("Invalid color!")

# 4. ATM withdrawal check
balance = float(input("\nEnter your balance: "))
amount = float(input("Enter withdrawal amount: "))
if amount <= balance:
    balance -= amount
    print(f"Withdrawal successful! Remaining balance: {balance}")
else:
    print("Insufficient balance!")

# 5. Check if a number is positive, negative, or zero
num = int(input("\nEnter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# 6. Check if a number lies within a given range
n = int(input("\nEnter a number: "))
low = int(input("Enter lower range: "))
high = int(input("Enter upper range: "))
if low <= n <= high:
    print(f"{n} is within range {low} to {high}")
else:
    print(f"{n} is outside range {low} to {high}")

# 7. Username & password verification
username = "admin"
password = "1234"
u = input("\nEnter username: ")
p = input("Enter password: ")
if u == username and p == password:
    print("Login successful!")
else:
    print("Invalid username or password!")

# 8. Electricity bill calculator
units = int(input("\nEnter units consumed: "))
if units <= 100:
    bill = units * 1.5
elif units <= 300:
    bill = 100 * 1.5 + (units - 100) * 2.5
else:
    bill = 100 * 1.5 + 200 * 2.5 + (units - 300) * 4.0
print(f"Electricity bill: ₹{bill:.2f}")

# 9. Simple calculator
a = float(input("\nEnter first number: "))
op = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))
if op == "+":
    print(f"Result: {a + b}")
elif op == "-":
    print(f"Result: {a - b}")
elif op == "*":
    print(f"Result: {a * b}")
elif op == "/":
    print(f"Result: {a / b}" if b != 0 else "Cannot divide by zero!")
else:
    print("Invalid operator!")

# 10. Check type of triangle
s1 = int(input("\nEnter side 1: "))
s2 = int(input("Enter side 2: "))
s3 = int(input("Enter side 3: "))
if s1 == s2 == s3:
    print("Equilateral Triangle")
elif s1 == s2 or s2 == s3 or s1 == s3:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")