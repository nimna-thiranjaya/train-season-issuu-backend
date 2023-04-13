import datetime
from server import db


class Season(db.Model):
    __tablename__ = 'SEASON'
    s_id = db.Column(db.Integer, primary_key=True)
    p_id = db.Column(db.Integer, nullable=False)
    start_station = db.Column(db.String, nullable=False)
    end_station = db.Column(db.String, nullable=False)
    renewal_date = db.Column(db.Date, nullable=False)
    expiration_date = db.Column(db.Date, nullable=False)
    price = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

    def __init__(self, **kwargs):
        self.s_id = kwargs.get("s_id")
        self.p_id = kwargs.get("p_id")
        self.start_station = kwargs.get("start_station")
        self.end_station = kwargs.get("end_station")
        self.renewal_date = kwargs.get("renewal_date")
        self.expiration_date = kwargs.get("expiration_date")
        self.price = kwargs.get("price")

    def __repr__(self):
        return "<Season {}>".format(self.s_id)


class IssuedDetails(db.Model):
    __tablename__ = 'ISSUED_DETAILS'
    s_id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=False)
    off_id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

    def __init__(self, **kwargs):
        self.s_id = kwargs.get("s_id")
        self.off_id = kwargs.get("off_id")
        self.date = kwargs.get("date")

    def __repr__(self):
        return "<issuedDetails {}>".format(self.s_id)
