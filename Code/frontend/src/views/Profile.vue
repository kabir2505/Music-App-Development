<template>

<div class="main" style="display:flex;flex-direction:column; height:100vh;width:100vw;justify-content:center;align-items:center;">
    <div>
{{user.name}}</div>
<div>
{{user.email}}</div>
</div>

    



</template>
<style scoped>

</style>
<script>
export default {
    name:'Profile',
    data(){
        return{
        uid:localStorage.getItem('uid'),
        data:[],
        authtoken:localStorage.getItem('auth-token'),
        user:{
            name:"",
            email:""
        }
        }
    },

    async mounted(){
        let res=await fetch(`http://localhost:5000/api/all_users/${this.uid}`,
        {
              headers:{
                       'Authentication-Token':this.authtoken,
                        }
        })

        let data=await res.json()
        this.data=data
        this.user.name=data.uname;
        this.user.email=data.email;
        
    }
}
</script>