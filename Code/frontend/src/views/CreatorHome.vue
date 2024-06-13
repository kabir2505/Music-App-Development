<template>
    <div>
        <Navbar userRole='creator'>
             <template v-slot:add_song>
                
            <upload_song></upload_song>
             </template>

             <template v-slot:add_album>
                add album
                </template>
            hello
        </Navbar>
        <!-- <router-link :to="{ path: '/all_songs/300' }">songs</router-link> -->
   
       
    <div class="main2">
        <!-- //main2 is a grid -->
        <!-- consists of: A->stats(songs,rating,albums)
                     B->few songs C->few albums
                     *add respective buttons/router-links for few songs and few albums
                     to redirect them to all -->
        <div style="display:flex;justify-content:center;margin-top:1.5rem;color:#4c4e4d"><h2><em>Statistics</em></h2></div>
        <hr color="yellow">
        <div class="stats">
            <div class="song_count">
                        <div class="card" style="width: 18rem;">
                            <div class="card-body" style="display:flex;justify-content:center;">
                                <h5 class="card-title" style="text-align:center;background-color:yellow;width:10rem;font-size:2rem;display:flex;justify-content:center;"> {{stats.song_count}} songs</h5>
                            </div>
                        </div>
             

            </div>
            <div class="avg_ratings">
                 <div class="card" style="width: 18rem;">
                            <div class="card-body" style="display:flex;justify-content:center;">
                                <h5 class="card-title" style="text-align:center;background-color:yellow;width:10rem;font-size:2rem;display:flex;justify-content:center;">  {{stats.avg_ratings}} rating</h5>
                            </div>
                        </div>
             
                  

            </div>
            <div class="album_count">
                      <div class="card" style="width: 18rem;">
                            <div class="card-body" style="display:flex;justify-content:center;">
                                <h5 class="card-title" style="text-align:center;background-color:yellow;width:10rem;font-size:2rem;display:flex;justify-content:center;">    {{stats.album_count}} albums</h5>
                            </div>
                        </div>
                 
                
            </div>
            

        </div>
        <hr>


        <div class="top_songs">
            
                 <div class="bordered-word">
                <h2><em>Your top Songs</em></h2>
               
                <hr>
                </div>
                 <button style="background-color:yellow;color:color: #606362;margin-right:0rem"> <router-link to="/all_songs/300" style="color: #606362;">all your songs</router-link></button>
                    <ul class="grid_div">

                        <div class="card" style="width: 18rem;border-radius:40px;height:25rem;" v-for="(song,index) in topsongs" :key=index >
                            <img class="card-img-top"  alt="Card image cap"  :src="song && song.song_cover ? song.song_cover : ' '"
 style="height:20em;">
                            <div class="card-body" style="background-color:#f3f4f6;height:30em">
                                <h3 class="card-title" style="display:flex;justify-content:space-between;height:20%"><div style="font-size:1.5rem;">{{ song && song.song_name ? song.song_name: ''}}   </div>             
                                    <div><button style="border:none;" @click="playAudio(song)"><span class="mdi mdi-play-box" style="color: blue; font-size: 1.8rem; position:relative;"  ></span></button></div>
                                    </h3>

                                <p class="card-text" style="margin-top:15px;">
                                    <div class="1" style="display:grid;grid-template-columns:repeat(2,1fr);gap:0.5rem;">
                                    <div class="attri2" style="background-color:#e5e7eb;text-align:center;">artist:<b>{{ song && song.artist_name?song.artist_name:''}}</b></div>
                                    <div class="attri3" style="background-color:#e5e7eb;text-align:center;"><b>{{ song && song.song_genre?song.song_genre:''}}</b></div>
                                    <div  class="attri4" style="background-color:#e5e7eb;text-align:center;display:flex;justify-content:center;align-items:center"><b>{{ song && song.ratings?song.ratings:''}}❤️</b></div>
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
                            
                                    </div>
                                </p>

                                <div class="c_one" v-if="cred.user_role=='creator'&&  song && song.artist_name" style="display:flex;gap:3.5rem;">
                                    
                                        <button>  <Editsong :Song-Id=song.sid :SongName="song.song_name" :song=song></Editsong></button>
                                        
                                     
                                           <button @click="deletesong(song.sid)">Delete</button>

                                </div>
                              <!-- for search, take the params and add search-yes in the data: v-if=search=true -->
                                   
                                   
                               
                            </div>
                        </div>

                        



                
                    </ul>
   


        </div>
        <hr>

        <div class="top_albums">
            

             <div class="bordered-word">

            <h1><em>Albums</em></h1>
            <hr>
            
            </div>
                <button style="background-color:yellow;color:color: #606362;margin-right:0rem"> <router-link to="/all_albums/300" style="color: #606362;">all your albums</router-link></button>
                    <ul class="grid_div">

                    <div class="card" style="width: 18rem;border-radius:40px;height:25rem;" v-for="(album,index) in creato_albums" :key=index >
                        <img class="card-img-top"  alt="Card image cap"  src=" " style="height:20em;">
                        <div class="card-body" style="background-color:#f3f4f6;height:20em">
                            <h3 class="card-title" style="display:flex;justify-content:space-between;margin-bottom:2rem;height:40%">
                                <div style="display:flex;flex-direction:column">
                                    <div class="datetime" style="font-size:0.8rem;">{{getMonthandYear(album.date_uploaded)}}</div>
                                    <div style="width:80px;font-size:1.5rem;">{{album.alb_name}}</div>   
                                </div>          
                                <div><button style="border:none;" @click="playCollection(album)"><span class="mdi mdi-play-box" style="color: blue; font-size: 1.4rem; position:relative;"  ></span></button></div>
                                </h3>
                                <hr>

                            <p class="card-text" style="margin-top:15px;">
                                
                                <div class="1" style="display:grid;grid-template-columns:repeat(2,1fr);gap:0.5rem;">
                                <div class="attri2" style="background-color:#e5e7eb;text-align:center;">artist:<b>{{ }}</b></div>
                            <div class="attri2" style="background-color:#e5e7eb;text-align:center;"><b> <router-link :to="`/album_song/300/${album.a_id}`">Songs</router-link></b></div>
                                       
                                            
                                            <!-- <div v-if=="song.flag"></div> -->
                                             
                                                
                                                  
                                                <button  @click="deletealbum(album.a_id)">delete</button>
                                                
                                              
                                                    
                                             
                                            <button >   <router-link :to="'/edit_album/'+album.a_id">Edit</router-link></button>
                                              
                                          
                                <!-- new way to bind links to href tag -->

            
                                </div>
                                
                            </p>
                        </div>
                    </div>



            
                </ul>











        </div>

    </div>

          <AudioPlayer></AudioPlayer>

    </div>
</template>

<script>
import upload_song from '@/components/upload_song.vue'
import Navbar from '@/components/Navbar.vue'
import Editsong from '@/components/edit_song.vue'
import AudioPlayer from '@/components/AudioPlayer.vue'

export default {
    name:'CreatorHome',
    data(){
        return{
            cred:{
                user_role:localStorage.getItem('role'),
                user_uid:localStorage.getItem('uid'),
               authtoken:localStorage.getItem('auth-token')
            },
            message:"",
            stats:{
                song_count:0,
                avg_ratings:0,
                album_count:0
            },
            creator_songs:[],
            topsongs:[],
            creato_albums:[],
            topalbums:[]
        }

    },
    components:{
        upload_song,
        Navbar,
        Editsong,
        AudioPlayer
       
    },
    methods:{
         playCollection(collection){
            console.log("onecheck in all_albums")
            this.$store.dispatch('playCollection',collection)
         },
            async deletealbum(al_id){
            const res=await fetch(`http://localhost:5000/api/all_albums/${al_id}`,{
                method:'DELETE',
                headers:{
                       'Authentication-Token':this.cred.authtoken,
                        'User-Role':this.cred.user_role,
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
         getMonthandYear(date){
            return date.substring(7,11)+''+date.substring(11,16)
        },

         async deletesong(songid){
            const res=await fetch(`http://localhost:5000/api/all_songs/${songid}`,{
                method:'DELETE',
                headers:{
                       'Authentication-Token':this.cred.authtoken,
                        'User-Role':this.cred.user_role
                },
            })
            const data=await res.json().catch((e)=>{})
            if (res.ok){
            console.log("data",data)
            alert(data.message)
            this.message=data.message
             setTimeout(()=>{
            window.location.reload();
            },1000)
            }else{
            this.message=data.message
            }
            

            


    },
      playAudio(song){

            this.$store.dispatch('playTrack',song)
            //console.log(song)->>works
         }},


   async mounted(){
        // console.log('gello')
        // console.log('role',this.cred.user_role)
        if (this.cred.user_role=='norm_user'){
            
             let uid=this.cred.user_uid
             console.log(uid)
             const res=await fetch("http://localhost:5000/change_role/creator",{
                  method: 'GET',  // Adjust the HTTP method if needed
            headers: {
                'Content-Type': 'application/json',
                'uid':this.cred.user_uid,
                'Authentication-Token': this.cred.authtoken,

            },
             })

             const data= await res.json()
             //console.log(data)
             if (res.ok){
                alert(data.message)
                localStorage.setItem('role','creator')
             }else{
                alert('nah bruh')
             }

        }


        if(this.cred.user_role=="creator"){

            try{
                let res2=await fetch(`http://localhost:5000/creator_page/${this.cred.user_uid}`,{
                      method: 'GET',  // Adjust the HTTP method if needed
            headers: {
                'Content-Type': 'application/json',
                'uid':this.cred.user_uid,
                'Authentication-Token': this.cred.authtoken,
                'role':this.cred.user_role

            },
                })


            let data=await res2.json()
            if (res2.ok){
            //    console.log(data.avg_rating)
            //    console.log(data.song_count)
            //    console.log(data.album_count)
                this.stats.song_count=data.song_count
                this.stats.album_count=data.album_count
                this.stats.avg_ratings=data.avg_rating
                

            }




            }catch(e){
                 console.log(e)
            }


        }

        // fetch top songs
           const res3=await fetch(`http://localhost:5000/api/${this.cred.user_uid}/all_songs`,{
               headers:{
                'Authentication-Token':this.cred.authtoken,
                
                
            }
        })

        const data=await res3.json().catch((e)=>{})
        if (res3.ok){
            this.creator_songs=data
        if (this.creator_songs){
                    console.log('hello',this.creator_songs[0])

          
            if (data.length>0 && data[0].song_name){
              
            this.creator_songs.forEach(element => {
                console.log(element,'element')
                element.song_cover= `http://localhost:5000/uploads/${element.sid}`
                element.song_audio=`http://localhost:5000/songs/${element.sid}/audio`
            
                
            }
            )}else{this.creator_songs=''}}
            if (this.creator_songs.length >0){

            this.topsongs=this.creator_songs=this.creator_songs.sort((a,b)=>b.ratings-a.ratings)}


        }


         const res4=await fetch(`http://localhost:5000/api/${this.cred.user_uid}/all_albums`,
        {
             headers:{
                'Authentication-Token':this.cred.authtoken,
                
            },

        }     )
     


        const data2=await res4.json().catch((e)=>{})
         if (res4.ok){
            console.log(data2)
            this.creato_albums=data2
            
            this.creato_albums.forEach(element=>{
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

@import url('https://fonts.googleapis.com/css2?family=Fira+Sans:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');

*{
    font-family: "Fira Sans", sans-serif;
}
fira-sans-medium {
  font-family: "Fira Sans", sans-serif;
  font-weight: 500;
  font-style: normal;
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
    grid-template-columns: repeat(4,1fr);
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

</style>