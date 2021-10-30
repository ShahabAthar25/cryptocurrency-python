from enum import unique
from database import db

class transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.Text, nullable=False)
    userPhoto = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)
    to = db.Column(db.Text, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    time = db.Column(db.DateTime, nullable=False)