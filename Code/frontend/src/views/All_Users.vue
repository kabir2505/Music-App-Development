<template>
<div class="main">
     <Navbar userRole="admin"></Navbar>
    <h1 style="display:flex;justify-content:center"> All Users!</h1>
    <div class="all_users">

         <div v-for="user in allUsers"> 
           
              <div class="card" style="width: 18rem;">
  <div class="card-body">
    <h5 class="card-title">{{user.uname}}</h5>
    <h6 class="card-subtitle mb-2 text-body-secondary"><div>{{user.email}}</div> <div>{{user.roles}}</div></h6>
    <div class="attri">
    <div class="b1"><button v-on:click="flaguser(user.uid)" >
        <div v-if="user.active">flag!</div> <div v-if="!user.active">unflag!</div></button></div>
    <div class="b2"><button v-on:click="deleteuser(user.uid)">ban!</button></div>
  </div>
  </div>
</div>
               
         </div>

    </div>
</div>

</template>

<script>
import Navbar from '@/components/Navbar.vue'
export default {
    name:'All_Users',
    data(){
        return{
        allUsers:[],
        token:localStorage.getItem('auth-token'),
        role:localStorage.getItem('role'),
        message:null,
      
        }
    },
    components:{
        Navbar
    }
    ,
    async mounted(){
        const res=await fetch("http://localhost:5000/api/all_users",{
            headers:{
                'Authentication-Token':this.token,
                'User-Role':this.role
            },
        })
        if (localStorage.getItem('role')!='admin'){  
        setTimeout(()=>{
            console.log('tf')
           this.$router.push('/login')
        },1500)};
        const data=await res.json().catch((e)=>{})
        if (res.ok){
            console.log("datacreated",data)

            this.allUsers=data
        }else{
            this.message=data.message
        }

    },
    methods:{
         async deleteuser(id){
            const res=await fetch(`http://localhost:5000/api/all_users/${id}`,{
                method:'DELETE',
                headers:{
                       'Authentication-Token':this.token,
                        'User-Role':this.role
                },
            })
            const data=await res.json().catch((e)=>{})
            if (res.ok){
             setTimeout(function() {
            location.reload();
        }, 5000)
            }else{
            this.message=data.message
            }

            

         },

         async flaguser(id){
              const res=await fetch(`http://localhost:5000/activate/user/${id}`,{
              
                headers:{
                       'Authentication-Token':this.token,
                        'User-Role':this.role
                },
            })

              const data=await res.json().catch((e)=>{})
            if (res.ok){
             setTimeout(function() {
            location.reload();
        }, 2000)

            }else{
            this.message=data.message
            }

            


         }
    } 


    
}
</script>


<style scoped>
button{
    background-color:lightpink;

}
.main{
    
}
.card{
    text-align: center;
    margin-top:1rem;
}
.all_users{
    margin-left:1.5rem;
    margin-right:1.5rem;
    margin-top:3rem;
    display: grid;
    grid-template-columns: repeat(4,1fr);
    
}
.attri{
    display: flex;
    justify-content: space-between;
}

</style>