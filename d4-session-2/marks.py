n = int(input("Enter number of students: "))

students = {}
for i in range(n):
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    students[name] = marks

print("--- Student Marks ---")
for name, marks in students.items():
    print(name, ":", marks)

total = sum(students.values())
average = total / n

print("\nTotal marks:", total)
print("Average marks:", average)
print("Highest:", max(students, key=students.get), "-", max(students.values()))
print("Lowest:", min(students, key=students.get), "-", min(students.values()))
