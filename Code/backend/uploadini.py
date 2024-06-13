from os import path
#from . import db
from app.__init__ import create_app,db
#from .app.__init__ import app,db
#from app import create_app,db
from app.models import Roles,Users,roles_users

app=create_app()
with app.app_context():
    admin=Roles(id='admin',name='Admin',description='Admin description')
    db.session.add(admin)
    user=Roles(id='user',name='User',description='User description')
    db.session.add(user)
    creator=Roles(id='creator',name='Creator',description='Creator description')
    db.session.add(creator)
    db.session.commit()


if __name__=='__main__':
    app.run(debug=True)

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
