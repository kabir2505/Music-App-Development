from flask_security import SQLAlchemyUserDatastore
from .models import db, Users, Roles
datastore = SQLAlchemyUserDatastore(db, Users, Roles)