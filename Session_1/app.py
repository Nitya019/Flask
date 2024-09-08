from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route("/home")   #for the same server we can have multiple routes
def index():
    return "<H1>Welcome to home page</H1>"


@app.route("/welcome/<name>")   #PATH parameters
def welcome(name):
    return f"<h1>Hi {name} </h1>"  #Note : these parameters (eg. name), by default are strings

@app.route("/addition/<int:num>")  #taking an int path parameter
def addition(num):
    return f"Input is {num}, output is {num + 10}"

@app.route("/addition_two/<int:num1>/<int:num2>")  #taking an 2 int path parameter
def addition_two(num1, num2):
    return f"{num1} + {num2}, is {num1 + num2}"


@app.route("/about")
def about():
    return "<H1>Welcome to about page</H1>"

if __name__ == "__main__":
    app.run(debug = True)    