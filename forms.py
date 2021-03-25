from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=5, max=25)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class DictionaryForm(FlaskForm):
    word = StringField('Word',
                       validators=[DataRequired()])
    definition = StringField('Definition', validators=[DataRequired()])
    example = StringField('Example',
                          validators=[DataRequired()])
    submit = SubmitField('Add Word')


class UpdateWordForm(FlaskForm):
    word = StringField('Word', validators=[DataRequired()])
    definition = StringField('Definition', validators=[DataRequired()])
    example = StringField('Example', validators=[DataRequired()])
    submit = SubmitField('Update Word')


class SearchForm(FlaskForm):
    word = StringField('word')
    submit = SubmitField('search')
