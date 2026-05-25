# 1. Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1))

num = int(input("Enter a number to check prime: "))
print(f"{num} is {'Prime' if is_prime(num) else 'Not Prime'}")

# 2. Function to reverse a string
def reverse_string(s):
    return s[::-1]

s = input("\nEnter a string to reverse: ")
print(f"Reversed: {reverse_string(s)}")

# 3. Function to find factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

n = int(input("\nEnter a number for factorial: "))
print(f"Factorial of {n} = {factorial(n)}")

# 4. Function to calculate simple interest
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

p = float(input("\nEnter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time in years: "))
print(f"Simple Interest: ₹{simple_interest(p, r, t):.2f}")

# 5. Function to check if a word is palindrome
def is_palindrome(word):
    word = word.lower().replace(" ", "")
    return word == word[::-1]

word = input("\nEnter a word to check palindrome: ")
print(f"'{word}' is {'a Palindrome' if is_palindrome(word) else 'Not a Palindrome'}")

# 6. Function to count vowels in a string
def count_vowels(s):
    return sum(1 for c in s.lower() if c in "aeiou")

s = input("\nEnter a string to count vowels: ")
print(f"Number of vowels: {count_vowels(s)}")

# 7. Function to merge two lists
def merge_lists(l1, l2):
    return l1 + l2

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(f"\nMerged list: {merge_lists(list1, list2)}")

# 8. Function to find GCD of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a = int(input("\nEnter first number for GCD: "))
b = int(input("Enter second number for GCD: "))
print(f"GCD of {a} and {b} = {gcd(a, b)}")

# 9. Function to find area of rectangle
def area_rectangle(length, width):
    return length * width

l = float(input("\nEnter length of rectangle: "))
w = float(input("Enter width of rectangle: "))
print(f"Area of rectangle: {area_rectangle(l, w)}")

# 10. Function to check Armstrong number
def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    return n == sum(int(d) ** power for d in digits)

n = int(input("\nEnter a number to check Armstrong: "))
print(f"{n} is {'an Armstrong' if is_armstrong(n) else 'Not an Armstrong'} number")