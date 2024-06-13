<template>
<div>
<div>
  
    <!-- <All_Users v-if="role==='admin' && wid===4"></All_Users>
    <All_Songs v-if="wid==1"> </All_Songs> -->
    <!-- <All_Albums v-if="wid==2"></All_Albums> -->
    <!-- <All_Playlists v-if="wid==3"></All_Playlists> -->
    
  
</div>
 <!-- <upload_song>hello</upload_song>--> 
 </div> 
</template>

<script>
// import All_Users from '@/components/All_Users.vue'
// import All_Songs from '@/components/All_songs.vue'
// // import All_Albums from '@/components/All_albums.vue'
// import All_Playlists from '@/components/All_playlists.vue'
// import upload_song from '@/components/upload_song.vue'


export default {
    name:'All_Stuff',
    computed:{
      wid(){
        return this.$route.params.id
      }
    },}
//     mounted(){
//       if (!localStorage.getItem('auth-token')){
//         console.log('nope')
//         alert('please login first!')
//         // setTimeout(()=>{
//         //    this.$router.push('/login')
//         // },1500)
       
//       }
//     },
//    data(){
//         return{
        
//         token:localStorage.getItem('auth-token'),
//         role:localStorage.getItem('role'),
//         message:null,
      
//         }
//     },
//     components: {

//     All_Users,
//     All_Songs,
    
//     All_Playlists,
//     upload_song
        
//   },
    
// }

</script>
<style scoped>

</style>