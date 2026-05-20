# 1. Print numbers from 1 to 10
print("1 to 10:")
for i in range(1, 11):
    print(i, end=" ")
print()

# 2. Display multiplication table for a given number
n = int(input("\nEnter a number for multiplication table: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# 3. Find factorial of a number
num = int(input("\nEnter a number for factorial: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"Factorial of {num} = {factorial}")

# 4. Generate the first N Fibonacci numbers
n = int(input("\nHow many Fibonacci numbers? "))
a, b = 0, 1
print("Fibonacci:", end=" ")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()

# 5. Check if a number is prime
num = int(input("\nEnter a number to check prime: "))
is_prime = num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))
print(f"{num} is {'Prime' if is_prime else 'Not Prime'}")

# 6. Reverse a number (e.g., 123 → 321)
num = int(input("\nEnter a number to reverse: "))
print(f"Reversed: {int(str(abs(num))[::-1])}")

# 7. Count digits in a number
num = int(input("\nEnter a number to count digits: "))
print(f"Number of digits: {len(str(abs(num)))}")

# 8. Find sum of even numbers between 1-100
total = sum(i for i in range(1, 101) if i % 2 == 0)
print(f"\nSum of even numbers (1-100): {total}")

# 9. Print a pyramid pattern
rows = int(input("\nEnter number of rows for pyramid: "))
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)

# 10. Find all divisors of a number
num = int(input("\nEnter a number to find divisors: "))
divisors = [i for i in range(1, num + 1) if num % i == 0]
print(f"Divisors of {num}: {divisors}")