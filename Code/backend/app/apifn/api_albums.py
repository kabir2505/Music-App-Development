from flask_restful import Resource, Api, fields, marshal_with, reqparse,abort
from app.__init__ import db
#from .. import api
from ..models import Songs,Users,Albums,Playlists
import datetime
import pytz
from flask_security import current_user,roles_required, auth_required,roles_required
from flask import jsonify,make_response,request
# #to parse incomin 
# parser=reqparse.RequestParser()
# parser.add_argument('alb_name',type=str,help="name of the song required",required=True)
# parser.add_argument('date_uploaded',type=datetime,help="type of genre required",required=True)

# parser.add_argument('flag',type=bool,help="flag please",required=False)
# parser.add_argument('active',type=bool,help="active or not ",required=False)
# parser.add_argument('lyrics',type=str,help='lyrics required')

def abort_if_album_dne():
    abort(404,message="No albums present!")
def abort_if_no_creator():
    abort(404,message="There does not exist any creator with such creator_id")
def abort_artist():
    abort(404,message="artist does not have an album")

def deleted(al_id):
        return {"message": f"Album with ID {al_id} deleted successfully"}
song_fields={
    "sid":fields.Integer,
    "song_name":fields.String,
    "song_genre":fields.String,
    "date_uploaded":fields.DateTime,
    "creator_id":fields.Integer,
    "lyrics":fields.String,
     'ratings':fields.Integer,
      'artist_name':fields.String,
}
resource_fields={
    "a_id":fields.Integer,
    "alb_name":fields.String,
    "date_uploaded":fields.DateTime,
    "song":fields.List(fields.Nested(song_fields)),
    "creator_id":fields.Integer,
     'flag':fields.Boolean,

    
}


class Api_Albums(Resource):
    @auth_required("token")
    @marshal_with(resource_fields)
    def get(self,creator_id=None,album_id=None):
        print("<h1>hello</h1>")
        all_albums=Albums.query.all()
        
        if len(all_albums)==0:
            
            abort_if_album_dne()
           
            
        if creator_id is None and album_id is None:
                return Albums.query.all()
     
        
        if creator_id is None:
            if album_id:
                album=Albums.query.get(album_id)
                if album:
                    return album
                else:
                    abort_if_album_dne()
                  
        else:
            user=Users.query.get(creator_id)
            if user:
                album=Albums.query.filter_by(creator_id=creator_id).all()
                if album:
                    print(album)
                    return album

                else:
                  abort_artist()
            else:
                    return abort_if_no_creator()
            
    
    @auth_required("token")       
    def delete(self,album_id):
        to_delete=Albums.query.get(album_id)

        if to_delete:
            db.session.delete(to_delete)
            db.session.commit()
            return make_response(jsonify(deleted(album_id)),200)
        else:
            
            return make_response(jsonify({"message": f"Album with ID {album_id} not found"}), 404)
        
    def post(self,creator_id):
         data=request.get_json()
       
         album_name=data.get('album_name','')
         song_ids=data.get('checkedNames',[])
         #print(song_ids)
         new_album=Albums(alb_name=album_name,creator_id=creator_id)
         #new_album.song is a list
         db.session.add(new_album)
         for id in song_ids:
              add_song=Songs.query.get(id)
              if add_song:
                new_album.song.append(add_song)
              else:
                    return make_response(jsonify({"error": f"Song not found"}), 404)
                  
         db.session.commit()
         #print(new_album)
         return make_response(jsonify({"message": f"Album successfully uploaded!"}), 201)
    
    def put(self,album_id):
        album=Albums.query.get(album_id)
        data=request.get_json()

    
        updated_name=data.get('album_name','')
        updated_songids=data.get('checkedNames',[])
        #print(song_ids)
      
        #new_album.song is a list
        if updated_name:
            album.alb_name=updated_name

        for songs in album.song:
           if songs.sid not in updated_songids:
              db.session.delete(songs)

         

          
         
                
        db.session.commit()
        #print(new_album)
        return make_response(jsonify({"message": f"Album successfully updated!"}), 201)

    #put req: A->get the new name and the updated songs(list)
    #(B)->loop through the list, delete songs not available in the updated list and db.commit

         

     
    
 