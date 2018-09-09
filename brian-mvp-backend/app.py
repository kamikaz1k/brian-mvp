from flask import Flask, g
from flask_restful import Resource, Api

from app.database import db
from app.resources.vendor.resource import (
    VendorResource,
    VendorsResource
)
from app.resources.vendor_item.resource import (
    VendorItemResource,
    VendorItemsResource
)

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqldb://root@localhost/brian_mvp?charset=utf8"

db.init_app(app)

api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')
api.add_resource(
    VendorResource,
    '/vendor/<int:vendor_id>'
)
api.add_resource(
    VendorsResource,
    '/vendors'
)
api.add_resource(
    VendorItemResource,
    '/vendor-item/<int:vendor_item_id>'
)
api.add_resource(
    VendorItemsResource,
    '/vendor-items'
)

if __name__ == '__main__':
    app.run(debug=True)