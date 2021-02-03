from flask import request, render_template, session, redirect, url_for
from app import app
from app.PolyLinear import linearPicker


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        pass

    if session.get("username",None):
        x, y,prob = linearPicker()
        return render_template("linear.html", uname=session["username"], prob=prob)

    return redirect('/login')


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