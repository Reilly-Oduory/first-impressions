from . import db
from datetime import datetime

class Pitch(db.Model):

    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String)
    category = db.Column(db.String)
    content = db.Column(db.String)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    upvotes = db.Column(db.Integer)
    downvotes = db.Column(db.Integer)


    def __init__(self,title,category,content,date_created,upvotes = 0,downvotes = 0):
        self.title = title
        self.category = category
        self.content = content
        self.date_created = date_created
        self.upvotes = upvotes
        self.downvotes = downvotes

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_pitches(cls):
        Pitch.all_pitches.clear()

    @classmethod
    def get_pitches(cls):
        pitches = Pitch.query.all()
        
        return pitches


class User(db.Model):

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String)
    email = db.Column(db.String, unique = True, index = True)
    password = db.Column(db.String)


    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = password
