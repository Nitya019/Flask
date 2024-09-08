from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the home page"

@app.route("/hi/steve")
def welcome_steve():
    return "Hey steve, welcome to our Webpage"

@app.route("/hi/tony")
def welcome_tony():
    return "Hey Tony, welcome to our Webpage"

#problem: We cannot keep on writing the same code for each viewer of the website, hence we can pass a parameter

@app.route("/welcome/<name>")
def welcome(name):
    return f"Hi {name.title()}! Welcome to the webpage"


if __name__ == "__main__":
    app.run(debug = True)
    

