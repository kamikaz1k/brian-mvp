from sqlalchemy.schema import ForeignKey


from app.database import db


class VendorItem(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    vendor_id = db.Column(db.Integer, ForeignKey("vendor.id"), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    timer_started_at = db.Column(db.TIMESTAMP, nullable=False)
    timer_stop_at = db.Column(db.TIMESTAMP, nullable=False)
