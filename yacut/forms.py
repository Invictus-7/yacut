from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Optional, Regexp, URL

from settings import SHORT_ID_REGEX


class URLMapForm(FlaskForm):
    original_link = StringField(
        'Длинная ссылка',
        validators=[DataRequired(message='Обязательное поле'),
                    URL(message='Некорректная ссылка')],
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Optional(),
            Length(1, 16),
            Regexp(regex=SHORT_ID_REGEX,
                   message='Можно использовать только цифры и буквы "a-Z"')]
    )

    submit = SubmitField('Создать')
