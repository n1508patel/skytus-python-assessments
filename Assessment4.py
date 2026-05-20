# 1. Create a tuple with 5 numbers
t = (10, 20, 30, 40, 50)
print(f"Tuple: {t}")

# 2. Access the third element in a tuple
print(f"Third element: {t[2]}")

# 3. Unpack a tuple into separate variables
a, b, c, d, e = t
print(f"Unpacked: a={a}, b={b}, c={c}, d={d}, e={e}")

# 4. Create a set of 5 fruits
fruits = {"Apple", "Mango", "Banana", "Grapes", "Orange"}
print(f"\nFruits set: {fruits}")

# 5. Add a new fruit to the set
fruits.add("Pineapple")
print(f"After add: {fruits}")

# 6. Remove an element from a set
fruits.remove("Banana")
print(f"After remove: {fruits}")

# 7. Find union of two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(f"\nUnion: {set1 | set2}")

# 8. Find intersection of two sets
print(f"Intersection: {set1 & set2}")

# 9. Check if one set is subset of another
set3 = {1, 2, 3}
print(f"{set3} is subset of {set1}? {set3.issubset(set1)}")

# 10. Convert a list with duplicates into a set
dup_list = [1, 2, 2, 3, 3, 4, 5, 5]
print(f"Without duplicates: {set(dup_list)}")

# 11. Create a dictionary storing student names and marks
students = {"Nistha": 90, "Raj": 85, "Priya": 92, "Meet": 78}
print(f"\nStudents: {students}")

# 12. Add a new key-value pair
students["Riya"] = 88
print(f"After add: {students}")

# 13. Delete a key-value pair
del students["Meet"]
print(f"After delete: {students}")

# 14. Merge two dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {**dict1, **dict2}
print(f"Merged: {merged}")

# 15. Check if a key exists
key = "Nistha"
print(f"'{key}' exists? {key in students}")

# 16. Count word frequency in a string
sentence = "apple banana apple mango banana apple"
freq = {}
for word in sentence.split():
    freq[word] = freq.get(word, 0) + 1
print(f"Word frequency: {freq}")

# 17. Find the key with maximum value
print(f"Highest marks: {max(students, key=students.get)}")

# 18. Reverse keys and values
reversed_dict = {v: k for k, v in students.items()}
print(f"Reversed: {reversed_dict}")

# 19. Update value for a specific key
students["Nistha"] = 95
print(f"After update: {students}")

# 20. Convert a list of tuples into a dictionary
tuples_list = [("name", "Nistha"), ("age", 21), ("city", "Surat")]
converted = dict(tuples_list)
print(f"Converted: {converted}")