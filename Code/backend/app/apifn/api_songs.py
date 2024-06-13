from flask_restful import Resource, Api, fields, marshal_with, reqparse,abort
from app.__init__ import db
#from .. import api
import base64
from ..models import Songs,Users
import datetime
import pytz
from flask_security import current_user,roles_required, auth_required,roles_required
from flask import jsonify,make_response,request
from ..instances import cache
#to parse incomin 
parser=reqparse.RequestParser()
parser.add_argument('song_name',type=str,help="name of the song required",required=True)
parser.add_argument('song_genre',type=str,help="type of genre required",required=True)
parser.add_argument('artist_name',type=str,help="name of the artist required",required=True)
parser.add_argument('ratings',type=int,help="ratings please",required=False)
parser.add_argument('flag',type=bool,help="flag please",required=False)
parser.add_argument('active',type=bool,help="active or not ",required=False)
parser.add_argument('lyrics',type=str,help='lyrics required')

def abort_if_song_dne():
    abort(404,message="no songs found ")
def abort_if_no_creator():
    abort(404,message="There does not exist any creator with such creator_id")
def deleted(song_id):
        return {"message": f"song with ID {song_id} deleted successfully"}
song_resource_fields={

 'sid':fields.Integer,
 'song_name':fields.String,
 'song_genre':fields.String,
 'artist_name':fields.String,
 'ratings':fields.Integer,
 'lyrics':fields.String,
 'flag':fields.Boolean,
 'album_id':fields.Integer,
#   'song_audio': fields.String(attribute=lambda x: base64.b64encode(x.song_audio).decode('utf-8') if x.song_audio else None),
#  'song_audio':fields.String(attribute=lambda x: base64.b64encode(x.song_audio).decode('utf-8') if x.song_audio else None),
 # 'song_cover': fields.String(attribute=lambda x: base64.b64encode(x.song_cover).decode('utf-8') if x.song_cover else None),
#     'song_audio': fields.String(attribute=lambda x: x.song_audio.decode('utf-8') if x.song_audio else None),
 


}


class Api_Songs(Resource):
    @auth_required("token")

    @marshal_with(song_resource_fields)
    @cache.cached(timeout=60)
    def get(self,creator_id=None,song_id=None):

        all_songs=Songs.query.all()
        

        if len(all_songs)==0:
            abort_if_song_dne()
         
        if creator_id is None and song_id is None:
            # for song in all_songs:
            #     song.song_audio = base64.b64encode(song.song_audio).decode('utf-8') if song.song_audio else None
            #     song.song_cover = base64.b64encode(song.song_cover).decode('utf-8') if song.song_cover else None
            return all_songs
        
        if song_id:
            song=Songs.query.get(song_id)
            if song:
                return song
            else:
                return abort_if_song_dne()
        if creator_id:
            songs=Songs.query.filter_by(creator_id=creator_id).all()
          
            if songs:
                
                #print(songs)
                
                return songs
            else:
                return make_response(jsonify({"message":"no songs found"}),400)

        
    @auth_required("token")
    def post(self):
        song_name = request.form.get('song_name')
        song_genre=request.form.get('song_genre')
        artist_name=request.form.get('artist_name')
        lyrics=request.form.get('lyrics')
        song_cover=request.files.get('song_cover')
        song_audio=request.files.get('song_audio')
        #to get data out of the headers
       
      
        artist_id=request.headers.get('artistid')
       
       
        
        try:
            song_cover=song_cover.read()
            song_audio=song_audio.read()
        except:
            return make_response(jsonify({"message":"doesnot work"}))
            
        new_song=Songs(song_name=song_name,song_genre=song_genre,artist_name=artist_name,lyrics=lyrics,song_cover=song_cover,song_audio=song_audio,creator_id=artist_id)



        try:
            db.session.add(new_song)
            db.session.commit()
            print('done')

            return make_response(jsonify({"message":"song added successfully"}),200)
        except:
            return make_response(jsonify({"message":"song no[e] successfully"}))

    @auth_required("token")
    def delete(self,song_id):
        to_delete=Songs.query.get(song_id)

        if to_delete:
            db.session.delete(to_delete)
            db.session.commit()
            return make_response(jsonify(deleted(song_id)),200)
        else:
            return make_response(jsonify({"message": f"User with ID {song_id} not found"}), 404)
        
    @auth_required("token")
    def put(self,song_id):
        #song_name, song_genre, artist_name, song_genre , lyrics , song_cover, song_audio
        
        song_name = request.form.get('song_name')
        print(song_name,'is the song name')
        song_genre=request.form.get('song_genre')
       
        lyrics=request.form.get('lyrics')
        song_cover=request.files.get('song_cover')
        song_audio=request.files.get('song_audio')

        song_update=Songs.query.get(song_id)
        print('song_name',song_name)
        if song_name:
            song_update.song_name=song_name
        if song_genre:
            song_update.song_genre=song_genre
        if lyrics:
            song_update.lyrics=lyrics
        if song_cover:
                try:
                    song_cover=song_cover.read()
                    song_update.song_cover=song_cover
                except:
                        return make_response(jsonify({"message":"does not work, wrong song cover format"}),400)

                
        if song_audio:
            try:
                song_audio=song_cover.read()
                song_update.song_cover=song_cover
            except:
                return make_response(jsonify({"message":"does not work, wrong song audio format"}),400)
            
        
        db.session.commit()
        return make_response(jsonify({"message":"song updated successfully"}),200)



        
        


     
    