from flask import Blueprint,jsonify,request,send_file,make_response,jsonify,render_template
from .models import Songs,Users,RolesUsers,Roles,Albums,Playlists
from flask_security import auth_required,roles_required,login_required,logout_user,current_user,login_user
from app.__init__ import db
from werkzeug.security import check_password_hash,generate_password_hash
views=Blueprint('views',__name__)  #setting up a blueprint for the app
from app.sec import datastore
from sqlalchemy import func,or_
# from main import datastore
from datetime import datetime
from collections import defaultdict
import io
import os
from werkzeug.utils import secure_filename
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
#celery
from celery.result import AsyncResult
from .tasks import say_hello,add
from .instances import cache
from .apifn.api_songs import song_resource_fields




@views.route('/')
def home():
    return "<h1>test</h1>"



@views.get('/admin')
@auth_required("token")
@roles_required("admin")
def admin():
    return 'welcome admin'


#to activate a user


@views.get('/activate/user/<int:user_id>')
@auth_required("token")
@roles_required("admin")
def activate_user(user_id):
    user=Users.query.get(user_id)
    if not user.active:
       
        if not user:
            return jsonify({"message":"User not found"}),404
        
        user.active=True
        db.session.commit()
        return jsonify({"message":"Activated"})
    else:
        user=Users.query.get(user_id)
        user.active=False
        db.session.commit()
        return jsonify({"message":"Activated"})



#to get the authentication token (admin/creator/user)
@views.post('/user-login')
def user_login():
    data=request.get_json()
    email=data.get('email')
    if not email:
        
        return jsonify({"message":"email not provided"}),400
    
    user=datastore.find_user(email=email)
    if not user:
        #print('no email user mane')
        return jsonify({"message":"email not found"}),404


    if not user.active:
        return make_response(jsonify({"message":"your account has been withheld!"}),401)

    if check_password_hash(user.password,data.get("password")):
        try:
            user.last_login = datetime.utcnow()
            db.session.commit()
            login_user(user)

        except:
            print('not logged in')
    
        return jsonify({"token":user.get_auth_token(),"uid":user.uid,"email":user.email,"role":user.roles[0].name}),200
    else:
        return jsonify({"message":"wrong password"}),400
    
@views.post('/user-signup')
def user_signup():
   
    data=request.get_json()
    email=data.get('email')
    uname=data.get('uname')
    password=data.get('password')
    
    #
    if not email:
        return jsonify({"message":"email not provided"}),400
    if not uname:
        return jsonify({"message":"name not provided"}),400
    
    
    if not datastore.find_user(email=email):
        #
        new_user= datastore.create_user(email=email,uname=uname,password=generate_password_hash(password))
        #
        datastore.add_role_to_user(new_user,'norm_user')
        
        db.session.commit()
        
    
        return jsonify({"message":"user registered successfully!!Please Login!"},200)
    else:
        return jsonify({'message':'email already exists!Please use a different email'},400)
    
@views.route('/user-logout', methods=['POST'])
@login_required
def user_logout():
    logout_user()
    return jsonify({"message": "Logout successful"}), 201
    
    
    
    

@views.route('/uploads/<sid>')
def uploaded_file(sid):
    song = Songs.query.get(sid)
      
    if song:
        return send_file(io.BytesIO(song.song_cover), mimetype='image/jpeg')
    else:
        return 'Song not found'

@views.route('/songs/<int:song_id>/audio')
@cache.cached(timeout=60)
def get_audio(song_id):
    song = Songs.query.get(song_id)
    if song:
        return send_file(io.BytesIO(song.song_audio), mimetype='audio/mp3')
    else:
        return 'Song not found'
    
@views.route('/change_role/creator')
@auth_required("token")
def change_role():
    uid=request.headers.get('uid')
    print(uid)
    user=Users.query.get(uid)
    print(user)

    if user is None:
        return make_response(jsonify({'message':'no user found'}),404)
    else:
         print(user.roles)
         roles=Roles.query.all()
         for i in roles:
             if i.name=='creator':
                 print(i)
                 user.roles=[i]
                 db.session.commit()
         return make_response(jsonify({"message":"Yay! You have been registered as a creator now!"}),201)
     
    

@views.post('/rate_song/<int:songid>')
@auth_required("token")
def rate_song(songid):
  
    song=Songs.query.get(songid)
    if song:
        rating=request.form.get("rating")
        rating=float(rating)
        song.ratings=(song.ratings*song.numof_ratings+rating)
        song.numof_ratings+=1
        if song.numof_ratings>0:
             song.ratings=round(song.ratings/song.numof_ratings)
        db.session.commit()
        return make_response(jsonify({"message":"thank you for the review!"}),201)


    else:
          return make_response(jsonify({"errorm":"no such song found"}),400)


@views.post('/flag_song/<int:song_id>')
@auth_required("token")
@roles_required("admin")
def flag_song(song_id):
      
      song=Songs.query.get(song_id)
      if song:
          if song.flag:
             song.flag=False
             db.session.commit()
             return make_response(jsonify({"message":"song un-flagged!"}),201)
          else:
              song.flag=True
              db.session.commit()
              return make_response(jsonify({"message":"song flagged!"}),201)
          
@views.post('/flagu_song/<int:song_id>')
@auth_required("token")
def flagu_song(song_id):
      
      song=Songs.query.get(song_id)
      if song:
          if song.flagu:
             song.flagu=False
             db.session.commit()
             return make_response(jsonify({"message":"song un-flagged!"}),201)
          else:
              song.flagu=True
              db.session.commit()
              return make_response(jsonify({"message":"song flagged!"}),201)

@views.post('/flag_album/<int:albumid>')
@auth_required("token")
@roles_required("admin")
def flag_album(albumid):
    
      album=Albums.query.get(albumid)
      if album:
          if album.flag:
             album.flag=False
             db.session.commit()
             return make_response(jsonify({"message":"album un-flagged!"}),201)
          else:
              album.flag=True
              db.session.commit()
              return make_response(jsonify({"message":"album flagged!"}),201)

@views.post('/flagu_album/<int:albumid>')
@auth_required("token")
def flagu_album(albumid):
    
      album=Albums.query.get(albumid)
      if album:
          if album.flagu:
             album.flagu=False
             db.session.commit()
             return make_response(jsonify({"message":"album un-flagged!"}),201)
          else:
              album.flagu=True
              db.session.commit()
              return make_response(jsonify({"message":"album flagged!"}),201)




@views.get('/creator_page/<int:id>')
@auth_required("token")
@roles_required("creator")
def creator_page(id):
    creator=Users.query.get(id)
    if creator:
        songs=creator.songs
        song_count=len(songs)
        album_count=len(creator.albums)
        avg_rating=average_rating = db.session.query(func.avg(Songs.ratings)).filter(Songs.creator_id ==creator.uid).scalar()
        if avg_rating is not None:
            avg_rating = round(avg_rating, 1)
        
        response_object={
            "message":"successful stats",
            "song_count":song_count,
            "album_count":album_count,
            "avg_rating":avg_rating,

        }

        return make_response(jsonify(response_object),201)

@views.get('/admin_info')
def admin_info():
    song_count=Songs.query.count()
    album_count=Albums.query.count()
    user_count=Users.query.count()
    top_songs=Songs.query.order_by(Songs.ratings.desc()).limit(8).all()

    user_active=Users.query.filter(Users.active==True).count()
    song_active=Songs.query.filter(Songs.flag==False).count()
    album_active=Albums.query.filter(Albums.flag==False).count()
    user_flag=Users.query.filter(Users.active==False).count()
    song_flag=Songs.query.filter(Songs.flag==True).count()
    album_flag=Albums.query.filter(Albums.flag==True).count()
    all_songs=Songs.query.all()
    song_data=defaultdict(int)
    for song in all_songs:
        if song.date_uploaded:
            upload_month_year=song.date_uploaded.strftime('%Y-%m')
            song_data[upload_month_year]+=1
    sorted_data=sorted(song_data.items())

    months=[date for date,one in sorted_data]
    counts=[count for one,count in sorted_data]

    users=Users.query.limit(1).all()
    admins = Users.query.join(Users.roles).filter(Roles.name == 'admin').count()
    

    creators=Users.query.join(Users.roles).filter(Roles.name == 'creator').count()
    norm_users=Users.query.join(Users.roles).filter(Roles.name == 'norm_user').count()
    distri=[norm_users,admins,creators]
    labels=['norm_user','admin','creator']
    
    all_users=Users.query.all()
    user_data=defaultdict(int)
    for user in all_users:
        if user.date_registered:
            date_registered=user.date_registered.strftime('%Y-%m')
            user_data[date_registered]+=1
    sorted_user_data=sorted(user_data.items())
    user_months=[date for date,one in sorted_user_data]
    user_counts=[count for one,count in sorted_user_data]


    unique_genres={}
    for song in all_songs:
        if song.song_genre:
            unique_genres[song.song_genre]=0
        unique_genres[song.song_genre]+=1
    
    #{'hola': 1, 'two': 1, '444two33': 1, '444two33.  jj': 1, 'asfas': 1, 'sasfasf': 1, 'newone': 1, 'rafadafd': 1}
      
           
   

    response_data={
        "song_count":song_count,
        "album_count":album_count,
        "user_count":user_count,
        "user_active":user_active,
        "song_active":song_active,
        "album_active":album_active,
        "user_flag":user_flag,
        "song_flag":song_flag,
        "album_flag":album_flag,
        "song_bar":{
            "months":months,
            "counts":counts
        },

        "role_pie":{
            "distri":distri,
            "labels":labels
        },
        "user_line":{
            "user_months":user_months,
            "user_counts":user_counts
        },
        "unique_genre":unique_genres,
    }
    return make_response(jsonify(response_data),201)

@roles_required('admin')
@views.get('/ranking')
def ranking():
       
    top_songs=Songs.query.order_by(Songs.ratings.desc()).limit(10).all()

    top_songs_=[{
        "song_name":song.song_name,
        "artist":song.artist_name,
        "ratings":song.ratings

    } for song in top_songs]
    print(top_songs)
    return jsonify(top_songs_)

# @roles_required('admin')
@views.get('/creator_rank')
def creator_rank():
    creators=Users.query.join(Users.roles).filter(Roles.name == 'creator')
    top_c=[]
    for creator in creators:
        d={}
        d["uname"]=creator.uname
        
        avg_rating=average_rating = db.session.query(func.avg(Songs.ratings)).filter(Songs.creator_id ==creator.uid).scalar()
        if avg_rating is not None:
            avg_rating = round(avg_rating, 1)
        d['avg_rating']=avg_rating
    
        songs=Songs.query.filter_by(creator_id=creator.uid).count()
        d['total_songs']=songs
        top_c.append(d)
    
    top_creators=[{
          "artist_name":creator["uname"],
          "total_uploads":creator["total_songs"],
        "avg_rating":creator["avg_rating"]
        


    } for creator in top_c]
    def get_avg_rating(creator):
        return creator['avg_rating'] or 0
    top_creators_sorted = sorted(top_creators, key=get_avg_rating, reverse=True)

    return jsonify(top_creators_sorted)


    





@views.get('/say_hello')
def say_hello_view():
    res=say_hello.delay()
    return jsonify({"task_id":res.id})

@views.get("/add/<int:a>/<int:b>")
def add_together(a,b):
    res=add.delay(a,b)
    return {"result_id":res.id}






@views.get('/res/<id>')
def hell(id):
    res=AsyncResult(id)
    return{
        "ready":res.ready(),
        "successful":res.successful(),
        "value":res.result if res.ready() else None,
    }

@views.get("/result/<int:id>")
def add_Result(id):
    return "hello"
    res=AsyncResult(id)
    return{
        "ready":res.ready(),
        "successful":res.successful(),
        "value":res.result if res.ready() else None,
    }


#search albums,playlists, songs, songs/albums by artist, songs/albums by genre
@views.route("/search_result/<int:uid>/<query>")
def search_query(uid,query):
    albums=[]
    # print(uid)
    # print(query)
    #searching songs
    #based upon name , genre 
    songs = Songs.query.filter(or_(Songs.song_name.ilike(f'%{query}%'), Songs.song_genre.ilike(f'%{query}%'))).all()
    # print(songs)
    # if songs:
    #     print('hel yah songs')
    #songs by ratings
    songs_ratings=Songs.query.filter(Songs.ratings==query).all()
    # print('ratings',songs_ratings)


    #songs by creator name
        #using the join operator
    songs_creator=Songs.query.join(Users).filter(or_(Users.uname.ilike(f'%{query}%'))).all()
    # print(songs_creator)

    #album by name,genre
    albums = Albums.query.filter(or_(Albums.alb_name.ilike(f'%{query}%'), Albums.album_genre.ilike(f'%{query}%'))).all()
    # print(albums)

    #album by creator name
    albums_creator=Albums.query.join(Users).filter(or_(Users.uname.ilike(f'%{query}%'))).all()
    # print('album_Creator',albums_creator)
    #playlist by name
    playlists=Playlists.query.filter((Playlists.maker==uid) & Playlists.pl_name.ilike(f"%{query}%")).all()
    print(playlists)
    # print('playlist',playlists)
    
    song_resource_fields=[]
    album_resource_fields=[]
    playlist_resource=[]
    #playlist by genre
    response_data={}
    if songs:
        song_resource_fields=[{

        'sid':song.sid,
        'song_name':song.song_name,
        'song_genre':song.song_genre,
        'artist_name':song.artist_name,
        'ratings':song.ratings,
        'lyrics':song.lyrics,
        'flag':song.flag,
#   'song_audio': fields.String(attribute=lambda x: base64.b64encode(x.song_audio).decode('utf-8') if x.song_audio else None),
#  'song_audio':fields.String(attribute=lambda x: base64.b64encode(x.song_audio).decode('utf-8') if x.song_audio else None),
 # 'song_cover': fields.String(attribute=lambda x: base64.b64encode(x.song_cover).decode('utf-8') if x.song_cover else None),
#     'song_audio': fields.String(attribute=lambda x: x.song_audio.decode('utf-8') if x.song_audio else None),
 


    }for song in songs]
    if songs_ratings:
              song_resource_fields=[{

        'sid':song.sid,
        'song_name':song.song_name,
        'song_genre':song.song_genre,
        'artist_name':song.artist_name,
        'ratings':song.ratings,
        'lyrics':song.lyrics,
        'flag':song.flag,
#   'song_audio': fields.String(attribute=lambda x: base64.b64encode(x.song_audio).decode('utf-8') if x.song_audio else None),
#  'song_audio':fields.String(attribute=lambda x: base64.b64encode(x.song_audio).decode('utf-8') if x.song_audio else None),
 # 'song_cover': fields.String(attribute=lambda x: base64.b64encode(x.song_cover).decode('utf-8') if x.song_cover else None),
#     'song_audio': fields.String(attribute=lambda x: x.song_audio.decode('utf-8') if x.song_audio else None),
 


    }for song in songs_ratings]
        
       
    if songs_creator:
             song_resource_fields=[{

        'sid':song.sid,
        'song_name':song.song_name,
        'song_genre':song.song_genre,
        'artist_name':song.artist_name,
        'ratings':song.ratings,
        'lyrics':song.lyrics,
        'flag':song.flag,
#   'song_audio': fields.String(attribute=lambda x: base64.b64encode(x.song_audio).decode('utf-8') if x.song_audio else None),
#  'song_audio':fields.String(attribute=lambda x: base64.b64encode(x.song_audio).decode('utf-8') if x.song_audio else None),
 # 'song_cover': fields.String(attribute=lambda x: base64.b64encode(x.song_cover).decode('utf-8') if x.song_cover else None),
#     'song_audio': fields.String(attribute=lambda x: x.song_audio.decode('utf-8') if x.song_audio else None),
 


    }for song in songs_creator]
    if albums:
        print(albums)
        album_resource_fields = [
    {
        'a_id': album.a_id,
        'alb_name': album.alb_name,
        'date_uploaded': album.date_uploaded,
        'creator_id': album.creator_id,
        'flag': album.flag,
        'songs': [
            {
                'sid': song.sid,
                'song_name': song.song_name,
                'song_genre': song.song_genre,
                'artist_name': song.artist_name,
                'ratings': song.ratings,
                'lyrics': song.lyrics,
                'flag': song.flag,
              
            }
            for song in album.song  
        ]
    }
    for album in albums
]

        
    if albums_creator:
       album_resource_fields = [
    {
        'a_id': album.a_id,
        'alb_name': album.alb_name,
        'date_uploaded': album.date_uploaded,
        'creator_id': album.creator_id,
        'flag': album.flag,
        'songs': [
            {
                'sid': song.sid,
                'song_name': song.song_name,
                'song_genre': song.song_genre,
                'artist_name': song.artist_name,
                'ratings': song.ratings,
                'lyrics': song.lyrics,
                'flag': song.flag,
               
            }
            for song in album.song  
        ]
    }
    for album in albums_creator
]

    if playlists:
        playlist_resource=[{
    "pid":playlist.pid,
    "pl_name":playlist.pl_name,
    "song": [
         {
                'sid': song.sid,
                'song_name': song.song_name,
                'song_genre': song.song_genre,
                'artist_name': song.artist_name,
                'ratings': song.ratings,
                'lyrics': song.lyrics,
                'flag': song.flag,
              
            }
            for song in playlist.song 


    ],
    "maker":playlist.maker
    
    }for playlist in playlists]
       


    #json response for song
    
   



    
    # if album_resource_fields:
    #     return make_response(album_resource_fields)
    # else:
    #     return jsonify('None')

    return jsonify({"songs":song_resource_fields,"albums":album_resource_fields,"playlists":playlist_resource})





   
    return  make_response(jsonify(response_data),201)


    

    



# Ability to filter songs based on rating,
