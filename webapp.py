import json

from flask import Flask, render_template

from login_form import LoginForm
from new_student_form import NewStudentForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'superduper-secretkey'


@app.route('/')
def hello_world():
    user = {'username': "Jonathan"}
    return render_template("index.html", title="Home Page", user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Capture data from the form and save to the database.
        print("SUBMITTED", form.username, form.password, form.remember_me)
    return render_template("new_student.html", title="Home Page", form=form)


@app.route('/newstudent', methods=['GET', 'POST'])
def new_student():
    form = NewStudentForm()
    if form.validate_on_submit():
        # Capture data from the form and save to the database.
        print("SUBMITTED", form.firstname, form.lastname)
    return render_template("new_student.html", title="New Student", form=form)


if __name__ == '__main__':
    app.run()
