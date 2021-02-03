from flask import request, render_template, session, redirect, url_for
from app import app
from app.PolyLinear import linearPicker
from app.Points import savePoints, getPoints



@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        if session.get("username", None) == None:
            return redirect("/login")
        x = session.get('x', None)
        ans = request.form.get('ans', None)
        try:
            ans = float(ans)
            if abs(ans - x) < 0.02:
                savePoints(10 + getPoints())
                return linear("correct")
            else:
                return linear("incorrect")
                
        except ValueError:
            return linear("empty")
    elif request.method == "GET":
        if session.get("username",None):
            return linear()
            
        return redirect('/login')

def linear(message = None):
    x, y,prob = linearPicker()
    session['x'] =x 
    print(x)
    return render_template("linear.html", uname=session["username"], prob=prob, message= message, pts=getPoints())


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("uname", None)
        session["username"] = username
        return redirect('/')
    return render_template("logintest.html")


@app.route("/leaderboard")
def leaderboard():
    return "leaderboard here"
