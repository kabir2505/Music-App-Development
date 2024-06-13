<template>
<div class="main">

   <Navbar userRole='user' type='three'></Navbar>
    <div class="bordered-word">
       
            <h1><em>All Playlists</em></h1>
            <hr>
            
            </div>
                
                    <ul class="grid_div">

                    <div class="card" style="width: 18rem;border-radius:40px;height:25rem;" v-for="(playlist,index) in creator.creato_playlists" :key=index >
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
                                                <div class="attri2" style="background-color:#e5e7eb;text-align:center;"><b> <router-link :to="`/edit_playlist/${playlist.pid}`">edit</router-link></b></div>
                                          
                                <!-- new way to bind links to href tag -->

            
                                </div>
                                
                            </p>
                        </div>
                    </div>



            
                </ul>





            <!-- <div>{{message}}</div>
            <div id="example"> 
                delete album example works fine!

                <button v-on:click="playCollection(allAlbums[1])">play</button>
            </div> -->
 <AudioPlayer></AudioPlayer>
            </div>






    
</template>

<script>
 import AudioPlayer from '@/components/AudioPlayer.vue'
import Navbar from '@/components/Navbar.vue'
export default {
    name:'All_playlists',
     data(){
        return{
        allPlaylists:[],
        token:localStorage.getItem('auth-token'),
        role:localStorage.getItem('role'),
        message:null,
        uid:localStorage.getItem('uid'),
        creator:{
            creato_playlists:[]
        },
      
        }
    },
      components:{
        AudioPlayer,
        Navbar
       
    },

    methods:{
         async deleteplaylist(pl_id){
            const res=await fetch(`http://localhost:5000/api/all_playlists/${pl_id}`,{
                method:'DELETE',
                headers:{
                       'Authentication-Token':this.token,
                        'User-Role':this.role
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
           playCollection(collection){
            //console.log("onecheck in all_albums")
            this.$store.dispatch('playCollection',collection)
         },

         shuffleCollection(collection){
            console.log(collection)
            this.$store.dispatch('shuffleCollection',collection)
         }



    },
    async mounted(){

       const res2=await fetch(`http://localhost:5000/api/${this.uid}/all_playlists`,
        {
             headers:{
                'Authentication-Token':this.token,
                
            },

        }     )
        console.log(res2)


        const data2=await res2.json().catch((e)=>{})
         if (res2.ok){
            console.log(data2)
            this.creator.creato_playlists=data2
            if (this.creator.creato_playlists[0].pl_name){
            this.creator.creato_playlists.forEach(element=>{
                let allsongs=element.song
                allsongs.forEach(song=>{
                    song.song_cover=`http://localhost:5000/uploads/${song.sid}`
                    song.song_audio=`http://localhost:5000/songs/${song.sid}/audio`

                })})}
            }
        else{
            this.message=data2.message
            
        }

         }
        
   

    }

    

</script>

<style scoped>

@import url('https://fonts.googleapis.com/css2?family=Fira+Sans:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
.fira-sans-medium {
  font-family: "Fira Sans", sans-serif;
  font-weight: 500;
  font-style: normal;
}

*{
     font-family: "Fira Sans", sans-serif;

}


.grid_div{

    height:100%;
    width:100vw;
    display: grid;
    grid-template-columns: repeat(4,1fr);
    grid-gap:1.2rem;
    background-color:aliceblue;
    padding:5rem;
    padding-bottom: 6rem;
    



}


.bordered-word {
    color: #606362;
    
    margin-top: 1.5rem;
    display: flex;
    justify-content: center;}


.grid_div .card{

height:100%;

}
.attri2:hover  , .attri3:hover , .attri4:hover{
    box-shadow: rgba(0, 0, 0, 0.25) 0px 54px 55px, rgba(0, 0, 0, 0.12) 0px -12px 30px, rgba(0, 0, 0, 0.12) 0px 4px 6px, rgba(0, 0, 0, 0.17) 0px 12px 13px, rgba(0, 0, 0, 0.09) 0px -3px 5px;

}


.datetime{
    color:rgb(88, 87, 87);
    font-size: 0.9rem;
}

</style>