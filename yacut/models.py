from datetime import datetime
from flask import url_for

from . import db

FIELD_RELATIONS = {'original': 'url', 'short': 'custom_id'}


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String, nullable=False)
    short = db.Column(db.String, unique=True, nullable=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=url_for('index_view', _external=True) + self.short
        )

    def from_dict(self, data):
        for field_1, field_2 in FIELD_RELATIONS.items():
            if field_2 in data:
                setattr(self, field_1, data[field_2])
