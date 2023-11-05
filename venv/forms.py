from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
    

class Form(FlaskForm):
    name = StringField("Імʼя:", 
                           validators=[DataRequired("Заповніть поле!")],
                           render_kw={"class": "form-control"})
    text = TextAreaField("Відгук:", 
                           validators=[DataRequired("Заповніть поле!")],
                           render_kw={"class": "form-control"})
    submit = SubmitField("Відправити", 
                         render_kw={"class": "btn btn-block btn-primary"})