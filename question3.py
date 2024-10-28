from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/calculator',methods=['POST','GET'])
def calculator():
    result = None
    if(request.method=='POST'):
        try:
            num1 = float(request.form.get('number1'))
            num2 = float(request.form.get('number2'))

            result = num1 + num2
        except (TypeError,ValueError):
            result = "Invalid input. Please enter numeric values."
    return render_template('question3.html',result=result)

if __name__=="__main__":
    app.run(debug=True)

