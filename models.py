from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

db = SQLAlchemy()

def current_time():
    return datetime.now(timezone.utc).replace(microsecond=0)

#these are different tables in the database. Devices and history, each with their respective columns
#visualize in an online db reader or downloading something that reads sqlite databases (.db)
class Device(db.Model): 
    __tablename__ = 'devices'
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    owner = db.Column(db.String)
    serial = db.Column(db.String)
    model = db.Column(db.String)
    status = db.Column(db.String)
    last_user = db.Column(db.String)
    last_updated = db.Column(db.DateTime, default=current_time)

class History(db.Model):
    __tablename__ = 'history'
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.String, db.ForeignKey('devices.id'))
    action = db.Column(db.String)
    user = db.Column(db.String)
    timestamp = db.Column(db.DateTime, default=current_time)
'''
class Inspection(db.Model):
    __tablename__ = 'inspection'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=current_time)
    '''

class Inspection(db.Model):
    __tablename__ = 'inspections'
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.String, db.ForeignKey('devices.id'))
    timestamp = db.Column(db.DateTime, default=current_time)
    # Header fields
    company = db.Column(db.String)
    project = db.Column(db.String)
    equipment_num = db.Column(db.String)
    category = db.Column(db.String)
    if_other = db.Column(db.String)
    model_num = db.Column(db.String)
    operator = db.Column(db.String)
    initials = db.Column(db.String)
    # Checklist stored as JSON string
    checklist_json = db.Column(db.Text)
    
