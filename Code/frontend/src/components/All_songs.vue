<template>

   <!-- songs
    1/if the req is from a user: display all songs w rating  any footer tag
    2/ if the req is from a creator: display all  their songs with the edit and delete footer-> edit/song and edit album as well,
    3/if the req is from an admin:display all songs with a flag song at the footer 
    
     -->
    <div class="main">
        {{$route.params}}
        <Navbar userRole="user" type="two"></Navbar>
        <hr>
        <div class="bordered-word">
    <h1><em>Songs</em></h1>
    <hr>
    </div>
          <ul class="grid_div">

            <div class="card" style="width: 18rem;border-radius:40px;height:25rem;" v-for="(song,index) in allSongs" :key=index >
                <img class="card-img-top"  alt="Card image cap"  :src="song.song_cover" style="height:20em;">
                <div class="card-body" style="background-color:#f3f4f6;height:30em">
                    <h3 class="card-title" style="display:flex;justify-content:space-between;height:20%"><div style="width:60px;font-size:1.5rem;">{{song.song_name}}   </div>             
                        <div><button style="border:none;" @click="playAudio(song)"><span class="mdi mdi-play-box" style="color: blue; font-size: 1.8rem; position:relative;"  >Listen</span></button></div>
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

                    <input name="rating"  href='#' class="btn btn-primary" id="number" type="number" placeholder="rate-song" style="margin-right:1.5rem;background-color:white;height:2rem;width:4.5rem;text-align:center;color:#606362" min=0 max=5></input>
                    <button type="submit">rate!</button>
                    </form>
                </div>
            </div>

            



       
          </ul>




      <AudioPlayer></AudioPlayer>



      </div>
   
    

</template>

<script>


import AudioPlayer from '@/components/AudioPlayer.vue'
import Navbar from '@/components/Navbar.vue'
export default {
    name:'All_Songs',
    components:{AudioPlayer,Navbar},
    data(){
        return{
         
        song_rating:0,
        allSongs:[],
        token:localStorage.getItem('auth-token'),
        role:localStorage.getItem('role'),
        message:null,
        coverImageUrl: 'http://localhost:5000/uploads/6',
        audioUrl0:'http://localhost:5000/songs/12/audio'
      
        }
    },
    async mounted(){
        const res=await fetch("http://localhost:5000/api/all_songs",{
            headers:{
                'Authentication-Token':this.token,
                
            },
        })
        const data=await res.json().catch((e)=>{})
        if (res.ok){
            //   data.forEach(song => {
        // if (song.song_cover) {
        //     console.log('hurray')
        //   song.song_cover = 'data:image/png;base64,' + song.song_cover;
        //   console.log(song.song_cover)
        // }
    //   });
            console.log(data)
            this.allSongs=data
                console.log(this.allSongs.forEach(element => {
                console.log(element,'element')
                element.song_cover= `http://localhost:5000/uploads/${element.sid}`
                element.song_audio=`http://localhost:5000/songs/${element.sid}/audio`
                
                
            }))
        }else{
            this.message=data.message
        }

    },
     methods:{
          getMonthandYear(date){
            return date.substring(7,11)+''+date.substring(11,16)
        },
         async deletesong(){
            const res=await fetch('http://localhost:5000/api/all_songs/2',{
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