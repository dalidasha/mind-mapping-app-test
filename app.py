from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('home.html')

@app.route('/workbench')
def workbench():
    return render_template('workbench.html')

@app.route('/login')
def login():
    return render_template('login.html')


