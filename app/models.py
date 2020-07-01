from app import db

class entity(db.Model):

    __tablename__ = 'entities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), index=True, unique=False)
    lastname = db.Column(db.String(50), index=True, unique=False)
    place_id = db.Column(db.Integer, db.ForeignKey('places.id'))

    def __repr__(self):
        return '{}, {}, {}'.format(self.name, self.lastname, self.place_id)


class place(db.Model):

    __tablename__ = 'places'

    id = db.Column(db.Integer, primary_key=True)
    place = db.Column(db.String(30), index=True, unique=True)
    entity = db.relationship('entity', backref='place', lazy='dynamic')

    def __repr__(self):
        return '{}'.format(self.place)