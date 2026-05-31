def reverse(s):
    return s[::-1]

def is_palindrome(s):
    return s.lower() == s[::-1].lower()

def count_vowels(s):
    return sum(1 for c in s.lower() if c in "aeiou")

def capitalize_words(s):
    return s.title()