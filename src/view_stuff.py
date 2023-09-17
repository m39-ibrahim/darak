from main import app
from flask import render_template


@app.route("/section")
def section():
    return render_template("section.html")


@app.route("/category")
def category():
    return render_template("category.html")
