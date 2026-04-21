print("--- Example 4: Using a Package ---")

from mypackage import calculator, string_utils

print("\n--- Calculator module ---")
print("5 + 3 =", calculator.add(5, 3))
print("10 - 4 =", calculator.subtract(10, 4))
print("6 * 7 =", calculator.multiply(6, 7))
print("20 / 4 =", calculator.divide(20, 4))

print("\n--- String Utils module ---")
text = input("\nEnter a word or sentence: ")
print("Uppercase:    ", string_utils.to_upper(text))
print("Lowercase:    ", string_utils.to_lower(text))
print("Reversed:     ", string_utils.reverse(text))
print("Vowel count:  ", string_utils.count_vowels(text))
