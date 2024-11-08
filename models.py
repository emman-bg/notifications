from app import db


class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipient = db.Column(db.String(254), nullable=False)
    message = db.Column(db.String(1000), nullable=False)