<template>

<div class="main-div">
    <Navbar userRole='creator'></Navbar>
<div class="bordered-word">
  <h1>Upload an album</h1>
  <hr>
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
            <div v-for = "song in all_data" :key=song.sid  >
        <li  v-if="!song.album_id" >
     
            <input type="checkbox" :id="'song_cov'+ song.sid" v-model="output.checkedNames" :value="song.sid" />
            <label :for="'song_cov' + song.sid">
                <figure>
                    <img :src=song.song_cover />
                    <figcaption><h4>{{song.song_name}}</h4></figcaption>
                </figure>
            </label>   
           
        </li>
        </div>
    </ul>

        <!-- </div> -->
  </form>



        

      <div v-show="message">{{message}}</div>
      <div v-show="error">{{error}}</div>

        <div class="stick">

            
              <div style="position:relative;margin-left:20rem;"> <input type="text" name="album_name" id="album_name" placeholder="album_name" v-model="output.album_name"></div>
              
             <button type="submit" style="margin-right:20.5rem; position:relative;margin-left:5rem;" @click="submitalbum">Upload!</button>
        </div>
        
  


  
    

</div>
    
</template>


<script>
import Navbar from '@/components/Navbar.vue'
import { ref } from 'vue'
export default {
    name:'upload_album',
    data(){
        return{
            cred:{
                authtoken:localStorage.getItem('auth-token')

            },
           
            all_data:[],
            message:null,
            error:null,
            output:{
                 album_name:"",
                checkedNames: ref([]),
            },
            checkedIds:ref([]),
        
         creator_id:localStorage.getItem('uid')
        }
    },
    components:{
        Navbar
    },


    methods:{
        async submitalbum(){
            try{
                const res= await fetch(`http://localhost:5000/api/${this.creator_id}/all_albums`,{
                    method:"POST",
                    headers:{
                        "Content-Type":"application/json",
                        'Authentication-Token':this.cred.authtoken,
                    },
                    body:JSON.stringify(this.output)
                })

                const data=await res.json()

                if(res.ok){ this.message=data.message
                alert(data.message)}else{alert(data.error)}



            } catch(e){
                console.log(e)
            }
        }

    },



    async mounted(){
//promise-->response object--->data.json()=promise-->object{},{}
        try {
        const res=await fetch(`http://localhost:5000/api/${this.creator_id}/all_songs`,{
            method:'GET',
            headers:{
                 'Content-Type': 'application/json',
                 'creator_id':this.creator_id,
                 'Authentication-Token': this.cred.authtoken,
            }

        })
        const data=await res.json() 
         if (res.ok){
            console.log(data)
            this.all_data=data
            console.log(this.all_data.forEach(element => {
                console.log(element,'element')
                element.song_cover= `http://localhost:5000/uploads/${element.sid}`
                element.song_audio=`http://localhost:5000/songs/${element.sid}/audio`
                
                
            }))
        }else{
            alert('not ok')
        }
}  catch (error) {
    
    console.error('Error:', error);
  }
            //res is a response object & res.json() is a promise
        
       

        
        
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

.main-div{
    margin:0;
    border:3px solid yellow;
    height:100vh;
    width:100vw;
}

.grid_div{
    height:79vh;
    display: grid;
    grid-template-columns:repeat(5,1fr) ;
background-color:#f7fee7;
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
    position:absolute;
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