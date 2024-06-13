


<template>
<!-- idea:   A->fetch the concerned song, with its attributes,
B->display the attributes as placeholders in the form with mild colors
C->remove form validation of any type
D->update it
-->



<div class="main">
   


  
 <!-- #song_name, song_genre, artist_name, song_genre , lyrics , song_cover, song_audio -->
 <button type="button" class="btn btn-primary addsong" data-bs-toggle="modal" :data-bs-target="'#' + 'modal-' + SongId">

   Edit song  
</button>

<!-- Modal -->
<div class="modal fade" :id="'modal-' + SongId" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-xl">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" :id="'modal-title-' + SongId">Edit Song</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body" >
       
            <form action="#" @submit.prevent="editsong(song.sid,$event)" id="formElem" style="width:100%;height:100%">
                 <!-- <div class="form-input"> -->
                  <div class="container-fluid">
                  
               <div class="row" >
               <input type="text" class= "col-md-3" name="song_name" id="song_name" :placeholder=song.song_name>
                 <input type="text" class="col-md-3" name="song_genre" id="song_genre" :placeholder=song.song_genre>
                <input type="text"  class="col-md-3" name="artist_name" id="artist_name" :placeholder=song.artist_name>
               </div>
             
                <div class="row">
            <textarea name="lyrics" id="lyrics" class="form-control col-md-10 lyrics" rows="4" :placeholder=song.lyrics style="text-align:center"></textarea>
               </div>
               <div class="row " style="margin-top:.8rem;">
               <div class='song_cover col-md-5 '>
                <label for="song_cover"><b>Upload alternative image</b></label>
               <input type="file" name="song_cover" id="song_cover" accept="image/*" >
               </div>
                
               <div class='song_audio col-md-5' style="margin-left:2.5rem;">
                 <label for="song_audio"> <b>Upload alternative audio</b></label>
               <input type="file" name="song_audio" id="song_audio" accept="audio/*">
               </div>
               </div>
               </div>
               <!--</div> -->
               <div class="row justify-content-center" style="margin-right:0px;">
               <button type="submit" class="col-md-3">submit</button>
               </div>
              
            </form>
       
      </div>
      <div class="modal-footer" style="min-height: 50px;">
      <div></div>
      </div>
    </div>
  </div>
</div>


  </div>  
</template>

<style scoped>


input[type="text"]::placeholder {
  color:#252626;
  font-style:italic;

}

</style>

<script>
export default {
      name:'Editsong',
       data(){
      return{
        cred:{
          authtoken:localStorage.getItem('auth-token'),
          creator_id:localStorage.getItem('uid')
        },
        artistid:localStorage.getItem('uid')
      }

    },
    
    computed:{
        getsongid(){
            pass
        }


    },

    props:{
  SongId: {
    type: Number,
    required: true
  },
  SongName: {
    type: String,
    required: true
  },
  song: {
    type: Object,
    required: true
  }
},

    methods:{
            async editsong(song_id,event){
                 let formElem = event.target.closest('form');
               
           
                let res=await fetch(`http://localhost:5000/api/all_songs/${song_id}`, {
      method: 'PUT',
      headers:{
        'Authentication-Token':this.cred.authtoken,
       
        artistid:this.artistid,
       
       
      },
      body: new FormData(formElem)
    });
     let result = await res.json();
    
     alert(result.message)
     setTimeout(()=>{
      window.location.reload();
     },1000)


            }
        },


    async mounted(){
      
        //   const res=await fetch("http://localhost:5000/api/all_songs/",{
        //     headers:{
        //         'Authentication-Token':this.token,
                
        //     },
        // })
        // const data=await res.json().catch((e)=>{})
        // if (res.ok){
      
        //     console.log(data)
        //     this.allSongs=data
        //         console.log(this.allSongs.forEach(element => {
        //         console.log(element,'element')


        //         element.song_cover= `http://localhost:5000/uploads/${element.sid}`
        //         element.song_audio=`http://localhost:5000/songs/${element.sid}/audio`
                
                
        //     }))
        // }else{
        //     this.message=data.message
        // }





    }
    
}
</script>