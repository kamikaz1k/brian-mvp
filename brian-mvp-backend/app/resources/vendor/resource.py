from flask import request
from flask_restful import Resource, abort

from app.database import db

from app.models.vendor import Vendor as VendorModel


def serializer_vendor(vendor):
    return {
        'type': 'vendor',
        'id': vendor.id,
        'attributes': {
            'name': vendor.name,
            'status': vendor.status
        }
    }


class VendorResource(Resource):

    def get(self, vendor_id):

        vendor = VendorModel.query.get(vendor_id)

        if not vendor:
            abort(404, message="Vendor {} doesn't exist".format(vendor_id))

        return {
            'data': serializer_vendor(vendor)
        }


class VendorsResource(Resource):

    def get(self):
        vendors = VendorModel.query.all()
        return {
            'data': [
                serializer_vendor(vendor)
                for vendor in vendors
            ]
        }

    def post(self):

        params = request.json

        vendor = VendorModel(
            name=params.get('name'),
            status=params.get('status')
        )

        db.session.add(vendor)
        db.session.commit()

        return {
            'data': serializer_vendor(vendor)
        }
