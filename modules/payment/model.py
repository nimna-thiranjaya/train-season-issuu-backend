import datetime
from server import db

class Payment(db.Model):
    __tablename__ = 'PAYMENT'
    payment_id = db.Column(db.Integer, nullable=False, primary_key=True)
    s_id = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

    def __init__(self, **kwargs):
        self.payment_id = kwargs.get("payment_id")
        self.s_id = kwargs.get("s_id")
        self.amount = kwargs.get("amount")
        self.date = kwargs.get("date")

    def __repr__(self):
        return "<Payment {}>".format(self.payment_id)