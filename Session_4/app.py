from flask import Flask, render_template, redirect, url_for, flash
from form import SignupForm, LoginForm  #These are classes

app = Flask(__name__)
app.config["SECRET_KEY"] = "This_is_the_csrf_token"

@app.route("/")
@app.route("/home")
def home():
    return  render_template("home.html", title = "Home")

@app.route("/signup", methods = ["GET","POST"]) #telling the app that we expect to submit data
def signup():
    form = SignupForm() #making an object 
    if form.validate_on_submit(): #if the data is correct then redirect to the home page
        flash(f"Welcome {form.username.data}!")
        return redirect(url_for("home"))
    return  render_template("signup.html", title = "Sign up", form = form)


@app.route("/login", methods = ['GET','POST'])
def login():
    form = LoginForm()
    email = form.email.data
    pw = form.password.data
    if form.validate_on_submit():
        if email == "abc@gmail.com" and pw == "12345":
            flash("Logged in successfully!")
            return redirect(url_for("home"))
        else:
            flash("Incorrect email or password")
    return  render_template("login.html", title = "Login", form = form)

if __name__ == "__main__":
    app.run(debug = True)