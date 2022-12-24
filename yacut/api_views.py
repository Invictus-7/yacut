import re

from flask import jsonify, request
from http import HTTPStatus

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from settings import SHORT_ID_REGEX
from .utils import check_short_id, get_unique_short_id, retrieve_obj


@app.route('/api/id/', methods=['POST'])
def create_short_link():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('\"url\" является обязательным полем!')
    if 'custom_id' in data:
        custom_id = data.get('custom_id')
        if not check_short_id(custom_id):
            raise InvalidAPIUsage(f'Имя "{custom_id}" уже занято.')
        if custom_id == '' or custom_id is None:
            data['custom_id'] = get_unique_short_id()
        elif not re.match(SHORT_ID_REGEX, custom_id):
            raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
    else:
        data['custom_id'] = get_unique_short_id()
    new_url = URLMap()
    new_url.from_dict(data)
    db.session.add(new_url)
    db.session.commit()
    return jsonify(new_url.to_dict()), HTTPStatus.CREATED


@app.route('/api/id/<short_id>/', methods=['GET'])
def get_original_url(short_id):
    db_object = retrieve_obj(URLMap.short, short_id).first()
    if not db_object:
        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
    original_url = db_object.original
    return jsonify({'url': original_url}), HTTPStatus.OK
