from main import app
from flask import render_template, request, redirect, session
from classes.user_factory import UserFactory

@app.route("/account")
def account():
    return render_template("account.html")


@app.route("/login", methods=["POST"])
def login():
    if request.method != 'POST':
        return render_template("error.html", err = "wrong request")
    user_type = request.form["type"]
    id = request.form["id"]
    password = request.form["password"]

    user = UserFactory.get_user_type(user_type)(id, password)

    if not user:
        return render_template("error.html", err = "user does not exist")

    return redirect(request.referrer)


@app.route("/logout")
def logout():
    return redirect(request.referrer)
