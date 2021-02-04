from flask import request, render_template, session, redirect, url_for
from app import app
from app.PolyLinear import linearPicker
from app.Points import savePoints, getPoints
from app.PolynomialGenerator import polynomialgen


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        if session.get("username", None) == None:
            return redirect("/login")
        x = session.get('x', None)
        ans = request.form.get('ans', None)
        try:
            ans = float(ans)
            if abs(ans - x) < 0.01:
                savePoints(10*session.get("difficulty", 1) + getPoints())
                return prob("correct")
            else:
                return prob("incorrect")
                
        except ValueError:
            return linear("empty")
    elif request.method == "GET":
        if session.get("username",None):
            return prob()
            
        return redirect('/login')

def prob(message = None):
    return linear(message) 

def linear(message = None):
    thing = ""
    prob = ""
    x = 0
    if session.get("difficulty", 1) == 1:
        thing = "Solve for x and type x intercept below. Rounding to 2 decimal places."
        x, y,prob = linearPicker()
    else:
        thing = "Solve for smaller root. Rounding to 2 decimal places."
        x,y, prob = polynomialgen()
        x = min(x,y)
    print(x)
    session['x'] =x 
    
    return render_template("thing.html", uname=session["username"], prob=prob, message= message, pts=getPoints(), thing = thing)

@app.route("/level", methods = ["GET","POST"])
def levelSet():
    if request.method == "POST":
        try:
            session["difficulty"] = int(request.form.get("v", 1))
        except: pass
        return redirect("/")
    else:
        return render_template("difficulty.html")

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
