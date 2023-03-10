# from datetime import datetime
#
from blog import db
from flask_login import UserMixin
#
#
# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))
#
#
class User(db.Model, UserMixin):
#
#     __tablename__ = "user"

     id = db.Column(db.Integer, primary_key=True)
     username = db.Column(db.String(20), unique=True, nullable=False)
     email = db.Column(db.String(120), unique=True, nullable=False)
     image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
     password = db.Column(db.String(60), nullable=False)
     last_seen = db.Column(db.DateTime)

     def __repr__(self):
         return f'User({self.id}, {self.username}, {self.email}, {self.password}, {self.image_file})'


