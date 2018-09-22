from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, RadioField, DateTimeField, SelectField
from wtforms.validators import ValidationError, DataRequired, Length, Email, EqualTo
from dan.models import User

class LoginForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
    email = StringField('Email', validators=[DataRequired(), Email()])

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register New User')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("Email already registered")

class ReviewForm(FlaskForm):
    review = StringField('Review', validators=[DataRequired()])
    rating = IntegerField('Rating')
    grade = IntegerField('Grade')
    submit = SubmitField('Add Review') 

class CourseSearchForm(FlaskForm):
    search = StringField('Search', validators=[DataRequired()])
    submit = SubmitField('Search') 
