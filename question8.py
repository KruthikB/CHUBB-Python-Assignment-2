from flask import Flask,render_template,request

app = Flask(__name__)

feedback_list = []
@app.route('/',methods=['POST','GET'])
def feedback_submission(): 

    if(request.method=='POST'):
        name = request.form.get('name')
        feedback = request.form.get('feedback')

        user_feedback={'name': name, 'feedback': feedback}

        feedback_list.append(user_feedback)

    return render_template('question8.html',feedback_list=feedback_list)

if __name__ == '__main__':
    app.run(debug=True)