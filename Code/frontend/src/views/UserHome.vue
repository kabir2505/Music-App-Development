
<template>
<div class="main">
    <Navbar userRole="user" type="one" >
            <button v-on:click="logout()" style="height:1.8rem;">logout</button></Navbar>

        <div class="top_songs">
            
                 <div class="bordered-word">
                <h1><em> Top Songs</em></h1>
               
                <hr>
                </div>
                 <button style="background-color:yellow;color:color: #606362;margin-right:0rem"> <router-link to="/all_songs/100" style="color: #606362;">all songs</router-link></button>
                    <ul class="grid_div">

                        <div class="card" style="width: 15rem;border-radius:40px;height:20rem;" v-for="(song,index) in topsongs" :key=index >
                            <img class="card-img-top"  alt="Card image cap"  :src="song && song.song_cover ? song.song_cover : ' '"
 style="height:20em;">
                            <div class="card-body" style="background-color:#f3f4f6;height:40em">
                                <h2 class="card-title" style="display:flex;justify-content:space-between;align-items:flex-start;"><div style="font-size:1.5rem;whitespace:nowrap;">{{ song && song.song_name ? song.song_name: ''}}   </div>             
                                    <div><button style="border:none;" @click="playAudio(song)"><span class="mdi mdi-play-box" style="color: blue; font-size: 1.5rem; position:relative;"  ></span></button></div>
                                    </h2>

                                <p class="card-text" style="margin-top:15px;">
                                    <br>
                                    <div class="1" style="gap:0.5rem;">
                                        <div style="display:flex;justify-content:space-between;gap:1.5rem;whitespace:wrap;">
                                        <div class="attri2" style="background-color:#e5e7eb;text-align:center;whitespace:nowrap;"><b>{{ song && song.artist_name?song.artist_name:''}}</b></div>
                                        <div class="attri3" style="background-color:#e5e7eb;text-align:center;whitespace:nowrap;"><b>{{ song && song.song_genre?song.song_genre:''}}</b></div>
                                   
                                        <div  class="attri4" style="background-color:#e5e7eb;text-align:center;display:flex;justify-content:center;align-items:center;"><b>{{ song && song.ratings?song.ratings:''}}❤️</b></div>
                                      </div>
                                      <br>
                                      <div style="display:flex;gap:0.5rem;">
                                    <div class="lyics_modal">


                                        <!-- Button trigger modal -->
            <!-- Button trigger modal -->
            <button type="button" class="btn btn-primary" data-bs-toggle="modal" :data-bs-target="'#' + 'modal-' + index">
                Lyrics
            </button>
             

            <!-- Modal -->
            <div class="modal fade" :id="'modal-' + index" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" :id="'modal-title-' + index">
                        <div style="display:flex;justify-content:center">{{ song && song.name?song.song_name:''}}</div></h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <div style="display:flex;flex-direction:column;justify-content:center;align-items:center;color:#606362;background-color:aliceblue">
                    {{ song && song.lyrics?song.lyrics:''}}
                    
                    </div>
                  
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                
                </div>
                </div>
            </div>
            </div>

                                    
                    

                                    </div>
                                     <form action="#"  id="formElem"  @submit.prevent="ratesong(song.sid,$event.target) ">
                                    <div style="display:flex;justify-content:start;">
                    
                                             <input   name="rating"  href='#' class="btn btn-primary" id="number" type="number" placeholder="rate-song" style="margin-right:1.5rem;background-color:white;height:2rem;width:4.5rem;text-align:center;color:#606362" min=0 max=5></input>
                                            <button type="submit" >!</button>
                                    </div>
                                    </form>
                                    </div>
                            
                                    </div>
                                </p>

                       
                              <!-- for search, take the params and add search-yes in the data: v-if=search=true -->
                                   
                                   
                               
                            </div>
                        </div>

                        



                
                    </ul>
   


        </div>

      <div class="top_albums">
            

             <div class="bordered-word">

            <h1><em>Albums</em></h1>
            <hr>
            
            </div>
                <button style="background-color:yellow;color:color: #606362;margin-right:0rem"> <router-link to="/all_albums/100" style="color: #606362;">all albums</router-link></button>
                    <ul class="grid_div">

                    <div class="card" style="width: 18rem;border-radius:40px;height:25rem;" v-for="(album,index) in topalbums" :key=index >
                        <img class="card-img-top"  alt="Card image cap"  src=" " style="height:20em;">
                        <div class="card-body" style="background-color:#f3f4f6;height:20em">
                            <h3 class="card-title" style="display:flex;justify-content:space-between;margin-bottom:2rem;height:40%">
                                <div style="display:flex;flex-direction:column">
                                    <div class="datetime" style="font-size:0.9rem;">{{getMonthandYear(album.date_uploaded)}}</div>
                                    <div style="font-size:1.5rem;">{{album.alb_name}}</div>   
                                </div>          
                                <div><button style="border:none;" @click="playCollection(album)"><span class="mdi mdi-play-box" style="color: blue; font-size: 1.4rem; position:relative;"  ></span></button></div>
                                </h3>
                                <hr>

                            <p class="card-text" style="margin-top:15px;">
                                
                                <div class="1" style="display:grid;grid-template-columns:repeat(2,1fr);gap:0.5rem;">
                                <div class="attri2" style="background-color:#e5e7eb;text-align:center;">artist:<b>{{ }}</b></div>
                                <div class="attri2" style="background-color:#e5e7eb;text-align:center;"><b> <router-link :to="`/album_song/100/${album.a_id}`">Songs</router-link></b></div>
                                       
                                            
                                            <!-- <div v-if=="song.flag"></div> -->
                                             
                                                
                                                  
                                             
                                                
                                              
                                                    
                                             
                                          
                                              
                                          
                                <!-- new way to bind links to href tag -->

            
                                </div>
                                
                            </p>
                        </div>
                    </div>



            
                </ul>











        </div>


    <div class="playlists">
        <div style="display:flex; justify-content:space-between;">
           <button style="background-color:yellow;color:color: #606362;margin-right:0rem"> <router-link to="/upload_playlist" style="color: #606362;">upload playlist</router-link></button>
            <button style="background-color:yellow;color:color: #606362;margin-right:0rem"> <router-link to="/all_playlists" style="color: #606362;">all playlists</router-link></button>
        </div>

          <div class="bordered-word">

            <h1><em>Playlists</em></h1>
            <hr>
            
            </div>
              
                    <ul class="grid_div">

                    <div class="card" style="width: 18rem;border-radius:40px;height:25rem;" v-for="(playlist,index) in topplaylists" :key=index >
                        <img class="card-img-top"  alt="Card image cap"  src=" " style="height:20em;">
                        <div class="card-body" style="background-color:#f3f4f6;height:20em">
                            <h3 class="card-title" style="display:flex;justify-content:space-between;margin-bottom:2rem;height:40%">
                                <div style="display:flex;flex-direction:column">

                                    <div style="width:80px;font-size:1.5rem;">{{playlist.pl_name}}</div>   
                                </div>          
                                <div style="display:flex;flex-direction:column;gap:0.5rem;"><button style="border:none;" @click="playCollection(playlist)"><span class="mdi mdi-play-box" style="color: blue; font-size: 1.4rem; position:relative;"  ></span></button>
                                    <button style="height:2.1rem;" @click="shuffleCollection(playlist)"><span class="mdi mdi-shuffle"></span></button>
                                
                                
                                </div>
                                </h3>
                                <hr>

                            <p class="card-text" style="margin-top:15px;">
                                
                                <div class="1" style="display:grid;grid-template-columns:repeat(2,1fr);gap:0.5rem;">
                                <div class="attri2" style="background-color:#e5e7eb;text-align:center;">artist:<b>{{ }}</b></div>
                                <div class="attri2" style="background-color:#e5e7eb;text-align:center;"><b> <router-link :to="`/playlist_song/${playlist.pid}`">Songs</router-link></b></div>
                                       
                                            
                                            <!-- <div v-if=="song.flag"></div> -->
                                             
                                                
                                                  
                                                <button  @click="deleteplaylist(playlist.pid)">delete</button>
                                                
                                              
                                                    
                                             
                                            <button >   <router-link :to="'/edit_playlist/'+playlist.pid">Edit</router-link></button>
                                              
                                          
                                <!-- new way to bind links to href tag -->

            
                                </div>
                                
                            </p>
                        </div>
                    </div>



            
                </ul>








    </div>
              <AudioPlayer></AudioPlayer>

</div>





</template>

<script>
import AudioPlayer from '@/components/AudioPlayer.vue'
import Navbar from '@/components/Navbar.vue'

export default {
    name:"UserHome",
    data(){
            return{

                topsongs:[],
                topalbums:[],
                topplaylists:[],
                 cred:{
                user_role:localStorage.getItem('role'),
                user_uid:localStorage.getItem('uid'),
               authtoken:localStorage.getItem('auth-token')
            },
            
            
            }

    },
    
    components:{
        Navbar
        ,
        AudioPlayer
    },
    methods:{
         async deleteplaylist(pl_id){
            const res=await fetch(`http://localhost:5000/api/all_playlists/${pl_id}`,{
                method:'DELETE',
                headers:{
                       'Authentication-Token':this.cred.authtoken,
                        'User-Role':this.cred.user_role
                },
            })
            const data=await res.json().catch((e)=>{})
            if (res.ok){
            console.log("data",data)
            this.message=data.message
             alert(data.message)
            this.message=data.message
             setTimeout(()=>{
            window.location.reload()},1000)
            }else{
            this.message=data.message
            }

            

         },




          shuffleCollection(collection){
            console.log(collection)
            this.$store.dispatch('shuffleCollection',collection)
         },
           async ratesong(songid,formElem){
           
            try{
            let res=await fetch(`http://localhost:5000/rate_song/${songid}`,
            {
                method:'POST',
                headers:{
                     
                     'Authentication-Token':this.cred.authtoken,
                
                },
                body:new FormData(formElem)

            });
         
            if (res.ok){
                   const data=await res.json().catch((e)=>{})
            
            alert(data.message)
              setTimeout(()=>{
            window.location.reload();
            },1000)}else{ 
                   const data=await res.json().catch((e)=>{})
                console.log('errorhere')
                alert(data.errorm)}
            } catch(error){
                console.log('Fetch error:',error)
            }



         },

          playCollection(collection){
            console.log("onecheck in all_albums")
            this.$store.dispatch('playCollection',collection)
         },
          getMonthandYear(date){
            return date.substring(7,11)+''+date.substring(11,16)
        },
          playAudio(song){

            this.$store.dispatch('playTrack',song)
            //console.log(song)->>works
         },
        async logout(){
             const res=await fetch("http://localhost:5000/user-logout",{
                method:'POST',
                headers:{
                      'Authentication-Token':this.cred.authtoken,
                }
        })
        const data=await res.json().catch((e)=>{})
        if (res.ok){
            localStorage.clear();
            console.log("loggedout")
            this.$router.push('/')

        }else{
            alert("error")
        }
    }
    
},
async mounted(){

//fetch top songs
           const res3=await fetch(`http://localhost:5000/api/all_songs`,{
              headers:{
                       'Authentication-Token':this.cred.authtoken,
                        'User-Role':this.cred.user_role}
                
               
        })

        const data=await res3.json().catch((e)=>{})
        if (res3.ok){
            this.topsongs=data
            console.log('hello',this.topsongs)
          
            if (data[0].song_name){
              
            this.topsongs.forEach(element => {
                console.log(element,'element')
                element.song_cover= `http://localhost:5000/uploads/${element.sid}`
                element.song_audio=`http://localhost:5000/songs/${element.sid}/audio`
            
                
            }
            )}else{this.topsongs=''}

            this.topsongs=this.topsongs.sort((a,b)=>b.ratings-a.ratings)


        }



            const res4=await fetch(`http://localhost:5000/api/all_albums`,
        {
             headers:{
                'Authentication-Token':this.cred.authtoken,
                
            },

        }     )
     


        const data2=await res4.json().catch((e)=>{})
         if (res4.ok){
            console.log(data2)
            this.topalbums=data2
            
            this.topalbums.forEach(element=>{
                let allsongs=element.song
                allsongs.forEach(song=>{
                    song.song_cover=`http://localhost:5000/uploads/${song.sid}`
                    song.song_audio=`http://localhost:5000/songs/${song.sid}/audio`

                })})

               
            }
        else{
            this.message=data.message
            
        };


            const res5=await fetch(`http://localhost:5000/api/${this.cred.user_uid}/all_playlists`,
        {
             headers:{
                'Authentication-Token':this.cred.authtoken,
                
            },

        }     )
     


        const data3=await res5.json().catch((e)=>{})
         if (res5.ok){
            console.log(data3)
            this.topplaylists=data3
            
            this.topplaylists.forEach(element=>{
                let allsongs=element.song
                allsongs.forEach(song=>{
                    song.song_cover=`http://localhost:5000/uploads/${song.sid}`
                    song.song_audio=`http://localhost:5000/songs/${song.sid}/audio`

                })})

               
            }
        else{
            this.message=data.message
            
        }


        
        

}



}
</script>

<style scoped>



@import url('https://fonts.googleapis.com/css2?family=Secular+One&display=swap');
.secular-one-regular {
  font-family: "Secular One", sans-serif;
  font-weight: 400;
  font-style: normal;
}

*{
     font-family: "Secular One", sans-serif;

}
/* stats styling */
.stats{
    display:flex;
    justify-content: space-around;


}

/* top songs */
.bordered-word {
    color: #606362;

    margin-top: 1.5rem;
    display: flex;
    justify-content: center;}


.grid_div{

   
   
    display: grid;
    overflow-x:scroll;
    grid-template-columns: repeat(9,1fr);
    grid-gap:1rem;
    background-color:aliceblue;
    padding:4rem;
    padding-bottom: 6rem;
    

}

.grid_div .card{

height:100%;

}
.mdi{
    height:3.5rem;
}
.attri2:hover  , .attri3:hover , .attri4:hover{
    box-shadow: rgba(0, 0, 0, 0.25) 0px 54px 55px, rgba(0, 0, 0, 0.12) 0px -12px 30px, rgba(0, 0, 0, 0.12) 0px 4px 6px, rgba(0, 0, 0, 0.17) 0px 12px 13px, rgba(0, 0, 0, 0.09) 0px -3px 5px;
   
}

button[data-bs-toggle="modal"]{
    width:4.5rem;
    height:2rem;
    text-align: center;
    
}


</style>