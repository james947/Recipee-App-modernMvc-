#forms module

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, SubmitField, TextAreaField
#Adds the user to the list
class SignupForm(FlaskForm):
    
    #firstname variable
    firtsname = StringField('firstname',[

        validators.data_required(),
        validators.length(min=4 ,max=10)

    ] )

    #lastname variable
    lastnamename = StringField('lastname',[

        validators.data_required(),
        validators.length(min=4 ,max=10)

    ] )

    #username variable
    username = StringField('username',[

        validators.data_required(),
        validators.length(min=4 ,max=10)

    ] )

    #emailvariable
    email = StringField('email',[

        validators.data_required(),
        validators.length(min=4 ,max=10),
                    validators.regexp(
                r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",
                flags=0, message="Invalid email address"
            )

    ] )