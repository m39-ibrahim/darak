from main import app
from flask import render_template, request, redirect
import model


@app.route("/home")
@app.route("/index")
@app.route("/")
def home():
    print([i for i in model.sample()])
    return render_template("home.html")


@app.route("/about_us")
def about_us():
    return render_template("about_us.html")
