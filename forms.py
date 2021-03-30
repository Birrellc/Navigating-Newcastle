from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp
import re

regex_key = re.compile("^[^\s].+[^\s]$")


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=3, max=12,
                                                              message="Please enter a username between 3 and 12 characters long"), Regexp(regex_key,
                                                                                                                                          message="Username must be alphanumeric and not start with a space")])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     Length(min=8, message="Password must be atleast 8 letters long")])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(message="Please enter a username"), Length(min=3, max=12,
                                                                                               message="Please enter a username between 3 and 12 characters long"), Regexp(regex_key,
                                                                                                                                                                           message="Username must be alphanumeric not start with a space")])
    password = PasswordField('Password', [DataRequired(),
                                          Length(min=8, message="Password must be atleast 8 letters long")])
    submit = SubmitField('Login')


class DictionaryForm(FlaskForm):
    word = StringField('Word',
                       validators=[DataRequired(), Regexp(regex_key,
                                                          message="Must be alphanumeric not start with a space")])
    definition = StringField('Definition', validators=[DataRequired(), Regexp(regex_key,
                                                                              message="Must be alphanumeric not start with a space"), Length(min=2, max=25, message="must be between 2-25 characters")])
    example = StringField('Example',
                          validators=[DataRequired(), Regexp(regex_key,
                                                             message="Must be alphanumeric not start with a space"), Length(min=2, max=50, message="must be between 2-50 characters")])
    submit = SubmitField('Add Word')


class UpdateWordForm(FlaskForm):
    word = StringField('Word',
                       validators=[DataRequired(), Regexp(regex_key,
                                                          message="Must be alphanumeric not start with a space")])
    definition = StringField('Definition', validators=[DataRequired(), Regexp(regex_key,
                                                                              message="Must be alphanumeric not start with a space"), Length(min=2, max=25, message="must be between 2-25 characters")])
    example = StringField('Example',
                          validators=[DataRequired(), Regexp(regex_key,
                                                             message="Must be alphanumeric not start with a space"), Length(min=2, max=50, message="must be between 2-50 characters")])
    submit = SubmitField('Update Word')


class SearchForm(FlaskForm):
    word = StringField("", validators=[DataRequired(), Regexp(regex_key,
                                                              message="Must be alphanumeric not start with a space")])
    submit = SubmitField("Search Word")
