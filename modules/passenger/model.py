import datetime
from server import db


class Passenger(db.Model):
    __tablename__ = 'PASSENGER'
    p_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    contact = db.Column(db.String(10), nullable=False)
    nic = db.Column(db.String(40), nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    address = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

    def __init__(self, **kwargs):
        self.p_id = kwargs.get("p_id")
        self.name = kwargs.get("name")
        self.contact = kwargs.get("contact")
        self.nic = kwargs.get("nic")
        self.address = kwargs.get("address")
        self.birthday = kwargs.get("birthday")

    def __repr__(self):
        return "<Passenger {}>".format(self.nic)
