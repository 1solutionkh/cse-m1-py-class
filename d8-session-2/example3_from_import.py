print("--- Example 3: from ... import and Aliases ---")

from temperature import celsius_to_fahrenheit, celsius_to_kelvin
import temperature as temp

try:
    c = float(input("Enter temperature in Celsius: "))

    print("\nUsing 'from ... import':")
    print(f"{c}C = {celsius_to_fahrenheit(c)}F")
    print(f"{c}C = {celsius_to_kelvin(c)}K")

    print("\nUsing alias 'temp':")
    f = float(input("Enter temperature in Fahrenheit: "))
    print(f"{f}F = {temp.fahrenheit_to_celsius(f)}C")

except ValueError:
    print("Error: Please enter a valid number.")
