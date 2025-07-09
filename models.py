from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Device(db.Model):
    __tablename__ = 'devices'
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    serial = db.Column(db.String)
    model = db.Column(db.String)
    status = db.Column(db.String)
    last_user = db.Column(db.String)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)

class History(db.Model):
    __tablename__ = 'history'
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.String, db.ForeignKey('devices.id'))
    action = db.Column(db.String)
    user = db.Column(db.String)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
