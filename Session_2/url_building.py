import time
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Home page!"


@app.route("/pass/<sname>/<int:marks>")
def passed(sname, marks):
    return f"Congrats {sname.title()}, you've passed with {marks} marks!"


@app.route("/fail/<sname>/<int:marks>")
def failed(sname, marks):
    return f"Sorry {sname.title()}, you've failed with {marks} marks!"


@app.route("/score/<name>/<int:num>")
def score(name, num):
    if num < 30:
        time.sleep(1)
        # redirect user to page 'fail'
        return redirect(url_for("failed", sname=name, marks=num))
    else:
        time.sleep(1)
        # redirect user to page 'pass'
        return redirect(url_for("passed", sname=name, marks=num))


if __name__ == "__main__":
    app.run(debug=True)