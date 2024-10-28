from flask import Flask

app = Flask(__name__)

@app.route('/')
def gallery():

    return f'''
    <h1>Mordern Humans VS Old Humans Gallery</h1>
    <div style="display: flex; justify-content:space-evenly;">
        <img src="static/1.png" alt="Image" style="width: 30%; height: auto;">
        <img src="static/2.png" alt="Image" style="width: 30%; height: auto;">
        <img src="static/3.png" alt="Image" style="width: 30%; height: auto;">
    </div>
    '''

if __name__=='__main__':
    app.run(debug=True)