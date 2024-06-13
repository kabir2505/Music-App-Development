<template>
<div class="main">
    <!-- {{album_id}} -->

<!-- idea:   A->pass the concerned album via props,
B->display the attributes as placeholders in the form with mild colors
C->remove form validation of any type
D->update it

A->fetch the id from this.$route and fetch the album
B->Navbar
B->display the album name and title
-->


<div class="main">
        <Navbar userRole='creator'>
            <template v-slot:add_song>
                 <router-link to="/creatorhome">Creator-Home</router-link>


            </template>
        </Navbar>
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
                    <div style="font-size:2rem"> <h2>{{album.alb_name}}</h2></div>

                </div>
            </div>
            <div class="alb2">

                    <div  class="attr" style="background-color:#e5e7eb;text-align:center; "> <b>{{song_count}}</b> songs</div>
                    <div   class="attr" style="background-color:#e5e7eb;text-align:center;">artist-<b>{{artist_name}}</b></div>

            </div>

            </div>
        </div>


         <form action="">
        <!-- <div class="grid_div"> -->
  
<!--         
           
            <div><button type="submit">Submit</button></div>
            <div style="background-color:black;"><button type="reset">Reset</button></div>
           -->



<!-- <input type="checkbox" id="mike" value="Mifdadke" v-model="checkedNames">
<label for="mike">Mike</label> -->

  
          <ul class="grid_div">

        <li v-for = "song in album.song" :key=song.sid>
           
            <input type="checkbox" :id="'song_cov'+ song.sid" v-model="output.checkedNames" :value="song.sid" />
            <label :for="'song_cov' + song.sid">
                <figure>
                    <img :src=song.song_cover />
                    <figcaption><h4>{{song.song_name}}</h4></figcaption>
                </figure>
            </label>     
        </li>
        {{output.checkedNames}}
    </ul>

        <!-- </div> -->
  </form>
    <div class="stick">

            
              <div style="position:relative;margin-left:20rem;"> <input type="text" name="album_name" id="album_name" :placeholder=album.alb_name v-model="output.album_name"></div>
             <button type="submit" style="margin-right:20.5rem; position:relative;margin-left:5rem;" @click="updatealbum">Upload!</button>
        </div>
        




</div>




</div>
    
</template>

<style scoped>

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

.common{
    background-color:aliceblue;

    display: flex;
    margin-left:4rem;
    margin-top:3rem;
    justify-content: flex-start;
    align-items: flex-start;
    gap:6rem;

}

@import url('https://fonts.googleapis.com/css2?family=Fira+Sans:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
  
fira-sans-medium {
  font-family: "Fira Sans", sans-serif;
  font-weight: 500;
  font-style: normal;
}
form{
     font-family: "Fira Sans", sans-serif;
    
}
input{
      font-family: "Fira Sans", sans-serif;

}

  @import url('https://fonts.googleapis.com/css2?family=Merriweather+Sans:ital,wght@1,800&display=swap');
*{
    font-family: 'Merriweather Sans', sans-serif;
}

hr {
  border-bottom: 1px dotted #cccccc; 
  margin-left:3.5rem;
    margin-right:3.5rem;
}
h1{
    color:#606362;

    margin-top:1.5rem;
  
    display: flex;
    justify-content: center;
    
}
.main{
    margin:0;
    border:3px solid yellow;
    height:100vh;
    width:100vw;
}
.grid_div{
    height:79vh;
    display: grid;
    grid-template-columns:repeat(5,1fr) ;
    background-color: rgb(226, 226, 226);
}
input{
    height:2.5rem;
    width:15rem;
    text-align: center;
}
ul {
  list-style-type: none;
}
li {
  display: inline-block;
}
input[type="checkbox"][id^="song_cov"] {
  display: none;
}

label {
  border: 1px solid #fff;
  padding: 10px;
  display: block;
  position: relative;
  margin: 10px;
  cursor: pointer; 
  /* specifies the mouse cursor to be displayed when pointing over an element. */
}

label:before {
  background-color: white;
  color: white;
  content: " ";
  display: block;
  border-radius: 50%;
  border: 1px solid grey;
  position: absolute;
  top: -5px;
  left: -5px;
  width: 25px;
  height: 25px;
  text-align: center;
  line-height: 28px;
  transition-duration: 0.4s;
  transform: scale(0);
}

label img {
  height: 100px;
  width: 100px;
  transition-duration: 0.2s;
  transform-origin: 50% 50%;
}

:checked + label {
  border-color: #ddd;
}

:checked + label:before {
  content: "✓";
  background-color: grey;
  transform: scale(1);
}

:checked + label img {
  transform: scale(0.9);
  box-shadow: 0 0 5px #333;
  z-index: -1;
}


.stick{
    display: flex;
    width:100vw;
    color:white;
    font-size:x-large;
    height:10vh;
    align-items: center;
    position:sticky;
    justify-content: space-between;
    background-color:#f0f9ff;
}


</style>

<script>
import Navbar from '@/components/Navbar.vue'
import { ref } from 'vue'
export default {
    name:'Edit_Album',
    data(){
        return{
            album_id:this.$route.params.a_id,
            cred:{
            token:localStorage.getItem('auth-token'),
            uid:localStorage.getItem('uid'),
            role:localStorage.getItem('role')},
             album:[],
             message:'',
              date:'',
              song_count:0,
              artist_name:' ',
              output:{
                 album_name:"",
                checkedNames: ref([]),
            },
             checkedIds:ref([]),
            

        }

    },
    components:{
        Navbar
    },
    methods:{
         getMonthandYear(date){
            return date.substring(7,11)+''+date.substring(11,16)
        },
         async updatealbum(){
            try{
                const res= await fetch(`http://localhost:5000/api/all_albums/${this.album.a_id}`,{
                    method:"PUT",
                    headers:{
                        "Content-Type":"application/json",
                        'Authentication-Token':this.cred.authtoken,
                    },
                    body:JSON.stringify(this.output)
                })

                const data=await res.json()
 
                if(res.ok){ this.message=data.message
                
                alert(data.message)
                 setTimeout(()=>{
            window.location.reload()},1000)}else{alert(data.error)}



            } catch(e){
                console.log(e)
            }
        }
,
    },

    async mounted(){
        try{
        let res=await fetch(`http://localhost:5000/api/all_albums/${this.album_id}`,{

              headers:{
                'Authentication-Token':this.cred.token,
                'role':this.cred.role

                
            },



        })
            const data=await res.json() 
              if (res.ok){
           
            this.album=data;

            
                let allsongs=this.album.song
                 this.date=this.album.date_uploaded;
                allsongs.forEach(song=>{
                    this.output.checkedNames.push(song.sid)
                    song.song_cover=`http://localhost:5000/uploads/${song.sid}`
                    song.song_audio=`http://localhost:5000/songs/${song.sid}/audio`

                })
                
                   for (let i of data.song){
                
                this.song_count=this.song_count+1;
            

            };
            this.artist_name=data.song[0].artist_name}
                 else{
            this.message=data.message
            alert(this.message)
            
        }
        
        }catch (error) {
    
    console.error('Error:', error);
  }





    }

}
</script>