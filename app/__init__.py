
from flask import Flask
from config import Config
import os
app = Flask(__name__,
template_folder='../templates')
app.config.from_object(Config)
app.secret_key = os.urandom(10)
from app.Points import init
init()
from app import routes

