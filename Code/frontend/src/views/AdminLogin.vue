
<template>
<div>
  <Navbar type="main1" user_role="none" food-name="apple"></Navbar>
<div class="main">

<div class="login">
<h1 style="font-size:3rem;background-color:yellow;">AdminLogin</h1>
  <form action="#" @submit.prevent="login">
    <label for="email" >email:</label>
    <br>
    <input type="email" name="email" id="email" placeholder="abc@gmail.com" v-model="cred.email">
    <br> <br>
    <label for="password">password:</label>
    <br>
    <input type="password" name="password" id="password" placeholder="******" v-model="cred.password">
    <br>
    <br>
    <button type="submit" @click="login">Submit</button>
  </form>
    <div v-show="error">{{error}}</div>
</div>
</div>  
</div>

</template>

<script>


import HomeVue from '@/components/Home.vue'
import Navbar from '@/components/Navbar.vue'
export default {
    name: 'AdminLogin',
    data(){
        return{
            cred:{
        email:"",
        password:"",},
        error:null,
                 }
        
    },

    methods:{
        async login(){
            const res= await fetch('http://localhost:5000/user-login',{
                method:'POST',
                headers:{
                    'Content-Type':'application/json'
                },
                body:JSON.stringify(this.cred),
                                 })
                
              
              //res.json is a promise
              const data=await res.json()
              //res.ok->200 to 299
              if (res.ok){
                if (data.role=="admin" ){
                //console.log(data)
                //data:Object{email:"",role:"",token:""}

                localStorage.setItem('auth-token',data.token)
                localStorage.setItem('role',data.role)
                this.error=null
                this.$router.push('/adminhome')}else{ this.error='no such admin exists'}

              } else{
                console.log("data",data)
                console.log('hello')

                this.error=data.message
               
              }
        }
    },
  components: {
    Navbar,


    HomeVue
  },
  mounted(){
    const message=this.$route.query.message
    if (message){
      console.log(message)
      alert(message)
    }
  }
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

label{
  background-color:yellow;
}
input{
    width:25vw;
    height:3.5vh;
    text-align: center;
    font-size:1.5rem;

}
input:focus{
  color:black;


}
.main{
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
  height:80vh;

}

.login{
  border:2px solid black;
  box-shadow: rgba(0, 0, 0, 0.25) 0px 54px 55px, rgba(0, 0, 0, 0.12) 0px -12px 30px, rgba(0, 0, 0, 0.12) 0px 4px 6px, rgba(0, 0, 0, 0.17) 0px 12px 13px, rgba(0, 0, 0, 0.09) 0px -3px 5px;
  width:30vw;
  height: 60vh;
  padding:5px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap:2rem;

}
button{
  background-color:yellow;
  width:10vw;
}
</style>