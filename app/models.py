from app import db

class entity(db.Model):

    __tablename__ = 'entities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), index=True, unique=False)
    lastname = db.Column(db.String(50), index=True, unique=False)

    def __repr__(self):
        return '<entity {}>'.format(self.name)

