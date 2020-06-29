from app import db

class tbl_entity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), index=True, unique=False)
    lastname = db.Column(db.String(50), index=True, unique=False)
    address = db.Column(db.String(50), index=True, unique=False)

    def __repr__(self):
        return '<entity {}>'.format(self.name)

