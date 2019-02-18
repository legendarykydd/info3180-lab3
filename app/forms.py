from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,validators, ValidationError

class ContactForm(FlaskForm):
    
    name = StringField('Name',[validators.DataRequired()])
    email = StringField('E-mail',[validators.DataRequired()])
    subject = StringField('Subject',[validators.DataRequired()])
    message = TextAreaField('Message',[validators.DataRequired()])
    send = SubmitField("Send")