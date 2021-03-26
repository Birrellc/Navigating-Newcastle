from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp
import re


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=3, max=12,
                            message="Must be between 3 and 12 characters long"), Regexp('^\w+$',
                             message="Username must contain only letters numbers or underscore")])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     Length(min=8)])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=3, max=12,
                            message="Must be between 3 and 12 characters long"), Regexp('^\w+$',
                             message="Username must contain only letters numbers or underscore")])
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
    word = StringField("Word", validators=[DataRequired()])
    submit = SubmitField("Search Word")
