from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Poll(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    description = db.Column(db.String(2000))
    question = db.Column(db.String(200))
    option_1 = db.Column(db.String(150))
    option_2 = db.Column(db.String(150))
    option_3 = db.Column(db.String(150))
    option_4 = db.Column(db.String(150))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    user_name = db.Column(db.String(100), unique=True)
    polls = db.relationship("Poll")
