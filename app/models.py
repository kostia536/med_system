
from . import db

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    test_name = db.Column(db.String(100), nullable=False)
    results = db.Column(db.Text, nullable=True)
