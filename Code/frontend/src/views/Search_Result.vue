<template>
   <div class="main">
     <Navbar userRole="user" type="two" ></Navbar>
    <!-- <div class="search" >
            <form  @submit.prevent="search"  id="formElem">
            <input type="search" name="search_" id="search_" placeholder="Search" width="10" v-model="new_query">
            <button type="submit" ><span class="mdi mdi-magnify"></span></button>
            </form>
                      

        </div>
      -->
    <div class="bordered_word">
    <h3>Song result:</h3>
    
    </div>
   

        <div class="songs_" v-if="songs_exist()">
             <ul class="grid_div">

                        <div class="card" style="width: 18rem;border-radius:40px;height:25rem;" v-for="(song,index) in songs" :key=index >
                            <img class="card-img-top"  alt="Card image cap"  :src="song && song.song_cover ? song.song_cover : ' '"
 style="height:20em;">
                            <div class="card-body" style="background-color:#f3f4f6;height:30em">
                                <h3 class="card-title" style="display:flex;justify-content:space-between;height:20%"><div style="width:60px;font-size:1.5rem;">{{ song && song.song_name ? song.song_name: ''}}   </div>             
                                    <div><button style="border:none;" @click="playAudio(song)"><span class="mdi mdi-play-box" style="color: blue; font-size: 1.8rem; position:relative;"  >Listen</span></button></div>
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


                                    
                                  
                                        
                                     
                                         

                             
                              <!-- for search, take the params and add search-yes in the data: v-if=search=true -->
                                   
                                   
                               
                            </div>
                        </div>

                        



                
                    </ul>
   
    

   </div>
   <div v-if="!songs_exist()">
    No results
   </div>

    <div class="bordered_word">
       <h3>Playlist result:</h3>
    </div>

   <div class="playlists_"  v-if="playlists_exist()"> 
       <ul class="grid_div">

                    <div class="card" style="width: 18rem;border-radius:40px;height:25rem;" v-for="(playlist,index) in playlists" :key=index >
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
     <div v-if="!playlists_exist()" >
    <h4 style="display:flex;justify-content:center">No results</h4>
   </div>
     <div class="bordered_word">
      <h3>Album result:</h3>
    </div>
   <div class="albums_"  v-if="albums_exist()">
      <ul class="grid_div">

                    <div class="card" style="width: 18rem;border-radius:40px;height:25rem;" v-for="(album,index) in albums" :key=index >
                        <img class="card-img-top"  alt="Card image cap"  src=" " style="height:20em;">
                        <div class="card-body" style="background-color:#f3f4f6;height:20em">
                            <h3 class="card-title" style="display:flex;justify-content:space-between;margin-bottom:2rem;height:40%">
                                <div style="display:flex;flex-direction:column">
                                   
                                    <div style="width:80px;font-size:1.5rem;">{{album.alb_name}}</div>   
                                </div>          
                                <div><button style="border:none;" @click="playCollection(album)"><span class="mdi mdi-play-box" style="color: blue; font-size: 1.4rem; position:relative;"  >Listen</span></button></div>
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
    <div v-if="!albums_exist()"  >
    <h4 style="display:flex;justify-content:center">No results</h4>
   </div>
    <AudioPlayer></AudioPlayer>
</div>
</template>
<style scoped>

/* .main{
    height:100vh;
    width:100vw;

} */
.search{
    width:100vw;
    display:flex;
    justify-content: center;
}
input[id="search_"]{
    width:25rem;
    text-align: center;
    border-color:blue;


}
.bordered_word {
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

</style>
<script>
import Navbar from '@/components/Navbar.vue'
import AudioPlayer from '@/components/AudioPlayer.vue'
export default {
    name:'Search_Result',
    data(){
        return{
            query:"",
            uid:localStorage.getItem('uid'),
            response:{},
            songs:[],
            albums:[],
            playlists:[],
            new_query:""


        }
    },


    components:{
        Navbar,
        AudioPlayer

    },
    methods:{
         shuffleCollection(collection){
            console.log(collection)
            this.$store.dispatch('shuffleCollection',collection)
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



        
        songs_exist(){
        
            return this.songs.length>0
            
        },
         playlists_exist(){
        
            return this.playlists.length>0
            
        },
         albums_exist(){
        
            return this.albums.length>0
            
        },



        

        search(){
            
            this.$router.push({path:'/search_result',query:{query:this.new_query}})
        


}}
    ,


  
    async mounted(){
        

        this.query=this.$route.query.query
        if (this.new_query){
             this.query=this.new_query

        }

        let res1= await fetch(`http://localhost:5000/search_result/${this.uid}/${this.query}`)

       let data=await res1.json().catch((e)=>{})
        if (res1.ok){
            this.songs=data.songs;
            this.albums=data.albums;
            this.playlists=data.playlists;

             this.songs.forEach(element => {
                console.log(element,'element')
                element.song_cover= `http://localhost:5000/uploads/${element.sid}`
                element.song_audio=`http://localhost:5000/songs/${element.sid}/audio`
            
                
            }
            )

         this.albums.forEach(element=>{
                let allsongs=element.song
                if (allsongs){
                      allsongs.forEach(song=>{
                    song.song_cover=`http://localhost:5000/uploads/${song.sid}`
                    song.song_audio=`http://localhost:5000/songs/${song.sid}/audio`

                })
                }
              })

                  this.playlists.forEach(element=>{
                let allsongs=element.song
                allsongs.forEach(song=>{
                    song.song_cover=`http://localhost:5000/uploads/${song.sid}`
                    song.song_audio=`http://localhost:5000/songs/${song.sid}/audio`

                })})
            
            
            
            }else{this.songs=''
        }

            





    }
}
</script>