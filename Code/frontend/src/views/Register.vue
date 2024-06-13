<template>
<div>
<Navbar type="main1" user_role="none" food-name="apple"></Navbar>
<div class="main">

    <div class="login">
    <div class="form">
        <h1 style="font-size:3rem;background-color:yellow;">Signup here!</h1>
      
        <form action="#" @submit.prevent="signup">
            <div>
                <div>
                     <label for="email">Email</label>
                     <br>
                    <input type="email" name="email" id="email"  v-model="cred.email"  >
                </div>
               
                <div> 
                    <label for="uname">Name</label>
                    <br>
                    <input type="text" v-model="cred.uname" name="uname" id="uname" >
                </div>
                <div>
                    <label for="password" >Password</label>
                    <br>
                    <input type="password"  v-model="cred.password" name="password" id="password" required >
                </div>
                <div>{{message}}</div>
               
            </div>
            <button type="submit">Submit</button>

            
        </form>
    </div>
    </div>
    </div>
    </div>
</template>
<script>
import Navbar from '@/components/Navbar.vue'
export default {
    name:'RegisterUser',
    data(){
        return{
            cred:{
            email:'',
            uname:'',
            password:'',
            },
            message:''
        };

        
    },
    components:{Navbar,},
    methods:{
        async signup(){
            console.log('heelo1')
            const res=await fetch('http://localhost:5000/user-signup',{
                method:'POST',
                headers:{
                    'Content-Type':'application/json'
                },
                body:JSON.stringify(this.cred)
               
            })
            console.log(JSON.stringify(this.cred))

            const data=await res.json()
            if (res.ok){
              
                console.log(data.message)
                alert('signup successful!')
                this.cred.email='',
                this.cred.uname='',
                this.cred.password=''
                this.message=data.message
                setTimeout(()=>{
                    this.$router.push('/login')
                },2000)
                
            }else{
                this.message=data.message
            }





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