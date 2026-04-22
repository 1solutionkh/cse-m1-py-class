class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.grades = []

    def add_grade(self, subject, score):
        self.grades.append({"subject": subject, "score": score})

    def average(self):
        if not self.grades:
            return 0
        total = sum(g["score"] for g in self.grades)
        return total / len(self.grades)

    def show_info(self):
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Average: {self.average():.2f}")


student1 = Student("Sathya", 20, "S001")
student1.add_grade("Math", 85)
student1.add_grade("Python", 92)
student1.add_grade("English", 78)

student1.show_info()
