from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///employees.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False #improves readability 

db = SQLAlchemy(app) 

#table (model) of the database
class Employee(db.Model): #the class that we write to represent a table is called Model
#we'll write the structure of the database
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)  #nullable = False because we don't wannt the name column to be empty
    age = db.Column(db.Integer, nullable = False)
    email = db.Column(db.String(50), nullable = False, unique = True) #unique = True because no two emails can be the same

    def __repr__(self): #this method is used to modify the output
        return f"Employee('{self.name}', {self.age}, '{self.email}')"
if __name__ == "main":
    app.run(debug= True)
    
    