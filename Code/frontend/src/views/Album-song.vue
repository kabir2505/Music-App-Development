<template>
    <!-- particular albums songs
    1/if the req is from a user: display all songs w/o any footer tag
    2/ if the req is from a creator: display all songs with the edit footer-> edit/song and edit album as well,
    3/if the req is from an admin:display all songs with a flag song at the footer 
    
     -->
    <div class="main">
       



         
    
      


    
        


          <div class="user-allsongs" v-if="wishd==100||300">
        <Navbar userRole="user" type="two"></Navbar>

         <div class="common">
            <!-- Album info
            Album image 
            Album name
            Album date
            Album song count
            Album creator name
            -->
            <div>
            <img src="https://media.newyorker.com/photos/644afa9f328537f70292b8df/master/w_1800,c_limit/Graphic1_Beat3_01.png" height=150px width=150px alt="">
            </div>

            <div class="alb">
            <div class="albone">
                <div>
                    <div class="datetime" style="font-size:1rem">{{getMonthandYear(date)}}</div>
                        
                </div>
                <div>
                    <div style="font-size:2rem"> <h2>{{allSongs.alb_name}}</h2></div>

                </div>
            </div>
            <div class="alb2">
                   <div><button style="border:none;" @click="playCollection(allSongs)"><span class="mdi mdi-play-box" style="color: blue; font-size: 1.4rem; position:relative;"  ></span></button></div>
                    <div  class="attr" style="background-color:#e5e7eb;text-align:center; "> <b>{{song_count}}</b> songs</div>
                    <div   class="attr" style="background-color:#e5e7eb;text-align:center;">artist-<b>{{artist_name}}</b></div>

            </div>
            </div>
           


        </div>
        <hr>
        <div class="bordered-word">
                <h1><em>Songs</em></h1>
                <hr>
                </div>
                    <ul class="grid_div">

                        <div class="card" style="width: 18rem;border-radius:40px;height:25rem;" v-for="(song,index) in allSongs.song" :key=index >
                            <img class="card-img-top"  alt="Card image cap"  :src="song.song_cover" style="height:20em;">
                            <div class="card-body" style="background-color:#f3f4f6;height:30em">
                                <h3 class="card-title" style="display:flex;justify-content:space-between;height:20%"><div style="font-size:1.5rem;">{{song.song_name}}   </div>             
                                    <div><button style="border:none;" @click="playAudio(song)"><span class="mdi mdi-play-box" style="color: blue; font-size: 1.8rem; position:relative;"  ></span></button></div>
                                    </h3>

                                <p class="card-text" style="margin-top:15px;">
                                    <div class="1" style="display:grid;grid-template-columns:repeat(2,1fr);gap:0.5rem;">
                                    <div class="attri2" style="background-color:#e5e7eb;text-align:center;">artist:<b>{{song.artist_name}}</b></div>
                                    <div class="attri3" style="background-color:#e5e7eb;text-align:center;"><b>{{song.song_genre}}</b></div>
                                    <div  class="attri4" style="background-color:#e5e7eb;text-align:center;display:flex;justify-content:center;align-items:center"><b>{{song.ratings}}❤️</b></div>
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
                                <form action="#"  id="formElem"  @submit.prevent="ratesong(song.sid,$event.target)">
                                    <div v-if="role=='norm_user'">
                    
                                             <input   name="rating"  href='#' class="btn btn-primary" id="number" type="number" placeholder="rate-song" style="margin-right:1.5rem;background-color:white;height:2rem;width:4.5rem;text-align:center;color:#606362" min=0 max=5></input>
                                            <button type="submit">rate!</button>
                                    </div>
                                   
                                </form>
                              
                                    <div class="flag" v-if="role=='admin'">

                                    <!-- <div v-if=="song.flag"></div> -->
                                        <div v-if="song.flag">
                                               <button type="submit" @click="flagsong(song.sid)">un-flag!</button>
                                            </div>
                                        <div v-if="!song.flag">
                                        <button type="submit" @click="flagsong(song.sid)">flag!</button>
                                        </div>
                                    </div>
                                   
                               
                            </div>
                        </div>

                        



                
                    </ul>


            </div>




         <AudioPlayer></AudioPlayer>


        


</div>




</template>

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
    grid-gap:1rem;
    background-color:aliceblue;
    padding:4rem;
    padding-bottom: 6rem;
    

}

.grid_div .card{

height:100%;

}

.common{
    background-color:aliceblue;

    display: flex;
    margin-left:4rem;
    margin-top:3rem;
    justify-content: flex-start;
    align-items: flex-start;
    gap:6rem;

}
.alb{
    display: flex;
    flex-direction:column;
    gap:1.5rem
}
.albone{
    display:flex;
    flex-direction:column;
    gap:0.5rem;

}
.alb2{
    
     display:flex;
     justify-content: flex-start;
     /* margin-left:1rem; */
     align-content: center;
 
    gap:1.5rem;

}
.bordered-word {
    color: #606362;
    
    margin-top: 1.5rem;
    display: flex;
    justify-content: center;}
.attr:hover{
    box-shadow: rgba(0, 0, 0, 0.25) 0px 54px 55px, rgba(0, 0, 0, 0.12) 0px -12px 30px, rgba(0, 0, 0, 0.12) 0px 4px 6px, rgba(0, 0, 0, 0.17) 0px 12px 13px, rgba(0, 0, 0, 0.09) 0px -3px 5px;
    text-align: center;

}
</style>


<script>
 import AudioPlayer from '@/components/AudioPlayer.vue'
import Navbar from '@/components/Navbar.vue'
export default {
    name:'albumsong',
    data(){
        return{
            cred:{
                token:localStorage.getItem('auth-token'),
                
            },
            artist_name:'',
            song_count:0,
            message:'',
            albumid:this.$route.params.aid,
            date:'',
            allSongs:[],
            error:'',
            message:''

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

    methods:{
         playCollection(collection){
            console.log("onecheck in all_albums")
            this.$store.dispatch('playCollection',collection)
         },
          getMonthandYear(date){
            return date.substring(7,11)+''+date.substring(11,16)
        }
,
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
    },

       async mounted(){


        try{

            const res=await fetch(`http://localhost:5000/api/all_albums/${this.albumid}`,{
                methods:'GET',
                headers:{
                      'Authentication-Token':this.cred.token,
                     
                }

            })

            let data=await res.json()

            if (res.ok){
                this.allSongs=data

                this.allSongs.song.forEach(element => {
                console.log(element,'element')
                element.song_cover= `http://localhost:5000/uploads/${element.sid}`
                element.song_audio=`http://localhost:5000/songs/${element.sid}/audio`
                
                
            }) 
            this.date=data.date_uploaded;
            //number of songs in the album:
            for (let i of data.song){
                
                this.song_count=this.song_count+1
            }
            this.artist_name=data.song[1].artist_name
         

            }else{
                this.error=data.errorm
                alert(errorm)

            }



        } catch(error){console.log(error)}

        


    }
}
</script>