from wtforms import StringField,TextAreaField,SubmitField
from flask_wtf import FlaskForm

class SignForm(FlaskForm):
    name=StringField('Your name')
    comment=TextAreaField('Your Comment')
    sign=SubmitField('Sign')