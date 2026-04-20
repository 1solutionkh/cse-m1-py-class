print("--- Save Student Records ---")

num_students = int(input("How many students to add? "))

with open("students.txt", "a") as file:
    for i in range(num_students):
        print(f"\nStudent {i + 1}")
        name = input("Enter name: ")
        age = input("Enter age: ")
        grade = input("Enter grade: ")

        file.write(f"Name: {name}, Age: {age}, Grade: {grade}\n")

print("\nAll records saved to students.txt")

print("\n--- Current Records ---")
try:
    with open("students.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("No records found yet.")
