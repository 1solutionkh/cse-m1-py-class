from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Hello, Flask!</h1><p>Welcome to my first Flask app.</p>"


@app.route("/about")
def about():
    return "<h1>About</h1><p>This is a basic Flask example.</p>"


@app.route("/user/<name>")
def user(name):
    return f"<h1>Hello, {name}!</h1>"


@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return f"<h1>{a} + {b} = {a + b}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
