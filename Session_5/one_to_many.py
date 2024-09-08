from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ipl.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app) 

class Team(db.Model):
    __tablename__ = "teams" #giving our own name to the table (not compulsory)
    id = db.Column(db.Integer, primary_key = True)
    team = db.Column(db.String(50), nullable = False, unique = True)
    state = db.Column(db.String(50), nullable = False)
    #members is not a columns. We are trying to convey to SQL Alchemy that we are establishing a relationship
    members = db.relationship("Player", backref = "team")  #backref will create an imaginary column in the players table
    
    def __repr__(self):# self is the reference to the current object
        return f"Team('{self.team}', '{self.state}')"
    
    
class Player(db.Model):
    __tablename__ = "players"
    id = db.Column(db.Integer, primary_key = True) 
    name = db.Column(db.String(50), nullable = False)
    nation = db.Column(db.String(50), nullable = False)
    team_id = db.Column(db.Integer, db.ForeignKey("teams.id")) #making a foreign key. Referenced to "teams" table's ID column
    
        
    def __repr__(self):# self is the reference to the current object
        return f"Player('{self.name}', '{self.nation}')"
    
    
if __name__ == "__main__":
    app.run(debug = True)