print("--- Example 2: Using a Custom Module ---")

import greetings

print("1. Hello")
print("2. Welcome")
print("3. Goodbye")

choice = input("Choose a greeting (1-3): ")
name = input("Enter your name: ")

if choice == "1":
    print(greetings.say_hello(name))
elif choice == "2":
    place = input("Enter a place: ")
    print(greetings.welcome(name, place))
elif choice == "3":
    print(greetings.say_goodbye(name))
else:
    print("Invalid choice.")
