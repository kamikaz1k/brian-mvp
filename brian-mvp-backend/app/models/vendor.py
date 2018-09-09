from app.database import db


class Vendor(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    status = db.Column(db.String(10), nullable=False)
