import random
import string

from .models import URLMap
from settings import SHORT_URL_LENGTH


def retrieve_obj(item, query):
    return URLMap.query.filter(item == query)


def check_short_id(short_id):
    return retrieve_obj(URLMap.short, short_id).first() is None


def get_unique_short_id():
    base_symbol_pack = string.ascii_letters + string.digits
    short_id = ''.join(random.choice(base_symbol_pack) for i in range(SHORT_URL_LENGTH))
    if check_short_id(short_id):
        return short_id
    return get_unique_short_id()
