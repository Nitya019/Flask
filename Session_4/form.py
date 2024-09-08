from flask_wtf import FlaskForm
from wtforms import (StringField, SelectField, DateField, PasswordField, SubmitField, BooleanField)
from wtforms.validators import(DataRequired, Length, Email, Optional, EqualTo)


class SignupForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[DataRequired(), Length(2, 30)]    # to check whether the user has input any data and whether it follows the conditions
    )
#DataRequired check whether the user has input any data
#Length will check whether the length of the input is b/w 2 - 30 char or not
    email = StringField(
        "Email",
        validators=[DataRequired(),Email() ]
    )
    
    gender = SelectField(
        "Gender",
        choices=['Male', 'Female', 'Other'],
        validators=[Optional()]
    )
#Optional will make it optional for the users to fill their gender

    dob = DateField(
        "Date of Birth",
        validators=[Optional()]
    )
    
    password = PasswordField(
        "Password",
        validators=[DataRequired(), Length(5,25)]
    )
    
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[DataRequired(), Length(5,25), EqualTo('password')]
    )#the value of confirm password should be equal to the password

    submit = SubmitField("Sign up")
    
    
class LoginForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[DataRequired(),Email() ]
    )
    
    password = PasswordField(
        "Password",
        validators=[DataRequired(), Length(5,25)]
    )
    
    remember_me = BooleanField("Remember Me")
    
    submit = SubmitField("Login")
