from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    credits = db.Column(db.Integer, default=0)
    referrals = db.Column(db.Integer, default=0)

db.create_all()
