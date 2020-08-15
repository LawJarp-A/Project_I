from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class get_url(FlaskForm):
    enter_url = StringField('Enter Product link', validators=[DataRequired()])
    submit = SubmitField('Get Price')
