# STRING HANDLING 

# 1. Take a string input and print its length
s = input("Enter a string: ")
print(f"Length: {len(s)}")

# 2. Convert a sentence to lowercase
print(f"Lowercase: {s.lower()}")

# 3. Replace spaces with underscores
print(f"Underscores: {s.replace(' ', '_')}")

# 4. Extract the first and last character
print(f"First: {s[0]}, Last: {s[-1]}")

# 5. Reverse a string using slicing
print(f"Reversed: {s[::-1]}")

# 6. Count how many times a letter appears
letter = input("Enter a letter to count: ")
print(f"'{letter}' appears {s.count(letter)} times")

# 7. Check if a word is present in a sentence
word = input("Enter a word to search: ")
print(f"'{word}' found? {word in s}")

# 8. Take name & age and print using f-string
name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"My name is {name} and I am {age} years old.")

# 9. Remove extra spaces from start and end
messy = "   Hello World   "
print(f"Stripped: '{messy.strip()}'")

# 10. Join a list of words with - between them
words = ["Python", "is", "fun"]
print(f"Joined: {'-'.join(words)}")

# DATA STRUCTURES

# 11. Create a list of 5 favorite movies
movies = ["Inception", "Interstellar", "3 Idiots", "KGF", "RRR"]
print(f"\nMovies: {movies}")

# 12. Add a new movie to the list
movies.append("Pushpa")
print(f"After add: {movies}")

# 13. Remove the first movie from the list
movies.pop(0)
print(f"After remove first: {movies}")

# 14. Sort a list of numbers in ascending order
nums = [5, 2, 8, 1, 9, 3]
nums.sort()
print(f"Sorted: {nums}")

# 15. Reverse a list
nums.reverse()
print(f"Reversed: {nums}")

# 16. Find the largest number in a list
print(f"Largest: {max(nums)}")

# 17. Merge two lists into one
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged = list1 + list2
print(f"Merged: {merged}")

# 18. Access the last element without using index number
print(f"Last element: {merged[-1]}")

# 19. Create a nested list and access a specific inner element
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Nested[1][2]: {nested[1][2]}")

# 20. Count how many times an element appears in a list
data = [1, 2, 2, 3, 2, 4, 5]
print(f"2 appears {data.count(2)} times")