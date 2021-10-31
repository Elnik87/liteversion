from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, FileField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class NewsForm(FlaskForm):
    title = StringField("Заголовок", validators=[DataRequired()])
    intro = TextAreaField("Краткое содержание новости", validators=[DataRequired()])
    content = TextAreaField("Содержание новости", validators=[DataRequired()])
    picture = FileField("Изображение в jpg или png", validators=[FileAllowed("jpg", "png")])
    submit = SubmitField("Опубликовать")


class NewsUpdateForm(FlaskForm):
    title = StringField("Заголовок", validators=[DataRequired()])
    intro = TextAreaField("Краткое содержание новости", validators=[DataRequired()])
    content = TextAreaField("Содержание новости", validators=[DataRequired()])
    picture = FileField("Изображение в jpg или png", validators=[FileAllowed("jpg", "png")])
    submit = SubmitField("Обновить новость")


class CommentForm(FlaskForm):
    name = StringField("Представьтесь", validators=[DataRequired()])
    content = TextAreaField("Введите свой комментарий", validators=[DataRequired()])
    submit = SubmitField("Добавить комментарий")
