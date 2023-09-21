from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(255))

    def __init__(self, data):
        self.data = data

    def save(self):
        db.session.add(self)
        db.session.commit()
