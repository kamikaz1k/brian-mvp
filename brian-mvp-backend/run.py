import os

from flask import Flask, g, render_template, Response
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

api = Api()

class LandingPage(Resource):
    def get(self):
        return Response(
            response=render_template('index.html'),
            mimetype='text/html'
        )

api.add_resource(LandingPage, '/')
api.add_resource(
    VendorResource,
    '/vendors/<int:vendor_id>'
)
api.add_resource(
    VendorsResource,
    '/vendors'
)
api.add_resource(
    VendorItemResource,
    '/vendor-items/<int:vendor_item_id>'
)
api.add_resource(
    VendorItemsResource,
    '/vendor-items'
)

def get_db_url():
    LOCAL_DEV_URI = "mysql+mysqldb://root@localhost/brian_mvp?charset=utf8"
    return os.environ.get(
        'CLEARDB_DATABASE_URL',
        LOCAL_DEV_URI
    )

def create_app():
    app = Flask(
        'brian_mvp',
        template_folder=os.path.abspath('./static'),
        static_folder=os.path.abspath('./static/assets')
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = get_db_url()

    db.init_app(app)
    api.init_app(app)

    return app

if __name__ == '__main__':
    create_app().run(debug=True)
