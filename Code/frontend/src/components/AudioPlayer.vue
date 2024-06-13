<template>
    <div class="main">
        <div class="aud">
            <div class="song_one">

        
                <div>
                        <div v-if="currentTrack?.song_cover"><img :src="currentTrack.song_cover" alt="" srcset="" height="60em" width="70em" style="margin-top:0;margin-bottom:25px;"></div>
                        <div v-else><img src="https://images.unsplash.com/photo-1494232410401-ad00d5433cfa?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8N3x8bXVzaWN8ZW58MHx8MHx8fDA%3D" alt="" srcset="" height="60em" width="70em" style="margin-top:0;margin-bottom:25px;"></div>
                </div>
                <div style="font-size:1.5rem;display:flex;flex-direction:column;gap:0.6rem;margin-bottom:25px;">
                
                <h3>{{currentTrack? currentTrack.song_name:'No Track Playing'}}</h3>
                 <audio autoplay  ref="audioPlayer" controls :src="audioUrl" @ended="playNext" ></audio>
                </div>
               
            </div>
            <div class="song_two">
                {{isPlaying ? 'Playing':'Paused'}}
               <button @click="playpause">
                <span class="mdi" style="color:white; font-size: 1.5rem;text-align:center;" :class="{ 'mdi-play': !isPlaying, 'mdi-pause': isPlaying }"></span>
                </button>
                


                  <button @click="playNext">
                <span class="mdi mdi-skip-next" style="font-size: 1.5rem"></span></button>

                
            </div>

            
            <!-- Button trigger modal -->

        </div>
        



    </div>


</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Fira+Sans:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
*{
     font-family: "Fira Sans", sans-serif;
    
  font-weight: 400;
  color:white;
  font-style: bold italic;

    margin:0;
    padding: 0;
    font-size: 1.2rem;
    
    
}

.main{
    
    position:fixed;
    bottom:0;
    left:0;
    width:100%;

    
}

audio{
    height:1.8rem;
    width:50vw;
}
audio::-webkit-media-controls-panel {
  background-color: white;
  
}
.modal{
    z-index: 2000;
}

.aud{
    
    height:13vh;
    background-color:#3959b1;
    display:flex;
}

.song_one{
    
    margin-top:10px;
    margin-left:5px;
    display: flex;
    align-items:center;
    /* flex-direction: column; */
    justify-content: flex-start;
    gap:2.5rem;
    flex-grow:0.5
}
.song_two{
    display: flex;
    justify-content: space-between;
    flex-grow:1;
    align-items: center;
    margin-right:15px;


}
button{
    height:45px;
    width:50px;
    border:1px solid black;
    border-radius:10px;
    text-align: center;
    background-color:blue;
    color:black;
}

</style>

<script>
export default {
    name:"AudioPlayer"
,
data(){
    return{
    audioUrl:'http://localhost:5000/songs/11/audio ',
    
   
    }
},
computed:{
    currentTrack(){
    console.log('inside audiop',this.$store.state.currentTrack)

        return this.$store.state.currentTrack;
     
    },

    isPlaying(){
        return this.$store.state.isPlaying
    },
    // audioUrl(){
    //     //console.log('inside audioURL',this.$store.state.currentTrack)
    //     //console.log('inside audioURL',this.currentTrack)

    //     //this.audioUrl0='http://localhost:5000/songs/12/audio'
       
    // // return this.currentTrack ? 'http://localhost:5000/songs/12/audio':'';

    //     return this.currentTrack ? this.currentTrack.song_audio:'';

        
    // },
},
watch:{
    currentTrack(newTrack){
       
        this.audioUrl=newTrack ?newTrack.song_audio:' ';
       
        console.log(this.audioUrl,'audiourl')
        
    },
  
},
methods:{

   

    playsong(){

    },
    //  onCanPlay() {
    //   this.isAudioLoaded = true;
    // },
    playpause(){
        console.log('hello')
        const audioPlayer=this.$refs.audioPlayer;
        console.log('audio',audioPlayer)
    
        if (this.isPlaying){
            audioPlayer.pause() //pause() is an event corr to the <audio> tag
            this.$store.dispatch('pauseTrack');
        }else{
            audioPlayer.play();
            this.$store.dispatch('playTrack',this.currentTrack)
        
    }},
    playNext(){
        this.$store.dispatch('playNextTrack')
    }
}
}
</script>