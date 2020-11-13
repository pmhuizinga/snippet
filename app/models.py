from app import db

class language(db.Model):

    __tablename__ = 'language'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), index=True, unique=False)

    def __repr__(self):
        return '{}'.format(self.name)


class user(db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True, unique=False)

    def __repr__(self):
        return '{}'.format(self.name)


class snippet(db.Model):

    __tablename__ = 'snippet'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    language_id = db.Column(db.Integer, db.ForeignKey('language.id'))
    tag = db.Column(db.String(100), index=True, unique=False)
    snippet = db.Column(db.String(300), unique=False)
    # language = db.relationship('language', backref=backref('snippet', lazy='dynamic'))
    # language = db.relationship('language', backref='snippet', lazy='dynamic')
    language = db.relationship('language', backref='snippet')
    # user = db.relationship('user', backref='snippet', lazy='dynamic')
    user = db.relationship('user', backref='snippet')

    def __repr__(self):
        return '{}'.format(self.snippet)