from flask_restful import Resource, Api, fields, marshal_with, reqparse,abort
from app.__init__ import db
#from .. import api
from ..models import Songs,Users,Playlists
import datetime
import pytz
from flask_security import current_user,roles_required, auth_required,roles_required
from flask import jsonify,make_response,request


def abort_if_playlist_dne():
    abort(404,message="No playlists present!")
def abort_if_no_creator():
    abort(404,message="There does not exist any creator with such creator_id")
def abort_artist():
    abort(404,message="artist does not have an playlist")

def deleted(pl_id):
        return {"message": f"Playlist deleted successfully"}
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
    "pid":fields.Integer,
    "pl_name":fields.String,
    "song":fields.List(fields.Nested(song_fields)),
    "maker":fields.Integer
    
}

class Api_Playlists(Resource):
    @auth_required("token") 
    @marshal_with(resource_fields)
    def get(self,creator_id,pl_id=None):
        print('creato',creator_id)
        print('play',pl_id)
        print("<h1>hello</h1>")
        maker_=Users.query.get(creator_id)
        print(maker_)

        all_playlists=Playlists.query.filter_by(maker=creator_id).all()
        # print(all_playlists)
        # print(all_playlists)
        if len(all_playlists)==0:
            
            abort_if_playlist_dne()
        if pl_id:
            playlist=Playlists.query.get(pl_id)
            if playlist:
                return playlist
            else:
                  return make_response(jsonify({"message": f"Album with ID {pl_id} not found"}), 404)
        return all_playlists
    
    @auth_required("token")       
    def delete(self,pl_id):
        to_delete=Playlists.query.get(pl_id)

        if to_delete:
            db.session.delete(to_delete)
            db.session.commit()
            return make_response(jsonify(deleted(pl_id)),200)
        else:
            
            return make_response(jsonify({"message": f"Playlist with ID {pl_id} not found"}), 404)
        
    def post(self,creator_id):
        data=request.get_json()
       
        playlist_name=data.get('playlist_name','')
        song_ids=data.get('checkedNames',[])
         #print(song_ids)
        new_playlist=Playlists(pl_name=playlist_name,maker=creator_id)
         #new_album.song is a list
        db.session.add(new_playlist)
        for id in song_ids:
            
            add_song=Songs.query.get(id)
            if add_song:
                new_playlist.song.append(add_song)
            else:
                return make_response(jsonify({"error": f"Song not found"}), 404)
                  
        db.session.commit()
         #print(new_album)
        return make_response(jsonify({"message": f"Playlist successfully uploaded!"}), 201)
    
    def put(self,pl_id):
        playlist=Playlists.query.get(pl_id)
        data=request.get_json()

    
        updated_name=data.get('playlist_name','')
        updated_songids=data.get('checkedNames',[])
        #print(song_ids)
      
        #new_album.song is a list
        if updated_name:
            playlist.pl_name=updated_name

        for songs in playlist.song:
           if songs.sid not in updated_songids:
              db.session.delete(songs)

         

          
         
                
        db.session.commit()
        #print(new_album)
        return make_response(jsonify({"message": f"Playlist successfully updated!"}), 201)