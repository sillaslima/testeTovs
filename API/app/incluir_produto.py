from flask_sqlalchemy import SQLAlchemy
from models.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


#db.create_all()
#db.create_all()

