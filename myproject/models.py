# myproject/models.py
from myproject import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)


class Users(db.Model, UserMixin):

    __tablename__ = "Users"

    id              = db.Column(db.Integer, primary_key=True)
    #profile_image   = db.Column(db.String(64), nullable=False, default='default_profile.jpg')
    #email           = db.Column(db.String(64), unique=True, index=True)
    username        = db.Column(db.String(64), unique=True, index=True)
    password_hash   = db.Column(db.String(128), nullable=False)
    

    #One to many - Admin can add many sarees
    JKSarees = db.relationship('JKSarees', backref='author', lazy=True)

    def __init__(self, username, password):
        #self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)


    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


    def __repr__(self):
        return f"username: {self.username}"


class JKSarees(db.Model):

    __tablename__ = "JKSarees"

    Users   = db.relationship(Users)

    id      = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    date    = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    provider = db.Column(db.String(140), nullable=False)
    category   = db.Column(db.String(140), nullable=False)
    subCategory   = db.Column(db.String(140), nullable=False)
    img_name = db.Column(db.Text, nullable=False, default='default_profile.jpg')
    image   = db.Column(db.Text, nullable=False)

    Users = db.relationship('Users', back_populates="JKSarees")


    def __init__(self, user_id, provider, category, subCategory, img_name, image):
        self.user_id = user_id
        self.provider = provider
        self.category = category
        self.subCategory = subCategory
        self.img_name = img_name
        self.image = image