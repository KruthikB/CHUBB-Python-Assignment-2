from flask import Flask, render_template

app = Flask(__name__)

users = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "Los Angeles"},
    {"name": "Charlie", "age": 35, "city": "Chicago"},
    {"name": "Diana", "age": 28, "city": "Houston"}
]

@app.route('/')
def display_table():
    return render_template('question9.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
