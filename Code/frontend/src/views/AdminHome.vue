<template>
<div class="main">
    <Navbar userRole='admin'></Navbar>

    <div class="main2">

        <div class="stats1">
            <div>
                <h2 style="text-align:center;margin-bottom:3rem;">Dashboard Overview</h2>
            </div>
            <div class="cards_">
                    <div class="c1">
                    <div>
                        <div class="card" style="width: 18rem;">
                            <div class="card-body">
                                <h5 class="card-title"><div>Total Users:{{stats1.user_count}}</div></h5>
                            
                                <p class="card-text">

                                    <div>Active:{{stats1.user_active}}</div>
                                    <div>Flagged:{{stats1.user_flag}}</div>
                                </p>
                                <div class="link">
                                <router-link to="/all_users">
                                <span class="mdi mdi-cog"></span></router-link>
                                </div>
                            </div>
                        </div>

                    </div>
                    </div>

                    <div class="c2">
                    <div>
                        <div class="card" style="width: 18rem;">
                            <div class="card-body">
                                <h5 class="card-title"><div>Total Songs:{{stats1.song_count}}</div></h5>
                            
                                <p class="card-text">

                                    <div>Active:{{stats1.song_active}}</div>
                                    <div>Flagged:{{stats1.song_flag}}</div>
                                </p>
                                <div class="link">
                                <router-link to="/all_songs/100">
                                <span class="mdi mdi-cog"></span></router-link>
                                </div>
                            </div>
                        </div>

                    </div>
                    </div>

                    <div class="c3">
                    <div>
                        <div class="card" style="width: 18rem;">
                            <div class="card-body">
                                <h5 class="card-title"><div>Total Albums:{{stats1.album_count}}</div></h5>
                            
                                <p class="card-text">

                                    <div>Active:{{stats1.album_active}}</div>
                                    <div>Flagged:{{stats1.album_flag}}</div>
                                </p>
                                <div class="link">
                                <router-link to="/all_songs/100">
                                <span class="mdi mdi-cog"></span></router-link>
                                </div>
                            </div>
                        </div>

                    </div>
                    </div>
            </div>


        </div>
 <!-- graphs:
    top songs based upon  the avg rating 
    pie chart based upon user roles
    songs uploaded overtime based upon date, year->line chart


    

    
    -->

        <div class="stats2" >
            <h2 style="background-color:yellow;position:sticky;top:0;">Top Songs</h2>
            <div>
            <table>
                <th>name</th>
                <th>artist</th>
                <th>ratings</th>
                <tr v-for="(song,index) in top_songs" :key="index" >
                    
                      <td >{{ song.song_name}}</td>
                      <td>{{song.artist}}</td>
                      <td>{{song.ratings}}</td>

                    
                </tr>
                </table>
                </div>


            
        </div>
        <div class="stats3">
             <h2 style="background-color:yellow;position:sticky;top:0;">Top Creators</h2>
            <div>
            <table>
                <th>name</th>
                <th>avg-rating</th>
                <th>total-uploads</th>
                <tr v-for="(creator,index) in top_creators" :key="index" >
                    
                      <td >{{ creator.artist_name}}</td>
                      <td v-if="creator.avg_rating">{{creator.avg_rating}}</td>
                      <td v-if="!creator.avg_rating">0</td>
                      <td>{{creator.total_uploads}}</td>

                    
                </tr>
                </table>
                </div>



        </div>
        <!-- <div class="chart1">
        <img src="http://127.0.0.1:5000/pie_chart" alt="">
        </div>
         <div class="chart2">
        <img src="http://127.0.0.1:5000/admin_charts" alt="">
        </div> -->



  <div class="charts">
   
    <!-- Button trigger modal -->
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal_line_chart1">
 Songs uploaded by month📈
</button>

<!-- Modal -->
<div class="modal fade" id="exampleModal_line_chart1" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog	modal-xl">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5 line_chart1" id="exampleModal_line_chart1">Songs uploaded by month📈</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
         <canvas id="line_chart1"></canvas>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>

      </div>
    </div>
  </div>
</div>

<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal_rolepie">
  Distribution of users by roles🥧
</button>

<!-- Modal -->
<div class="modal fade" id="exampleModal_rolepie" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog	modal-xl">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="exampleModal_rolepie">Distribution of users by roles</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
         <canvas id="role_pie"></canvas>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>

      </div>
    </div>
  </div>
</div>


<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal_genre_bar">
  Distribution of songs by genre📊
</button>

<!-- Modal -->
<div class="modal fade" id="exampleModal_genre_bar" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog	modal-xl">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="exampleModal_genre_bar">  Distribution of songs by genre📊</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
          <canvas id="genre_bar"></canvas>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>



<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal_userreg">
 User registration statistics📈
</button>

<!-- Modal -->
<div class="modal fade" id="exampleModal_userreg" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog	modal-xl">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="exampleModal_userreg"> User registration statistics📈</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <canvas id="user_line"></canvas>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
       
      </div>
    </div>
  </div>
</div>
   
   </div>
  
   
   
   
 </div>

</div>
  
    <!-- total users
    total songs
    total albums -->



   

    <!-- cards:
    all users
    all albums
    all playlists -->


</template>

<script>
import Navbar from '@/components/Navbar.vue' //import chart.js
import Chart from 'chart.js/auto';
export default {
    name:"AdminHome",
    data(){
        return{
             cred:{
                user_role:localStorage.getItem('role'),
                user_uid:localStorage.getItem('uid'),
               authtoken:localStorage.getItem('auth-token')
            },
            stats1:{},
            top_songs:[],
            top_creators:[],
             data1 : [
    { year: 2010, count: 10 },
    { year: 2011, count: 20 },
    { year: 2012, count: 15 },
    { year: 2013, count: 25 },
    { year: 2014, count: 22 },
    { year: 2015, count: 30 },
    { year: 2016, count: 28 },],
    song_bar:{
        months:[],
        counts:[]
    },
    role_pie:{
        distri:[],
        labels:[]

    },
    user_line:{
        user_months:[],
        user_counts:[]
    },
    unique_genre:{}
  
        }
    },
    components:{
            Navbar
    },
    async mounted(){
        const res1=await fetch(`http://localhost:5000/admin_info`,{
              headers:{
                       'Authentication-Token':this.cred.authtoken,
                        'User-Role':this.cred.user_role}
                
               
        })

        const data=await res1.json().catch((e)=>{})
        if (res1.ok){
            console.log(data)
            this.stats1.song_count=data.song_count;
            this.stats1.album_count=data.album_count;
            this.stats1.user_count=data.user_count;
            this.stats1.user_active=data.user_active;
            this.stats1.song_active=data.song_active;
            this.stats1.album_active=data.album_active;
            this.stats1.user_flag=data.user_flag;
            this.stats1.song_flag=data.song_flag;
            this.stats1.album_flag=data.album_flag;
            this.song_bar.months=data.song_bar.months;
            this.song_bar.counts=data.song_bar.counts;
            this.role_pie.distri=data.role_pie.distri;
            this.role_pie.labels=data.role_pie.labels;
            this.user_line.user_months=data.user_line.user_months;
            this.user_line.user_counts=data.user_line.user_counts;
            this.unique_genre=data.unique_genre


           
        }


        const res2=await fetch(`http://localhost:5000/ranking`,{
            headers:{
                       'Authentication-Token':this.cred.authtoken,
                        'User-Role':this.cred.user_role}

        })

        const data2=await res2.json()
        if(res2.ok){
            this.top_songs=data2

        }

    //fetchig the top creators
    const res3=await fetch('http://localhost:5000/creator_rank',{
            headers:{
                       'Authentication-Token':this.cred.authtoken,
                        'User-Role':this.cred.user_role}

    })
     const data3=await res3.json()
        if(res3.ok){
            this.top_creators=data3
            

        }

    //instantiate new chart and provide 2 arguments,: the canvas element where the chart would be rendered and the options object.
        new Chart(
    document.getElementById('line_chart1'),
    {
      type: 'line',//define the chart type
      data: {
        labels: this.song_bar.months,//horizontal data
        datasets: [
          {
            label: 'Songs uploaded by month', //appear as the legend
            data: this.song_bar.counts, //for y ,
             borderColor: 'rgb(75, 192, 192)',
          }
        ]
      }
    }
  );
  //role_pie
    new Chart(
    document.getElementById('role_pie'),
    {
      type: 'pie',//define the chart type
      data: {
        labels: this.role_pie.labels,//horizontal data
        datasets: [
          {
            label: 'Role distribution', //appear as the legend
            data: this.role_pie.distri, //for y ,
             borderColor: 'rgb(75, 192, 192)',
                backgroundColor: [
      'rgb(255, 99, 132)',
      'rgb(54, 162, 235)',
      'rgb(255, 205, 86)'
    ],
    
          }
        ]
      }
    }
  );

  //user_line
   new Chart(
    document.getElementById('user_line'),
    {
      type: 'line',//define the chart type
      data: {
        labels: this.user_line.user_months,//horizontal data
        datasets: [
          {
            label: 'User registration by month', //appear as the legend
            data: this.user_line.user_counts, //for y ,
             borderColor: 'rgb(75, 192, 192)',
          }
        ]
      }
    }
  );



  //genre_bar
   new Chart(
    document.getElementById('genre_bar'),
    {
      type: 'bar',//define the chart type
      data: {
        labels: Object.keys(this.unique_genre),//horizontal data
        datasets: [
          {
            label: 'Distribution by genre', //appear as the legend
            data: Object.values(this.unique_genre), //for y ,
          
          }
        ]
      }
    }
  );









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



th,td{
    font-size:1.5rem;
    padding: 15px;
    margin-right:1rem;
    overflow-wrap: break-word;

}
table,th,td{
     border: 2px solid black;
  border-collapse: collapse;
}
tr:nth-child(even) {
  background-color: #D6EEEE;
}
.stats2{
    display: flex;
    flex-direction: column;
    align-items: center;
    
   


}
.stats3{
      display: flex;
    flex-direction: column;
    align-items: center;
    grid-column: 3/5;
    grid-row:2/3;
    background-color:;

}

.charts{
   grid-column: 1/5;
    grid-row:3/4;
    display: flex;
    justify-content: space-between;
    margin-top:3rem;
    margin-bottom:3rem;

}

buttons{
  background-color:aliceblue
}
img{
    width:auto;
    height:30rem;
    border: 2px solid black;

}
/* .chart1{
     grid-column: 1/4;
    grid-row:2/3;

} */
.stats1{
    margin:4rem;
    padding:2rem;
    background-color:lightblue;
    grid-column:1/5;
    grid-row:1/2;
    

    
}
.stats2{
     grid-column:1/2;
    grid-row:2/3;
    

}
.cards_{

    display: flex;
    justify-content: space-between;
}
.card-title{
    text-align: center;

}
.card-text{
    display:flex;
    justify-content: space-around;
    text-align: center;
}
.link{
    display: flex;
    justify-content: flex-end;
}

.main2{
    background-color:lightcyan;
    height:100%;
     margin:2rem;
    display: grid;
    grid-template-rows: 1/4;
    grid-template-columns: 1/5;
    /* grid-template-columns: repeat(5,1fr);
    grid-template-rows: repeat(5,1fr); */
    


   
}

</style>