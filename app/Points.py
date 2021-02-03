import os
from flask import session
def savePoints(v):
    username = session["username"]
    open("pts/"+username, 'w').write(str(v))
def getPoints():
    username = session["username"]
    point = 0
    try:
        point = int(open("pts/"+username, 'r').read())
    except (ValueError, FileNotFoundError):
        pass
    return point
def init():
    os.makedirs('pts', exist_ok=True)
