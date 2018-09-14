from __future__ import print_function
from run import create_app, db

app = create_app()

with app.app_context():
    db.create_all()

print("DB Tables Created")
