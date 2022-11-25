from main import db


class Data(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    data = db.Column(db.String(length=300), nullable=False)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

