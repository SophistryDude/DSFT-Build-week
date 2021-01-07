"""SQLAlchemy models and utility functions for twitoff"""

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

DB = SQLAlchemy()
MIGRATE = Migrate()


class User(DB.model):
    """users corresponding to tweets"""
    id = DB.column(DB.BigInteger, primary_key=True)
    name = DB.column(DB.String, nullable=False)
    SongSuggestion = DB.Column(DB.BigInteger)
    def __repr__(self):
        return "<User: {}>".format(self.name)


class Suggestions(DB.Model):
    """Previous song suggestions"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(300))
    vect = DB.Column(DB.PickleType, nullable=False)
    #foreign key - user.id
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey(
        'user.id', nullable=False))
    user = DB.relationship('User', backref=DB.backref(
        'tweets', lazy=True))

def __repr__(self):
    return "<Tweet: {}>".format(self.text)
