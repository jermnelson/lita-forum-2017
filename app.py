__author__ = "Jeremy Nelson"
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("lita-forum-2017/index.html")
