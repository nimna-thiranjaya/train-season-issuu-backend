"""Data models."""
import datetime
from flask_bcrypt import generate_password_hash, check_password_hash
from server import db


class Officer(db.Model):
    """Officer model."""
    __tablename__ = 'CGR_OFFICER'
    off_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    contact = db.Column(db.String(10), nullable=False)
    nic = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(1000), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

    def __init__(self, **kwargs):
        """
        The function takes in a dictionary of keyword arguments and assigns the values to the class
        attributes
        """
        self.name = kwargs.get("name")
        self.contact = kwargs.get("contact")
        self.nic = kwargs.get("nic")
        self.email = kwargs.get("email")
        self.password = kwargs.get("password")

    def __repr__(self):
        """
        The __repr__ function is used to return a string representation of the object
        :return: The username of the user.
        """
        return "<Officer {}>".format(self.email)

    def hash_password(self):
        """
        It takes the password that the user has entered, hashes it, and then stores the hashed password in
        the database
        """
        self.password = generate_password_hash(self.password).decode("utf8")

    def check_password(self, password):
        """
        It takes a plaintext password, hashes it, and compares it to the hashed password in the database

        :param password: The password to be hashed
        :return: The password is being returned.
        """
        return check_password_hash(self.password, password)
