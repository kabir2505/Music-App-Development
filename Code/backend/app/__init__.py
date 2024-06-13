from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_security import SQLAlchemyUserDatastore,Security
from os import path
from flask_restful import Api,Resource,reqparse
#from .uploadini import create_database
from flask_migrate import Migrate
#from config import DevelopmentConfig
from .config import DevelopmentConfig
from .models import db
from flask_cors import CORS 
from .sec import datastore
from .instances import cache


#db=SQLAlchemy()
DB_NAME="database.db"

def create_app():

    app=Flask(__name__) #required so flask knows where to look for resources(templates/files)
    #app.config['SECRET_KEY']='sjfkjsdfkjsdf'
    app.config.from_object(DevelopmentConfig)
   # app.config['SQLALCHEMY_DATABASE_URI']=f'sqlite:///{DB_NAME}'
    #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    CORS(app)

   
    migrate=Migrate(app,db)
    api=Api(app)
    db.init_app(app)
   
    api.init_app(app)

    from .models import Users,Songs,Albums,Association,Playlists,Roles,RolesUsers

    #datastore=SQLAlchemyUserDatastore(db,Users,Roles)
    app.security=Security(app,datastore)
    cache.init_app(app)


    #registering the blueprints
    from .views import views
    from .auth import auth
    from .apifn.api_songs import Api_Songs
    from .apifn.api_users import Api_Users
    from .apifn.api_albums import Api_Albums
    from .apifn.api_playlists import Api_Playlists
    app.register_blueprint(views,url_prefix="/")
    app.register_blueprint(auth,url_prefix="/")

    api.add_resource(Api_Songs,"/api/all_songs","/api/<int:creator_id>/all_songs","/api/all_songs/<int:song_id>")
    api.add_resource(Api_Users,"/api/all_users","/api/all_users/<int:user_id>")
    api.add_resource(Api_Albums,"/api/all_albums","/api/all_albums/<int:album_id>","/api/<int:creator_id>/all_albums")
    api.add_resource(Api_Playlists,"/api/all_playlists","/api/all_playlists/<int:pl_id>","/api/<int:creator_id>/all_playlists","/api/<int:creator_id>/all_playlists/<int:pl_id>")
   #from .models import Users,Songs,Albums,Association,Playlists,Roles,RolesUsers
   
   
    #create_database(app)
  
    return app


#def create_database(app):
    if not path.exists("Code/instance/" + DB_NAME):
        with app.app_context():
            print('created now')
            db.create_all()






# def create_database(app):
#     try:
#         if not path.exists("Code/" + DB_NAME):
#             if not path.exists(path.join("Code",DB_NAME)):
#                 with app.app_context():
#                     try:
#                         print('created now')
#                         db.create_all()
#                     except:
#                         print('not able to create')
#         else:
#             print('already exists')

#     except:
#         print('already exists')





  