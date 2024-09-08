from flask import Flask, redirect, url_for
import time

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the home page"


#if the student has passed
@app.route("/pass")
def passed():
    return "Congrats, you've passed"


@app.route("/failed")
def fail():
    return "Unfortunately, you have failed"


@app.route("/score/<name>/<int:num>")
def scored(name, num):
    if num < 30:
        time.sleep(1)
        return redirect(url_for("failed")) # we will pass the name of the function instead of the name of the endpoint
    else:
        time.sleep(1)
        return redirect(url_for("passed")) # we will pass the name of the function instead of the name of the endpoint
        


if __name__ == "__main__":
    app.run(debug = True)


    
    