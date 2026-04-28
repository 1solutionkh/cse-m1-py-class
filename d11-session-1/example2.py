"""
Example 2: Templates with Jinja2 (HTML rendering, loops, conditions)
Run: python3 example2.py
"""
from flask import Flask, render_template

app = Flask(__name__)

students = [
    {"name": "Sathya", "age": 20, "grades": [85, 92, 78], "active": True},
    {"name": "Mary",   "age": 22, "grades": [70, 65, 80], "active": True},
    {"name": "Bob",    "age": 19, "grades": [95, 88, 91], "active": False},
    {"name": "Anna",   "age": 21, "grades": [60, 72, 68], "active": True},
]


@app.route("/")
def home():
    return render_template("home.html", title="Student Portal")


@app.route("/students")
def student_list():
    for s in students:
        s["average"] = sum(s["grades"]) / len(s["grades"])
    return render_template("students.html", students=students)


@app.route("/student/<name>")
def student_detail(name):
    student = next((s for s in students if s["name"].lower() == name.lower()), None)
    if not student:
        return render_template("not_found.html", name=name), 404
    student["average"] = sum(student["grades"]) / len(student["grades"])
    return render_template("student.html", student=student)


if __name__ == "__main__":
    app.run(debug=True, port=5002)
