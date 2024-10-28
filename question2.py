from flask import Flask, render_template

app = Flask(__name__)

@app.route('/bio')
def bio():
    personal_info = {
        'name': 'Kruthik Ballari',
        'age': 21,
        'hobbies': ['Coding', 'Reading', 'Gaming']
    }
    return render_template('question2.html', info=personal_info)

if __name__ == '__main__':
    app.run(debug=True)
