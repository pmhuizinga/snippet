from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length


class CreateSnippet(FlaskForm):
    user = SelectField('user', validators=[DataRequired()])
    language = SelectField('language', validators=[DataRequired()])
    tag = StringField('tag', validators=[DataRequired(), Length(max=100, message='name too long, max 100 characters')])
    snippet = TextAreaField('snippet', validators=[DataRequired(), Length(max=300, message='name too long, max 100 characters')])
    submit = SubmitField('Insert')


class ModifySnippet(FlaskForm):
    user = SelectField('user', validators=[DataRequired()])
    language = SelectField('language', validators=[DataRequired()])
    tag = StringField('tag', validators=[DataRequired(), Length(max=100, message='name too long, max 100 characters')])
    snippet = StringField('snippet', validators=[DataRequired(), Length(max=300, message='name too long, max 100 characters')])
    submit = SubmitField('Insert')


class CreateUser(FlaskForm):
    user = StringField('name', validators=[DataRequired(), Length(max=50, message='name too long, max 50 characters')])
    submit = SubmitField('Insert')


class CreateLanguage(FlaskForm):
    language = StringField('name', validators=[DataRequired(), Length(max=50, message='name too long, max 50 characters')])
    submit = SubmitField('Insert')