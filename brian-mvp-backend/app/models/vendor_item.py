import datetime

from sqlalchemy.schema import ForeignKey
from sqlalchemy.sql.expression import func

from app.database import db


class VendorItem(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    vendor_id = db.Column(db.Integer, ForeignKey("vendor.id"), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    # because first column gets auto update
    updated_at = db.Column(
        db.TIMESTAMP,
        server_default=func.now(),
        onupdate=func.current_timestamp()
    )
    timer_started_at = db.Column(db.TIMESTAMP(timezone=True), nullable=False)
    timer_stop_at = db.Column(db.TIMESTAMP(timezone=True), nullable=False)

