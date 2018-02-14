#importing methods
from functools import wraps
from flask import Flask, render_template, redirect ,url_for, request, flash, session
from .forms import SignupForm, LoginForm
from .users import Users, USERS

#instanciate app
app = Flask(__name__)
#secret key 
app.config['SECRET_KEY'] ="b'6b3105e553c75d921da76d0b13344700cf3b1b8e98efb639'"

def is_loggedin(function):
  #checks if user is logged in
    @wraps(function)
    def authorizer(*args, **kwargs):
        #confirms user not in session
        if 'user' not in session:
            flash('Sorry, you need to be logged in to view this', 'warning')
            return redirect(url_for('index'))
        return function(*args, **kwargs)
    return authorizer

#route to index page
@app.route('/index/', methods=['GET','POST'])
def index():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        user = Users.get_user(form.email.data, form.password.data)
        if user == "users not found":
             flash('Account not registerd, creat account.')
             return redirect(url_for('signup'))
        elif user == "Password error!":
            flash('Please enter the correct details.')
            return redirect(url_for('index'))
        elif user["email"] == form.email.data:
            session ["user"] == form.email.data
            session['username'] = USERS[form.email.data]['username']
            session["logged_in"] = True
            return redirect(url_for('dashboard', user=session['username']))
    return render_template("index.html",form=form)

#route to sign up page
@app.route("/signup/", methods=['GET', 'POST'])
def signup():
    form = SignupForm(request.form)
    if request.method == "POST" and form.validate():
        status =Users.add_user(form.email.data, form.username.data, form.password.data)
        flash("status")
        if status == "Sorry, Email is already registered":
            return redirect(url_for("signup"))
        return redirect(url_for("index"))
    elif "logged_in" not in session:    
         return render_template('signup.html', form=form)
    if session['logged_in']:
        return redirect(url_for('dashboard'))


