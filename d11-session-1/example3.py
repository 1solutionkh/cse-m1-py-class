"""
Example 3: Mini To-Do app with forms (POST), sessions, and CRUD
Run: python3 example3.py
"""
from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = "change-this-secret-in-production"

tasks = []
next_id = 1


@app.route("/", methods=["GET", "POST"])
def index():
    global next_id

    if "username" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        priority = request.form.get("priority", "normal")
        if not title:
            flash("Task title cannot be empty.", "error")
        else:
            tasks.append({
                "id": next_id,
                "title": title,
                "priority": priority,
                "done": False,
                "owner": session["username"],
            })
            next_id += 1
            flash(f"Task '{title}' added.", "success")
        return redirect(url_for("index"))

    user_tasks = [t for t in tasks if t["owner"] == session["username"]]
    return render_template("todo.html",
                           tasks=user_tasks,
                           username=session["username"])


@app.route("/toggle/<int:task_id>")
def toggle(task_id):
    if "username" not in session:
        return redirect(url_for("login"))
    for t in tasks:
        if t["id"] == task_id and t["owner"] == session["username"]:
            t["done"] = not t["done"]
            break
    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>")
def delete(task_id):
    if "username" not in session:
        return redirect(url_for("login"))
    global tasks
    tasks = [t for t in tasks
             if not (t["id"] == task_id and t["owner"] == session["username"])]
    flash("Task deleted.", "success")
    return redirect(url_for("index"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        if username:
            session["username"] = username
            flash(f"Welcome, {username}!", "success")
            return redirect(url_for("index"))
        flash("Please enter a username.", "error")
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("username", None)
    flash("Logged out.", "success")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True, port=5003)
