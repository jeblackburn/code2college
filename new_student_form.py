from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class NewStudentForm(FlaskForm):
    firstname = StringField("First Name", validators=[DataRequired()])
    lastname = StringField("Last Name", validators=[DataRequired()])
    grade = StringField("Grade", validators=[DataRequired(), NumberRange(9, 12)])
    submit = SubmitField('Add Student')
