from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, TextField, FileField, SubmitField
from wtforms.validators import DataRequired


class NewsForm(FlaskForm):
    title = StringField("Заголовок", validators=[DataRequired()])
    content = TextField("Содержание новости", validators=[DataRequired()])
    picture = FileField("Изображение в jpg или png", validators=[FileAllowed("jpg", "png")])
    submit = SubmitField("Опубликовать")


class NewsUpdateForm(FlaskForm):
    title = StringField("Заголовок", validators=[DataRequired()])
    content = TextField("Содержание новости", validators=[DataRequired()])
    picture = FileField("Изображение в jpg или png", validators=[FileAllowed("jpg", "png")])
    submit = SubmitField("Опубликовать")

class CommentForm(FlaskForm):
    name = StringField("Представьтесь", validators=[DataRequired()])
    content = TextField("Введите свой комментарий", validators=[DataRequired()])
    submit = SubmitField("Добавить комментарий")

