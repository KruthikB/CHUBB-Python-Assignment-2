from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == 'user' and password == 'password':
            return f"Welcome, {username}!"
        else:
            return "Invalid credentials, please try again."
    return render_template('question6.html')

if __name__ == '__main__':
    app.run(debug=True)
