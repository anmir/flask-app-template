# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from flask_wtf import Form, TextField, TextAreaField, DateTimeField, PasswordField
from flask_wtf import Required


class ExampleForm(Form):
    title = TextField(u'Title', validators=[Required()])
    content = TextAreaField(u'Content')
    date = DateTimeField(u'Data', format='%d/%m/%Y %H:%M')


# recaptcha = RecaptchaField(u'Recaptcha')

class LoginForm(Form):
    user = TextField(u'Name', validators=[Required()])
    password = PasswordField(u'Password', validators=[Required()])
