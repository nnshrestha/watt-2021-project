from flask import request, render_template
from app import app


@app.route("/",methods =['GET', 'POST'])
def home():
    username = request.form.get('uname', None)
    if username:
        return render_template('index.html', uname=username)
    else:
        return render_template('login.html')


@app.route("/leaderboard")
def leaderboard():
    return "leaderboard here"