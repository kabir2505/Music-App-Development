<template>
 
 <div class="main">
    <Navbar userRole='user' type='two'></Navbar>
  <div class="common">
    <div>
            <img src="https://media.newyorker.com/photos/644afa9f328537f70292b8df/master/w_1800,c_limit/Graphic1_Beat3_01.png" height=150px width=150px alt="">
    </div>
     <div class="alb">
        <div class="albone">
                <div>
                
                    <div class="datetime" style="font-size:1rem">{{getMonthandYear(date)}}</div>
                        
                </div>
                <div>
                    <div style="font-size:2rem"> <h2>{{playlist.pl_name}}</h2></div>

                </div>
            </div>
          <div class="alb2">

                    <div  class="attr" style="background-color:#e5e7eb;text-align:center; "> <b>{{song_count}}</b> songs</div>
                 

            </div>

    </div>





  </div>
    <form action="">
        
          <ul class="grid_div">

        <li v-for = "song in playlist.song" :key=song.sid>
           
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

            
              <div style="position:relative;margin-left:20rem;"> <input type="text" name="pl_name" id="pl_name" :placeholder=playlist.pl_name v-model="output.playlist_name"></div>
             <button type="submit" style="margin-right:20.5rem; position:relative;margin-left:5rem;" @click="updateplaylist">Upload!</button>
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
    background-color: red;
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
    background-color:blue;
}



</style>

<script>
 import Navbar from '@/components/Navbar.vue'
import { ref } from 'vue'
export default {
    name:'Edit_Playlist',
   

    
    data(){
        return{
            pl_id:this.$route.params.pid,
            cred:{
            token:localStorage.getItem('auth-token'),
            uid:localStorage.getItem('uid'),
            role:localStorage.getItem('role')},
             playlist:[],
             message:'',
              date:'',
              song_count:0,
           
              output:{
                 playlist_name:"",
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
         async updateplaylist(){
            try{
                const res= await fetch(`http://localhost:5000/api/all_playlists/${this.playlist.pid}`,{
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
        let res=await fetch(`http://localhost:5000/api/${this.cred.uid}/all_playlists/${this.pl_id}`,{

              headers:{
                'Authentication-Token':this.cred.token,
                'role':this.cred.role

                
            },



        })
            const data=await res.json() 
              if (res.ok){
           
            this.playlist=data;

            
                let allsongs=this.playlist.song
              
                allsongs.forEach(song=>{
                    this.output.checkedNames.push(song.sid)
                    song.song_cover=`http://localhost:5000/uploads/${song.sid}`
                    song.song_audio=`http://localhost:5000/songs/${song.sid}/audio`

                })
                
                   for (let i of data.song){
                
                this.song_count=this.song_count+1;
            

            };
          }
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