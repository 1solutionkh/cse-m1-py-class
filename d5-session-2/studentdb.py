students = {}

n = int(input("How many students? "))

for i in range(n):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    major = input("Enter major: ")
    students[name] = {"age": age, "major": major}

print("\n--- Student Database ---")
for name, info in students.items():
    print(name, "- Age:", info["age"], "- Major:", info["major"])
