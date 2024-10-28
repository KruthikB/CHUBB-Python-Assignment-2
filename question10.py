from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def temperature_converter():
    fahrenheit = None
    if request.method == 'POST':
        celsius = request.form.get('celsius')
        
        if celsius:  
            fahrenheit = (float(celsius) * 9/5) + 32
        else:
            fahrenheit = "Please enter a valid temperature in Celsius."

    return render_template('question10.html', fahrenheit=fahrenheit)

if __name__ == '__main__':
    app.run(debug=True)
