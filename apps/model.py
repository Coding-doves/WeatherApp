from flask_sqlalchemy import SQLAlchemy


# Declare base model
db = SQLAlchemy()


# Weather model
class Weather(db.Model):

    # Id generated using UUID
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city = db.Column(db.String(150), nullable=False)
    date = db.Column(db.Date, nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(250), nullable=False)
