from flask import Flask,render_template,redirect
import random

app = Flask(__name__)

quotes =  [
    "Believe you can and you're halfway there. -Theodore Roosevelt",
    "Don't watch the clock; do what it does. Keep going. -Sam Levenson",
    "The only way to do great work is to love what you do. -Steve Jobs",
    "Success is not the key to happiness. Happiness is the key to success. -Albert Schweitzer",
    "Your limitation—it's only your imagination.",
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones.",
    "Dream it. Wish it. Do it.",
    "Don't stop when you're tired. Stop when you're done.",
    "Success doesn't just find you. You have to go out and get it."
]

@app.route("/quote")
def generate_quote():
    quote = random.choice(quotes)
    return f'''
        <h1>Todays Quote:</h1>
        <h2 style='color:red'>{quote}</h2>
    '''

if __name__=='__main__':
    app.run(debug=True)
