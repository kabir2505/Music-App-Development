<template>
<div>

<!-- Button trigger modal -->
<button type="button" class="btn btn-primary addsong" data-bs-toggle="modal" data-bs-target="#exampleModal">
   + Add song  
</button>

<!-- Modal -->
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-xl">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="exampleModalLabel">Add Song</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body" >
       
            <form action="#" @submit.prevent="uploadsong" id="formElem" style="width:100%;height:100%">
                 <!-- <div class="form-input"> -->
                  <div class="container-fluid">
                  
               <div class="row" >
               <input type="text" class= "col-md-3" name="song_name" id="song_name" placeholder="song title">
                 <input type="text" class="col-md-3" name="song_genre" id="song_genre" placeholder="genre">
                <input type="text"  class="col-md-3" name="artist_name" id="artist_name" placeholder="artist name">
               </div>
             
                <div class="row">
            <textarea name="lyrics" id="lyrics" class="form-control col-md-10 lyrics" rows="4" placeholder="Enter lyrics..."></textarea>
               </div>
               <div class="row " style="margin-top:.8rem;">
               <div class='song_cover col-md-5 '>
                <label for="song_cover">Select an image</label>
               <input type="file" name="song_cover" id="song_cover" accept="image/*" >
               </div>
               <div class='song_audio col-md-5' style="margin-left:2.5rem;">
                 <label for="song_audio">Select the audio</label>
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

<script>

export default {
    name:'upload_song',
    data(){
      return{
        cred:{
          authtoken:localStorage.getItem('auth-token'),
          creator_id:localStorage.getItem('uid')
        },
        artistid:localStorage.getItem('uid')
      }

    },
        methods:{
            async uploadsong(event){
                event.preventDefault();
                const formData = new FormData(event.target);

                let res=await fetch('http://localhost:5000/api/all_songs', {
      method: 'POST',
      headers:{
        'Authentication-Token':this.cred.authtoken,
        mola:99,
        artistid:this.artistid,
       
       
      },
      body: formData
    });
     let result = await res.json();
    
     alert(result.message)
     setTimeout(()=>{
      window.location.reload();
     },1000)


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
.modal-body{

  height:70vh;
  display: grid;
  grid-template-columns: 1fr;
  gap:10px;

}


/* .form-input{
    display: flex;
    flex-direction: column;
    gap:15px;
    width:100%;
    height:100%;
} */

/*
#formElem{
  display: grid;
  grid-template-columns: repeat(4,1fr);
  grid-template-rows: 1fr 1fr 1fr 1fr;
}

#song_name{
  grid-column: 1/2;
  grid-row: 1/2;
}
#song_genre{
  grid-column: 2/3;
   grid-row: 1/2;
}
#artist_name{
  grid-column: 3/4;
   grid-row: 1/2;
}
.lyrics{
   grid-column: 1/4;
   grid-row: 2/3;
   background-color:black;
}*/



#exampleModalLabel{
  background-color: yellow;
  font-size:x-large;
  text-align: center;
}

input{
  border:2px solid black;
  border-radius: 10px;
  text-align: center;
  margin-top:1.0rem;
  font-size:x-large;
  content: bold;
  overflow: hidden;
  margin-left:2.5rem;
}
.song_audio{
  grid-column: 1/2;
  grid-row: 3/4;

}
.song_cover{
  grid-column: 3/4;
  grid-row: 3/5;
  
}
label{
  background-color:yellow;
}

.lyrics{
  margin-top:1rem;
  border:2px solid black;
  font-family: inherit;
  font-size:medium;
  height:20rem;
  text-align:left;
  overflow: scroll;
  overflow-x: hidden;
}

.addsong{
   white-space: nowrap;
  width:6.5rem;
  background-color:black;
  color:yellow;
  height:2rem;
}
.addsong :focus{
   width:6.5rem;
  background-color:black;
  color:yellow;

}





input:focus{
  border:2px solid rgb(64, 64, 164);
}
button[type="submit"]{
  margin-top:15px;
  width:10rem;
}

</style>