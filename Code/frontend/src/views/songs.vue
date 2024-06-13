<template>

   <!-- songs
    1/if the req is from a user: display all songs w rating  any footer tag
    2/ if the req is from a creator: display all  their songs with the edit and delete footer-> edit/song and edit    as well,
    3/if the req is from an admin:display all songs with a flag song at the footer 
    
     -->
<div class="main">
        

<div class="all_songsone">
        <div class="user-allsongs" v-if="wishd==100">
      <Navbar v-if="role === 'norm_user' || role === 'creator'" userRole="user" type="two"></Navbar>
        <Navbar v-if="role === 'admin'"  userRole='admin' ></Navbar>

        <hr>
        <div class="dropdown">
  <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
    Ratings
  </button>
  <ul class="dropdown-menu">
    <li><a class="dropdown-item " href="#" id="dall" @click="filt_rat(null)">all</a></li>
    <li><a class="dropdown-item " id="d1" href="#" @click="filt_rat(1)">1</a></li>
    <li><a class="dropdown-item dtwo" id="d2" href="#" @click="filt_rat(2)">2</a></li>
    <li><a class="dropdown-item dthree" id="d3" href="#" @click="filt_rat(3)">3</a></li>
    <li><a class="dropdown-item dfour" id="d4" href="#" @click="filt_rat(4)">4</a></li>
    <li><a class="dropdown-item dfive" id="d5" href="#" @click="filt_rat(5)">5</a></li>
  </ul>
</div>
        <div class="bordered-word">
                <h1><em>Songs</em></h1>
                <hr>
                </div>
                    <ul class="grid_div">

                        <div class="card" style="width: 18rem;border-radius:40px;height:25rem;" v-for="(song,index) in filtered_songs" :key=index  >
                            

                
                            <img class="card-img-top"  alt="Card image cap"  :src="song.song_cover?song.song_cover:' '" style="height:20em;">
                            <div class="card-body" style="background-color:#f3f4f6;height:30em">
                                <h3 class="card-title" style="display:flex;justify-content:space-between;height:20%"><div style="font-size:1.5rem;">{{song.song_name}}   </div>             
                                    <div v-if="!song.flag"><button style="border:none;" @click="playAudio(song)"><span class="mdi mdi-play-box" style="color: blue; font-size: 1.8rem; position:relative;"  ></span></button></div>
                                    <div v-if="song.flag" style="font-size:0.8rem;background-color:Red;height:0.9rem;">song flagged!</div>
                                    </h3>

                                <p class="card-text" style="margin-top:15px;">
                                    <div class="1" style="display:grid;grid-template-columns:repeat(2,1fr);gap:0.5rem;">
                                    <div class="attri2" style="background-color:#e5e7eb;text-align:center;"> <u><b>{{song.artist_name}}</b></u></div>
                                    <div class="attri3" style="background-color:#e5e7eb;text-align:center;"><b>{{song.song_genre}}</b></div>
                                    <div  class="attri4" style="background-color:#e5e7eb;text-align:center;display:flex;justify-content:center;align-items:center"><b>{{song.ratings}}❤️</b></div>
                                    <div class="lyics_modal" v-if="!song.flag">


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
                        <div style="display:flex;justify-content:center">{{song.song_name}}</div></h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <div style="display:flex;flex-direction:column;justify-content:center;align-items:center;color:#606362;background-color:aliceblue">
                    {{song.lyrics}}
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
                                <div style="display:flex;justify-content:space-between">
                                <form action="#"  id="formElem"  @submit.prevent="ratesong(song.sid,$event.target) " v-if="!song.flag">
                                    <div v-if="role=='creator' || role=='norm_user'">
                    
                                             <input   name="rating"  href='#' class="btn btn-primary" id="number" type="number" placeholder="rate-song" style="margin-right:1.5rem;background-color:white;height:2rem;width:4.5rem;text-align:center;color:#606362" min=0 max=5></input>
                                            <button type="submit" >rate!</button>
                                    </div>
                                   
                                </form>

                                    <div class="flagu" v-if="role==='norm_user' || role=='creator'">
                                         <div v-if="song.flagu">
                                               <button type="submit" @click="flagusong(song.sid)">un-ssflag!</button>
                                            </div>
                                            
                                        <div v-if="!song.flagu">
                                            
                                            <button type="submit" @click="flagusong(song.sid)">flag!</button>
                                        </div>
                                       
                                    </div>
                              </div>
                                    <div class="flag" v-if="role=='admin'">

                                    <!-- <div v-if=="song.flag"></div> -->
                                        <div v-if="song.flag">
                                               <button type="submit" @click="flagsong(song.sid)">un-flag!</button>
                                            </div>
                                        <div v-if="!song.flag">
                                        <button type="submit" @click="flagsong(song.sid)">flag!</button>
                                        </div>
                                          <button @click="deletesong(song.sid)">Delete</button>
                                    </div>
                                   
                               
                            </div>
                        </div>

                        



                
                    </ul>


            </div>

  </div>     

        <div class="creator_ownsongs" v-if="wishd==300 && creator_songs!=''">
            
          
               <div class="bordered-word">
                <h1><em>Your Songs</em></h1>
                <hr>
                </div>
                    <ul class="grid_div">

                        <div class="card" style="width: 18rem;border-radius:40px;height:25rem;" v-for="(song,index) in creator_songs" :key=index >
                            <img class="card-img-top"  alt="Card image cap"  :src="song && song.song_cover ? song.song_cover : ' '"
 style="height:20em;">
                            <div class="card-body" style="background-color:#f3f4f6;height:30em">
                                <h3 class="card-title" style="display:flex;justify-content:space-between;height:20%"><div style="font-size:1.5rem;">{{ song && song.song_name ? song.song_name: ''}}   </div>             
                                 
                                    <div v-if="!song.flag"><button style="border:none;" @click="playAudio(song)"><span class="mdi mdi-play-box" style="color: blue; font-size: 1.8rem; position:relative;"  ></span></button></div>
                                    <div v-if="song.flag" style="font-size:0.9rem;background-color:red;height:0.9rem;">song flagged!</div>
                                   
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

                                <div class="c_one" v-if="role=='creator'&&  song && song.artist_name" style="display:flex;gap:3.5rem;">
                                    
                                        <button>  <Editsong :Song-Id=song.sid :SongName="song.song_name" :song=song></Editsong></button>
                                        
                                       
                                           <button @click="deletesong(song.sid)">Delete</button>

                                </div>
                              <!-- for search, take the params and add search-yes in the data: v-if=search=true -->
                                   
                                   
                               
                            </div>
                        </div>

                        



                
                    </ul>
   

            


        </div>
        <div v-if="creator_songs=='' && wishd==300" style="display:flex;justify-content:center;font-size:4rem;">
            No songs available!
            
        </div>



      <AudioPlayer></AudioPlayer>



      </div>
   
   

</template>

<script>


import AudioPlayer from '@/components/AudioPlayer.vue'
import Navbar from '@/components/Navbar.vue'
import Editsong from '@/components/edit_song.vue'
export default {
    name:'songv',
    components:{AudioPlayer,Navbar, Editsong},
    data(){
        return{
         
        song_rating:0,
        allSongs:[],
        creator_songs:[],
        creator:{
            creator_songs:[],
            
        },
        filtered_songs:[],
        songsids:[],
        creator_songsids:[],
       
        token:localStorage.getItem('auth-token'),
        role:localStorage.getItem('role'),
        uid:localStorage.getItem('uid'),
        message:null,
        coverImageUrl: 'http://localhost:5000/uploads/6',
        audioUrl0:'http://localhost:5000/songs/12/audio'
      
        }
    },
    computed:{
      wishd(){
        return this.$route.params.wish
      }},
    async mounted(){
          if (this.$route.params.wish==100){
        const res=await fetch("http://localhost:5000/api/all_songs",{
            headers:{
                'Authentication-Token':this.token,
                
            },
        })
        const data=await res.json().catch((e)=>{})
        if (res.ok){
      
            console.log(data)
            this.allSongs=data
            
                console.log(this.allSongs.forEach(element => {
                console.log(element,'element')
                this.songsids.push(element.sid)


                element.song_cover= `http://localhost:5000/uploads/${element.sid}`
                element.song_audio=`http://localhost:5000/songs/${element.sid}/audio`
                
                
            }))
            this.filtered_songs=this.allSongs
        }else{
            this.message=data.message
        }
          }

        //if the router link is accessed by mysongs from the creator page and search results by user:
        if (this.$route.params.wish==300 && this.role=='creator'){

        const res2=await fetch(`http://localhost:5000/api/${this.uid}/all_songs`,{
               headers:{
                'Authentication-Token':this.token,
                
            }
        })

        const data=await res2.json().catch((e)=>{})
        if (res2.ok){
            this.creator_songs=data
            console.log('hello',this.creator_songs[0])
          
            if (data[0].song_name){
              
            this.creator_songs.forEach(element => {
                console.log(element,'element')
                element.song_cover= `http://localhost:5000/uploads/${element.sid}`
                element.song_audio=`http://localhost:5000/songs/${element.sid}/audio`
                this.creator_songsids.push(element.sid)
                
            })}else{this.creator_songs=''}

        }
        
        
        }

    },
     methods:{

        filt_rat(n){
           this.filtered_songs=n?this.allSongs.filter(song=>song.ratings===n):this.allSongs;


        },

        ownsongs(sid){

            if(this.creator_songsids.includes(sid)){
                return true
            }
            }
            


        ,
          getMonthandYear(date){
            return date.substring(7,11)+''+date.substring(11,16)
        },
         async deletesong(songid){
            const res=await fetch(`http://localhost:5000/api/all_songs/${songid}`,{
                method:'DELETE',
                headers:{
                       'Authentication-Token':this.token,
                        'User-Role':this.role
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
         },


         async ratesong(songid,formElem){
           
            try{
            let res=await fetch(`http://localhost:5000/rate_song/${songid}`,
            {
                method:'POST',
                headers:{
                     
                     'Authentication-Token':this.token,
                
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

         async flagsong(songid){
            //pass the song id through the url->receive it in the backend, if the song is unflag, flag it and if flag->unflag it, display the necessary changes on the template.

             try{
            let res=await fetch(`http://localhost:5000/flag_song/${songid}`,
            {
                method:'POST',
                headers:{
                     
                     'Authentication-Token':this.token,
                     'role':'admin'
                
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

             async flagusong(songid){
            //pass the song id through the url->receive it in the backend, if the song is unflag, flag it and if flag->unflag it, display the necessary changes on the template.

             try{
            let res=await fetch(`http://localhost:5000/flagu_song/${songid}`,
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



.bordered-word {
    color: #606362;

    margin-top: 1.5rem;
    display: flex;
    justify-content: center;}
.grid_div{

    height:100%;
    width:100vw;
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