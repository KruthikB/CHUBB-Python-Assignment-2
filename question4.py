from flask import Flask,render_template,request, redirect, url_for

app  = Flask(__name__)

tasks = []

@app.route('/to-do',methods=['GET','POST'])
def todo():
    if(request.method=='POST'):
        task = request.form.get('task')

        if task:
            tasks.append(task)
        return redirect(url_for('todo'))
    return render_template('question4.html',tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
    