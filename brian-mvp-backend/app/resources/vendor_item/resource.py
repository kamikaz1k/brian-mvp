from flask import request
from flask_restful import Resource, abort

from app.database import db

from app.models.vendor_item import VendorItem as VendorItemModel


DEFAULT_VENDOR_ID = 1
def serializer_vendor_item(vendor_item):
    return {
        'type': 'vendor-item',
        'id': vendor_item.id,
        'attributes': {
            'vendor_id': vendor_item.vendor_id,
            'name': vendor_item.name,
            'timer_started_at': vendor_item.timer_started_at.isoformat() + "Z",
            'timer_stop_at': vendor_item.timer_stop_at.isoformat() + "Z"
        }
    }


class VendorItemResource(Resource):

    def get(self, vendor_item_id):
        vendor_id = DEFAULT_VENDOR_ID
        vendor_item = VendorItemModel.query.filter(
            VendorItemModel.vendor_id == vendor_id,
            VendorItemModel.id == vendor_item_id
        ).one_or_none()

        return {
            'data': serializer_vendor_item(vendor_item)
        }


class VendorItemsResource(Resource):

    def get(self):
        vendor_id = DEFAULT_VENDOR_ID
        vendor_items = VendorItemModel.query.filter(
            VendorItemModel.vendor_id == vendor_id
        ).all()

        return {
            'data': [
                serializer_vendor_item(vendor_item)
                for vendor_item in vendor_items
            ]
        }

    def post(self):
        params = request.json.get('data')['attributes']
        vendor_id = DEFAULT_VENDOR_ID
        vendor_item = VendorItemModel(
            id=params.get('id'),
            vendor_id=vendor_id,
            name=params.get('name'),
            timer_started_at=params.get('timer_started_at'),
            timer_stop_at=params.get('timer_stop_at'),
        )

        db.session.add(vendor_item)
        db.session.commit()

        return {
            'data': serializer_vendor_item(vendor_item)
        }
