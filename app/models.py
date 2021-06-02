from app import db
from datetime import datetime as dt




class Divvy(db.Model):
    trip_id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.datetime, default=dt.utcnow)
    stop_time = db.Column(db.datetime, default=dt.utcnow)
    bike_id = db.Column(db.Integer)
    from_station_id = db.Column(db.Integer)
    from_station_name = db.Column(db.String)
    to_station_id = db.Column(db.Integer)
    to_station_name = db.Colum(db.String)
    user_type = db.Column(db.String)
    gender = db.Column(db.String)
    birthday = db.Column(db.String)
    trip_duration = db.Column(db.Integer)
