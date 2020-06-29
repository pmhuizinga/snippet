from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class ModifyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    lastname = StringField('lastname', validators=[DataRequired()])
    submit = SubmitField('Insert')


class CreateForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(), Length(max=30, message='name too long, max 30 characters')])
    lastname = StringField('lastname', validators=[DataRequired(), Length(max=50, message='lastname too long, max 50 characters')])
    submit = SubmitField('Insert')