from flask_restful import Resource, Api, fields, marshal_with, reqparse,abort
from app.__init__ import db
#from .. import api
from ..models import Songs,Users
import datetime
import pytz
from flask import jsonify,make_response
from flask_security import current_user,roles_required, auth_required,roles_required
def deleted(user_id):
  
        return {"message": f"User with ID {user_id} deleted successfully"}
  

parser=reqparse.RequestParser()
parser.add_argument('uname',type=str,help="name of the user required",required=True)
parser.add_argument('email',type=str,help="email required",required=True)
parser.add_argument('active',type=bool,help="status required")


user_resource_fields={

 'uid':fields.Integer,
 'uname':fields.String,
 'email':fields.String,
 'active':fields.Boolean,
}

class Api_Users(Resource):
    @marshal_with(user_resource_fields)
    @auth_required("token")
    
    def get(self,user_id=None):
        print(user_id)
        all_users=Users.query.all()
       
        if len(all_users)==0:
            return jsonify({"message":"no users found!"},404)
        # for i in all_users:
        #     print(i.uid)
        if user_id:
             user=Users.query.get(user_id)
             print(user)
             return user
        return all_users
    
    @auth_required("token")
    @roles_required("admin")

    def delete(self,user_id):
        to_delete=Users.query.get(user_id)

        if to_delete:
            db.session.delete(to_delete)
            db.session.commit()
            return make_response(jsonify(deleted(user_id)),200)

            
        else:
            return make_response(jsonify({"message": f"User with ID {user_id} not found"}), 404)
        
