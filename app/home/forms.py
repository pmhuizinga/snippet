from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length


class CreateForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(), Length(max=30, message='name too long, max 30 characters')])
    lastname = StringField('lastname', validators=[DataRequired(), Length(max=50, message='lastname too long, max 50 characters')])
    place_id = SelectField('place', validators=[DataRequired()]) #, id='select_place'
    submit = SubmitField('Insert')


class ModifyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    lastname = StringField('lastname', validators=[DataRequired()])
    place_id = IntegerField('place')
    submit = SubmitField('Insert')


class CreatePlace(FlaskForm):
    place = StringField('name', validators=[DataRequired(), Length(max=30, message='name too long, max 30 characters')])
    submit = SubmitField('Insert')

