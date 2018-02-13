#importing methods
from flask import Flask, render_template, redirect ,url_for, request
from .forms import SignupForm, LoginForm
from .users import Users, USERS

#instanciate app
app = Flask(__name__)
#secret key 
app.config['SECRET_KEY'] ="b'6b3105e553c75d921da76d0b13344700cf3b1b8e98efb639'"
#route to index page
@app.route('/index', methods=['GET','POST'])
def index():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        

    return render_template("index.html",form=form)