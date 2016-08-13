from settings import logger
from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length


class LoginForm(Form):
    username = StringField('username',
                           validators=[
                               DataRequired('Please enter a username and/or email if you are not registered.'),
                            ])
    password = PasswordField('password', validators=[
                                            DataRequired('Please enter a password.'),
                                            Length(min=3, message='Password needs at least 6 alphanumeric characters.')
                            ])