"""
Example 1: Multiple routes, query parameters, and JSON responses
Run: python3 example1.py
"""
from flask import Flask, request, jsonify

app = Flask(__name__)

books = [
    {"id": 1, "title": "Python Basics", "author": "John Doe", "year": 2020},
    {"id": 2, "title": "Flask Web Dev", "author": "Jane Smith", "year": 2021},
    {"id": 3, "title": "Data Science 101", "author": "Alex Lee", "year": 2022},
]


@app.route("/")
def home():
    return """
    <h1>Library API</h1>
    <ul>
        <li><a href="/books">All books (JSON)</a></li>
        <li><a href="/books/1">Book by ID</a></li>
        <li><a href="/search?author=Jane">Search by author</a></li>
        <li><a href="/stats">Library stats</a></li>
    </ul>
    """


@app.route("/books")
def all_books():
    return jsonify(books)


@app.route("/books/<int:book_id>")
def book_by_id(book_id):
    for book in books:
        if book["id"] == book_id:
            return jsonify(book)
    return jsonify({"error": "Book not found"}), 404


@app.route("/search")
def search():
    author = request.args.get("author", "")
    year = request.args.get("year", type=int)

    results = books
    if author:
        results = [b for b in results if author.lower() in b["author"].lower()]
    if year:
        results = [b for b in results if b["year"] == year]

    return jsonify({"count": len(results), "results": results})


@app.route("/stats")
def stats():
    return jsonify({
        "total_books": len(books),
        "authors": list({b["author"] for b in books}),
        "newest_year": max(b["year"] for b in books),
        "oldest_year": min(b["year"] for b in books),
    })


if __name__ == "__main__":
    app.run(debug=True, port=5001)
