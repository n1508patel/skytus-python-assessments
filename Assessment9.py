import re

# 1. Handle division by zero error
print(" Division by Zero")
try:
    a = int(input("Enter dividend: "))
    b = int(input("Enter divisor: "))
    print(f"Result: {a / b}")
except ZeroDivisionError:
    print(" Error: Cannot divide by zero!")

# 2. Handle invalid integer input
print("\n Invalid Integer Input")
try:
    num = int(input("Enter a number: "))
    print(f"You entered: {num}")
except ValueError:
    print(" Error: Invalid input! Please enter a number.")

# 3. Open a file and handle file not found error
print("\nFile Not Found")
try:
    with open("missing_file.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print(" Error: File not found!")

# 4. Multiple exception blocks
print("\n Multiple Exceptions ")
try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    result = x / y
    my_list = [1, 2, 3]
    print(f"Result: {result}")
    print(f"List item: {my_list[x]}")
except ZeroDivisionError:
    print(" Cannot divide by zero!")
except ValueError:
    print(" Invalid input!")
except IndexError:
    print(" Index out of range!")

# 5. Use finally for resource cleanup
print("\nFinally Block ")
try:
    with open("sample.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found!")
finally:
    print(" File operation completed (finally block).")

# 6. Custom exception for invalid age
print("\n Custom Exception ")
class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"Age {age} is invalid! Must be 18 or above.")
    print(f" Valid age: {age}")

try:
    age = int(input("Enter your age: "))
    check_age(age)
except InvalidAgeError as e:
    print(f" {e}")

# 7. Handle IndexError when accessing a list
print("\nIndexError")
my_list = [10, 20, 30, 40, 50]
try:
    idx = int(input(f"Enter index (list has {len(my_list)} items): "))
    print(f"Value: {my_list[idx]}")
except IndexError:
    print(" Error: Index out of range!")
except ValueError:
    print(" Error: Please enter a valid number!")

# 8. Take two numbers and handle all possible errors
print("\n Handle All Errors ")
try:
    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))
    print(f"Addition:    {n1 + n2}")
    print(f"Subtraction: {n1 - n2}")
    print(f"Multiply:    {n1 * n2}")
    print(f"Division:    {n1 / n2}")
except ZeroDivisionError:
    print(" Cannot divide by zero!")
except ValueError:
    print(" Invalid input! Enter numbers only.")
except Exception as e:
    print(f" Unexpected error: {e}")

# 9. Log errors to a file instead of printing
print("\n Log Errors to File ")
def log_error(error_msg):
    with open("error_log.txt", "a") as f:
        f.write(error_msg + "\n")

try:
    val = int(input("Enter a number (enter text to cause error): "))
    print(f"You entered: {val}")
except ValueError as e:
    log_error(f"ValueError: {e}")
    print(" Error logged to error_log.txt")

# 10. Validate email format and raise exception
print("\n Email Validation")
class InvalidEmailError(Exception):
    pass

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(pattern, email):
        raise InvalidEmailError(f"'{email}' is not a valid email!")
    return True

try:
    email = input("Enter your email: ")
    validate_email(email)
    print(f" Valid email: {email}")
except InvalidEmailError as e:
    print(f" {e}")

print("\n All Error Handling tasks completed!")