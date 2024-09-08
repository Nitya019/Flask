from flask import(Flask,
                  render_template,
                  redirect,
                  url_for,
                  flash,
                  session, 
                  request)  #session is a dictionary

from forms import LoginForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "This_is_the_token"

@app.route("/")
@app.route("/home")
def home():  #user_name
    return render_template("home.html", title = "Home")

@app.route("/about")
def about():
    #we will whethet the user has logged in or not
    if "user_name" not in session:
        flash("Login required")
        return redirect(url_for('login', next = request.url))  #next will colle
    else: #if the user has logged in
        flash(f"HI {session['user_name']}")
    return render_template("about.html", title = "About")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session["user_name"] = form.username.data #storing the username  
        flash(f"Successfully logged in as {session['user_name'].title()}!")
        next_url = request.args.get("next") #retrieving the argument of value of next
        return redirect(next_url or url_for("home")) #if accessed from about or contact page then redirect to them or else the home page
    return render_template("login.html", title = "Login", form = form)


@app.route("/contact")
def contact():
    if "user_name" not in session:
        flash("Login required")
        return redirect(url_for('login', next = request.url))  #next will colle
    else: #if the user has logged in
        flash(f"HI {session['user_name']}")
    return render_template("contact.html", title = "Contact")

if __name__ == "__main__":
    app.run(debug = True)
    
#cookie is in base64

