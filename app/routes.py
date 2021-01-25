from flask import request
from app import app


@app.route("/")
def home():
    return "questions and login"


@app.route("/leaderboard")
def leaderboard():
    return "leaderboard here"