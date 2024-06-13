<template>
  <div class="home">
   <div class="title">SoundScape</div>
   <div class="main">
    <div class="login"> <a href="/login">User Login</a></div>
    <div class="adm"><a href="/admlogin">Admin Login</a></div>
    <div class="singup"><a href="/signup">Signup</a></div>
   </div>
   
  </div>
</template>

<script>
// @ is an alias to /src



export default {
  name: 'HelloWorld',

}
</script>

<style scoped>

 
@import url('https://fonts.googleapis.com/css2?family=Acme&family=Bebas+Neue&display=swap');


.acme-regular {
  font-family: "Acme", sans-serif;
  font-weight: 400;
  font-style: normal;
}

*{
  font-family:"Acme", sans-serif; ;
}

.home{
  
  background-image: url(/Users/kabirjamadar/Desktop/life/iitmadras/diploma/mad2p/Code/frontend/src/assets/back/album.jpg);
  background-position: center;
  background-color: azure;
  overflow: hidden;
  background-size: contain;
  background-repeat: no-repeat;
  height: 100vh;
  width:100vw;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items:center;
 
}
.title{
  font-size: 5rem;
  background-color:yellow;
  padding:1rem;
  text-align: center;
  
}
a{
  color:#4c4e4d;
  border:2px solid black;
  background-color:yellow;
  padding:.6rem;
}
a:hover{
  color:black;
}

.main{
  margin-top:3rem;
  display: flex;
  font-size: 1.5rem;
  gap:40px;

}
</style>
