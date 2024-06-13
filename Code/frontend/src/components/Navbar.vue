<template>
    <div>
    <div class="login_nav" v-if="type==='main1'">
        <h1 style="flex-grow:0.2;font-size:3.5rem; text-decoration: underline; background-color:yellow;">SoundScape</h1>
        <div class="m1">
        <router-link to="/">Main</router-link>
        <router-link to="/signup">Signup</router-link>
        <router-link to="/login">User-login</router-link>
        <router-link to="/admlogin">Admin-Login</router-link>


        </div>
    </div>

    <div class="user_nav" v-if="userRole=='user'  && type=='one'">
          <h1 style="flex-grow:0.2;font-size:2.5rem; text-decoration: underline; background-color:yellow;">SoundScape</h1>
        <div class="search" >
            <form  @submit.prevent="search"  id="formElem">
            <input type="search" name="search_" id="search_" placeholder="Search" width="10" v-model="query">
            <button type="submit" ><span class="mdi mdi-magnify"></span></button>
            </form>
                      

        </div>
        <!-- <router-link to="/all_songs">Songs</router-link>
        <router-link  to="/all_albums">Albums</router-link> -->
    
        <router-link :to="'/profile/'+uid">Profile</router-link>
        <router-link to="/creatorhome">Register(creator)</router-link>
          <slot></slot>
    </div>



    <div class="user_nav1" v-if="userRole=='user' && type=='two'">
          <h1 style="flex-grow:0.2;font-size:3.5rem; text-decoration: underline; background-color:yellow;">SoundScape</h1>
        <router-link to="/userhome">Home</router-link>
           <router-link to="/all_albums/100">All-Albums</router-link>
        <!-- <router-link to="/all_songs">Songs</router-link>
        <router-link  to="/all_albums">Albums</router-link> -->
      <div style="display:flex;gap:1.5rem;">
        
        
          <router-link :to="'/profile/'+uid" >Profile</router-link>
          </div>
    </div>

    <div class="user_nav1" v-if="userRole=='user' && type=='three'">
          <h1 style="flex-grow:0.2;font-size:3.5rem; text-decoration: underline; background-color:yellow;">SoundScape</h1>
          <router-link to="/userhome">Home</router-link>
          <div>About</div>
          <div style="display:flex;gap:1.5rem;margin-right:0;">
           
          <div class="logo">logo</div>
          <router-link :to="'/profile'+uid">Profile</router-link>
          </div>

    </div>

    <div class='creat_nav' v-if="userRole=='creator'">
          <h1 style="flex-grow:0.2;font-size:3.0rem; text-decoration: underline; background-color:yellow;">SoundScape</h1>
          <div class="logo">logo</div>
          <router-link to="/userhome">User-Home</router-link>
          <slot name="add_song">Add Song</slot>
          
          <router-link to="/upload-album">upload_album</router-link>

    </div>
      <div class='creat_nav' v-if=" userRole=='creator' && type=='two'">
          <h1 style="flex-grow:0.2;font-size:3.0rem; text-decoration: underline; background-color:yellow;">SoundScape</h1>
          <div class="logo">logo</div>
          <router-link to="/userhome">User-Homess</router-link>
          <slot name="add_song">Add Song</slot>
          
          <router-link to="/upload-album">upload_album</router-link>

    </div>



    <div class="admin" v-if="userRole=='admin'">
           <h1 style="flex-grow:0.2;font-size:3.0rem; text-decoration: underline; background-color:yellow;">SoundScape</h1>
           <router-link to="/adminhome"> dashboard</router-link>
            <router-link to="/all_songs/100">All-Songs</router-link>
            <router-link to="/all_albums/100">All-Albums</router-link>
            <router-link to="/all_users">All-Users</router-link>
            
              <button @click="logout()">Logout</button>


            
    </div>

 
</div>
    
</template>




<script>
// Initialization for ES Users

export default {
    name:"Navbar",
    props:[
    "userRole",
    "type",
    'foodName'
    ],
    data(){
        return{
            query:"",
            uid:localStorage.getItem('uid'),
             authtoken:localStorage.getItem('auth-token')
        }

    },
    methods:{

        search(){
            this.$router.push({path:'/search_result',query:{query:this.query}})

            
        


},
 async logout(){
             const res=await fetch("http://localhost:5000/user-logout",{
                method:'POST',
                headers:{
                       'Content-Type': 'application/json',
                'Authentication-Token': this.authtoken,
                }
        })
        const data=await res.json().catch((e)=>{})
        if (res.ok){
            localStorage.clear();
            console.log("loggedout")
            this.$router.push('/')

        }else{
            alert("error")
        }
    }



}}
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
     font-size:1.2rem;

}
h1{
    overflow-y:visible;
}
.search{
  white-space: nowrap;
}

.user_nav{
    display: flex;
    /* justify-content:flex-start; */
    justify-content: space-between;
     margin-left: 0;
   
    background-color:#f7fee7;
    margin-bottom: 1.5rem;

}

input[id="search_"]{
    text-align: center;
    margin-top:0.2rem;
    border-color:white;
}
input[id="search_"]:focus{
    border-color:blue;
}

.user_nav1{
    background-color:#f7fee7;

    display:flex;
    justify-content: space-between;
    align-items:center;
}


.creat_nav{
    background-color:#f7fee7;
    display: flex;
    height:45px;
    font-size:medium;
    gap:10rem;
    margin-top:5px;
    justify-content: flex-start;
    align-items:top;
    margin-left: 0;
}
a{
    color:#606362;
}
a:focus{
    color:black;
}


.login_nav{

    display: flex;
    gap:10rem;
    margin-top:0;
    justify-content: flex-start;
    align-items:top;
    margin-left: 0;
}

a{
    color:black
}

.m1{
    display: flex;
    gap:10rem;
    margin-top:0;
    justify-content: center;
    align-items:top;

}

slot{
    color:#4c4e4d;
}

.admin{
    display:flex;
    justify-content: space-between;
    align-items:top;
}
</style>

