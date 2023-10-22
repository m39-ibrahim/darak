from main import app
from flask import render_template, request, redirect


@app.route("/home")
@app.route("/index")
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about_us")
def about_us():
    return render_template("about_us.html")
