import os
# Create a sample file for testing
with open("sample.txt", "w") as f:
    f.write("Hello this is Python file handling.\n")
    f.write("File handling is very important.\n")
    f.write("Python makes file handling easy.\n")
    f.write("This is the fourth line.\n")
    f.write("Last line of the file.\n")

# 1. Read a file and display its contents
print(" Read File")
with open("sample.txt", "r") as f:
    print(f.read())

# 2. Count the number of lines in a file
print(" Count Lines")
with open("sample.txt", "r") as f:
    lines = f.readlines()
print(f"Total lines: {len(lines)}")

# 3. Count how many times each word appears
print("\n Word Count")
with open("sample.txt", "r") as f:
    words = f.read().lower().split()
word_freq = {}
for word in words:
    word = word.strip(".,!?")
    word_freq[word] = word_freq.get(word, 0) + 1
for word, count in word_freq.items():
    print(f"  {word}: {count}")

# 4. Write 5 user-entered sentences to a file
print("\nWrite 5 Sentences")
with open("sentences.txt", "w") as f:
    for i in range(1, 6):
        sentence = input(f"Enter sentence {i}: ")
        f.write(sentence + "\n")
print(" Sentences saved to sentences.txt")

# 5. Append a list of strings to an existing file
print("\n Append to File")
new_lines = ["Appended line 1", "Appended line 2", "Appended line 3"]
with open("sample.txt", "a") as f:
    for line in new_lines:
        f.write(line + "\n")
print("Lines appended to sample.txt")

# 6. Read file and print only lines containing a specific word
print("\n Search Word in File")
search = input("Enter word to search in file: ")
with open("sample.txt", "r") as f:
    matched = [line for line in f if search.lower() in line.lower()]
if matched:
    for line in matched:
        print(f"  {line.strip()}")
else:
    print("Word not found!")

# 7. Replace a specific word in a file and save
print("\n=== Task 7: Replace Word ===")
old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")
with open("sample.txt", "r") as f:
    content = f.read()
content = content.replace(old_word, new_word)
with open("sample.txt", "w") as f:
    f.write(content)
print(f" Replaced '{old_word}' with '{new_word}'")

# 8. Merge contents of two files into a third file
print("\nMerge Two Files")
with open("file1.txt", "w") as f:
    f.write("Content from file 1.\nSecond line of file 1.\n")
with open("file2.txt", "w") as f:
    f.write("Content from file 2.\nSecond line of file 2.\n")
with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
    merged = f1.read() + f2.read()
with open("merged.txt", "w") as f:
    f.write(merged)
print(" Files merged into merged.txt")

# 9. Read a CSV file and display in formatted way
print("\n CSV File ")
with open("students.csv", "w") as f:
    f.write("Name,Age,Marks\n")
    f.write("Nistha,21,90\n")
    f.write("Raj,22,85\n")
    f.write("Priya,20,92\n")
with open("students.csv", "r") as f:
    lines = f.readlines()
headers = lines[0].strip().split(",")
print(f"  {headers[0]:<10} {headers[1]:<6} {headers[2]}")
print("  " + "-" * 25)
for line in lines[1:]:
    row = line.strip().split(",")
    print(f"  {row[0]:<10} {row[1]:<6} {row[2]}")

# 10. Backup a file by copying its contents
print("\n Backup File ")
with open("sample.txt", "r") as f:
    content = f.read()
with open("sample_backup.txt", "w") as f:
    f.write(content)
print(" Backup created: sample_backup.txt")

print("/n All File Handling tasks completed!")