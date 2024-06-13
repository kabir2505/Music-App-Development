#to import from current dir
#from .__init__ import db
#from flask_login import UserMixin
from flask_security import UserMixin,RoleMixin
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class RolesUsers(db.Model,UserMixin):
    __tablename__ = 'roles_users'
    id=db.Column(db.Integer(),primary_key=True)
    user_id=db.Column('user_id',db.Integer(),db.ForeignKey('users.uid'))
    role_id = db.Column('role_id', db.Integer(), db.ForeignKey('roles.id'))
    

class Roles(db.Model,RoleMixin):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80))
    description=db.Column(db.String(255))


class Users(db.Model,UserMixin):
    uid=db.Column(db.Integer,primary_key=True)
    uname=db.Column(db.String(150))
    password=db.Column(db.String(300))
    email=db.Column(db.String(150))
    date_registered=db.Column(db.DateTime,default=datetime.utcnow)
    last_login=db.Column(db.DateTime,default=datetime.utcnow)
    active=db.Column(db.Boolean(),default=True)
    fs_uniquifier=db.Column(db.String(255),unique=True,nullable=False)
    playlists=db.relationship('Playlists',backref='author')
    songs=db.relationship('Songs',backref='singer')
    albums=db.relationship('Albums',backref='artist')
    roles=db.relationship('Roles',secondary="roles_users",backref=db.backref('users',lazy='dynamic'))

   
    



class Playlists(db.Model):
    pid=db.Column(db.Integer,primary_key=True)
    pl_name=db.Column(db.String(150))
    song=db.relationship('Songs',backref='playl',secondary="association")
    maker=db.Column(db.Integer,db.ForeignKey("users.uid"))


class Songs(db.Model):
    sid=db.Column(db.Integer,primary_key=True)
    song_name=db.Column(db.String(60),nullable=False)
    song_genre=db.Column(db.String(60))
    artist_name=db.Column(db.String(60))
    date_uploaded=db.Column(db.DateTime,default=datetime.utcnow)
    lyrics=db.Column(db.String(2000))
    ratings=db.Column(db.Float,default=0)
    numof_ratings=db.Column(db.Integer,default=0)
    song_cover=db.Column(db.LargeBinary)
    song_audio=db.Column(db.LargeBinary)
    creator_id=db.Column(db.Integer,db.ForeignKey("users.uid"))
    album_id=db.Column(db.Integer,db.ForeignKey("albums.a_id")) #removed unique=True for now

    flag=db.Column(db.Boolean,default=False)
    flagu=db.Column(db.Boolean,default=False)

class Albums(db.Model):
    a_id=db.Column(db.Integer,primary_key=True)
    alb_name=db.Column(db.String(60),nullable=False)
    date_uploaded=db.Column(db.DateTime,default=datetime.utcnow)
    creator_id=db.Column(db.Integer,db.ForeignKey("users.uid"))
    song=db.relationship('Songs',backref='alb')
    album_genre=db.Column(db.String(60))
    flag=db.Column(db.Boolean,default=False)
    flagu=db.Column(db.Boolean,default=False)

    


class Association(db.Model):
    as_id = db.Column(db.Integer, primary_key=True)
    sid=db.Column(db.Integer,db.ForeignKey("songs.sid"))
    pid=db.Column(db.Integer,db.ForeignKey("playlists.pid"))

   

