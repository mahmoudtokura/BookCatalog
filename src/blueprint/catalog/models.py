from src import db
from datetime import datetime

class Publication(db.Model):

    __tablename__ = 'publications'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)


    def __init__(self, name:str):
        self.name = name

    def __repr__(self):
        return f'<Publication {self.name}>'


    def save(self):
        db.session.add(self)
        db.session.commit()
        return self.name


class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False, index=True)
    author = db.Column(db.String(80))
    avg_rating = db.Column(db.Float)
    format = db.Column(db.String(80))
    image = db.Column(db.String(80), unique=True)
    num_pages = db.Column(db.Integer)
    pub_date = db.Column(db.DateTime, default=datetime.utcnow())


    #Relationship
    publication_id = db.Column(db.Integer, db.ForeignKey('publications.id'), nullable=False)
    publication = db.relationship('Publication', backref=db.backref('books', lazy=True))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'<Book {self.title}>'

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self.name


