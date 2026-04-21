def to_upper(text):
    return text.upper()

def to_lower(text):
    return text.lower()

def reverse(text):
    return text[::-1]

def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)
