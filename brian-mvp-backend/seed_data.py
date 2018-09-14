from __future__ import print_function
from run import create_app, db
from app.models.vendor import Vendor as VendorModel

app = create_app()

with app.app_context():
    DEFAULT_NAME = "Default Vendor Name"
    exists = VendorModel.query.filter(VendorModel.name == DEFAULT_NAME).one_or_none()

    if not exists:
        vendor = VendorModel(
            name=DEFAULT_NAME,
            status="open"
        )
        db.session.add(vendor)
        db.session.commit()

        print("Default vendor row created")

    else:
        print("'{name}' already exists".format(name=DEFAULT_NAME))
