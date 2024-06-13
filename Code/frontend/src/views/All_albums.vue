<template>
   <!-- particular albums 
    1/if the req is from a user: display all albums w/o any footer tag except rate
    2/ if the req is from a creator: display all soalbum  with the edit footer and delete album->
    3/if the req is from an admin:display all albums with a flag song at the footer 
    
     -->


<div class="main">

<div v-if="wishd==100">
                <Navbar  v-if="role=='creator'|| role=='norm_user'" userRole='user' type='three'></Navbar>
                 <Navbar v-if="role === 'admin'"  userRole='admin' ></Navbar>
                    <!-- <button v-on:click="deletealbum()">delete_album</button> -->
            <!-- <div>{{allAlbums}}</div> -->
            <div class="bordered-word">
            <h1><em>Albums</em></h1>
            <hr>
            
            </div>
                    <ul class="grid_div">

                    <div class="card" style="width: 18rem;border-radius:40px;height:25rem;" v-for="(album,index) in allAlbums" :key=index >
                        <img class="card-img-top"  alt="Card image cap"  src=" " style="height:20em;">
                        <div class="card-body" style="background-color:#f3f4f6;height:20em">
                            <h3 class="card-title" style="display:flex;justify-content:space-between;margin-bottom:2rem;height:40%">
                                <div style="display:flex;flex-direction:column">
                                    <div class="datetime">{{getMonthandYear(album.date_uploaded)}}</div>
                                    <div style="font-size:1.5rem;">{{album.alb_name}}</div>   
                                </div>          
                                <div v-if="!album.flag"><button style="border:none;" @click="playCollection(album)"><span class="mdi mdi-play-box" style="color: blue; font-size: 1.4rem; position:relative;"  ></span></button></div>
                                <div v-if="album.flag" style="font-size:0.8rem;background-color:red;height:0.8rem;"> album flagged!</div>
                                </h3>
                                <hr>

                            <p class="card-text" style="margin-top:15px;">
                                
                                <div class="1" style="display:grid;grid-template-columns:repeat(2,1fr);gap:0.5rem;">
                                    
                                <div class="attri2" style="background-color:#e5e7eb;text-align:center;"><b>{{album.song[0].artist_name }}</b></div>
                                <div v-if="!album.flag" class="attri2" style="background-color:#e5e7eb;text-align:center;"><b> <router-link :to="`/album_song/100/${album.a_id}`">Songs</router-link></b></div>
                                <div v-if="album.flag">-</div>

                                     <div class="flagu" v-if="role==='norm_user' || role=='creator'">
                                         <div v-if="album.flagu">

                                               <button type="submit" @click="flagualbum(album.a_id)">un-flag!</button>
                                            </div>
                                            
                                        <div v-if="!album.flagu">
                                            
                                            <button type="submit" @click="flagualbum(album.a_id)">flag!</button>
                                        </div>
                                       
                                    </div>






                                        <div class="flag" v-if="role=='admin'" style="display:flex;justify-content:space-between;">
                                            
                                            <!-- <div v-if=="song.flag"></div> -->
                                                <div v-if="album.flag">
                                                
                                                  
                                                    <button type="submit" @click="flagalbum(album.a_id)">un-flag!</button>
                                                    </div>
                                                <div v-if="!album.flag">
                                                    
                                             
                                                <button type="submit" @click="flagalbum(album.a_id)">flag!</button>
                                                </div>
                                                <button  @click="deletealbum(album.a_id)">delete</button>
                                            </div>
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

            </div>



    <div class="creato_albums" v-if="wishd==300">
      
         <div class="bordered-word">
            <h1><em>Albums</em></h1>
            <hr>
            
            </div>
                    <ul class="grid_div">

                    <div class="card" style="width: 18rem;border-radius:40px;height:25rem;" v-for="(album,index) in creator.creato_albums" :key=index >
                        <img class="card-img-top"  alt="Card image cap"  src=" " style="height:20em;">
                        <div class="card-body" style="background-color:#f3f4f6;height:20em">
                            <h3 class="card-title" style="display:flex;justify-content:space-between;margin-bottom:2rem;height:40%">
                                <div style="display:flex;flex-direction:column">
                                    <div class="datetime">{{getMonthandYear(album.date_uploaded)}}</div>
                                    <div style="width:80px;font-size:1.5rem;">{{album.alb_name}}</div>   
                                </div>          
                                <div v-if="!album.flag"><button style="border:none;" @click="playCollection(album)"><span class="mdi mdi-play-box" style="color: blue; font-size: 1.4rem; position:relative;"  ></span></button></div>
                                <div v-if="album.flag" style="font-size:0.8rem;background-color:red;height:0.7rem;">album flagged!</div>
                                </h3>
                                <hr>

                            <p class="card-text" style="margin-top:15px;">
                                
                                <div class="1" style="display:grid;grid-template-columns:repeat(2,1fr);gap:0.5rem;">
                                <div class="attri2" style="background-color:#e5e7eb;text-align:center;"><b>{{album.song[0].artist_name }}</b></div>
                                <div class="attri2" style="background-color:#e5e7eb;text-align:center;"><b> <router-link :to="`/album_song/${album.a_id}`">Songs</router-link></b></div>
                                       
                                            
                                            <!-- <div v-if=="song.flag"></div> -->
                                             
                                                
                                                  
                                                <button  @click="deletealbum(album.a_id)">delete</button>
                                                
                                              
                                                    
                                             
                                            <button >   <router-link :to="'/edit_album/'+album.a_id">Edit</router-link></button>
                                              
                                          
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

            







    </div>
    <AudioPlayer></AudioPlayer>






</div>
</template>

<script>
 import AudioPlayer from '@/components/AudioPlayer.vue'
import Navbar from '@/components/Navbar.vue'
export default {
    name:'All_Albums',
    data(){
        return{
        allAlbums:[],
        token:localStorage.getItem('auth-token'),
        role:localStorage.getItem('role'),
        message:null,
        uid:localStorage.getItem('uid'),
        creator:{
            creato_albums:[]
        },
      
        }
    },
    components:{
        AudioPlayer,
        Navbar
       
    },
      computed:{
      wishd(){
        return this.$route.params.wish
      }},
    async mounted(){
        const res=await fetch("http://localhost:5000/api/all_albums",{
            headers:{
                'Authentication-Token':this.token,
                
            },
        })
        const data=await res.json().catch((e)=>{})
        if (res.ok){
            console.log(data)
            this.allAlbums=data
            this.allAlbums.forEach(element=>{
                let allsongs=element.song
                allsongs.forEach(song=>{
                    song.song_cover=`http://localhost:5000/uploads/${song.sid}`
                    song.song_audio=`http://localhost:5000/songs/${song.sid}/audio`

                })})
            }
        else{
            this.message=data.message
            
        }
         if (this.$route.params.wish==300 && this.role=='creator'){
          
        const res2=await fetch(`http://localhost:5000/api/${this.uid}/all_albums`,
        {
             headers:{
                'Authentication-Token':this.token,
                
            },

        }     )
        console.log(res2)


        const data2=await res2.json().catch((e)=>{})
         if (res2.ok){
            console.log(data2)
            this.creator.creato_albums=data2
            
            this.creator.creato_albums.forEach(element=>{
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
        
   

    },
    methods:{

             async flagualbum(albumid){
            //pass the song id through the url->receive it in the backend, if the song is unflag, flag it and if flag->unflag it, display the necessary changes on the template.

             try{
            let res=await fetch(`http://localhost:5000/flagu_album/${albumid}`,
            {
                method:'POST',
                headers:{
                     
                     'Authentication-Token':this.token,
                     
                
                },
               

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
            




        getMonthandYear(date){
            return date.substring(7,11)+''+date.substring(11,16)
        }

        ,
         async deletealbum(al_id){
            const res=await fetch(`http://localhost:5000/api/all_albums/${al_id}`,{
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
            console.log("onecheck in all_albums")
            this.$store.dispatch('playCollection',collection)
         },
         async flagalbum(albumid){
            //pass the album id through the url->receive it in the backend, if the song is unflag, flag it and if flag->unflag it, display the necessary changes on the template.

             try{
            let res=await fetch(`http://localhost:5000/flag_album/${albumid}`,
            {
                method:'POST',
                headers:{
                     
                     'Authentication-Token':this.token,
                     'role':this.role
                
                },
               

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