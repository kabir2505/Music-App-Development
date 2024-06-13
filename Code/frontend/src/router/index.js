import { createRouter, createWebHistory } from 'vue-router'
import HelloWorld from '../views/HelloWorld.vue'
import LoginView from '../views/LoginView'
import AdminLogin  from '../views/AdminLogin'
import UserHome from '../views/UserHome'
import AdminHome from '../views/AdminHome'
import RegisterUser  from '../views/Register'
import All_Stuff from '../views/All_Stuff'
import NotFound from '../views/NotFound'
import CreatorHome from '../views/CreatorHome'
import uploadAlbum from '../views/upload_album'
import albumsong from '../views/Album-song.vue'
import songv from '../views/songs.vue'
import All_Albums from '../views/All_albums.vue'
import Edit_Album from '../views/edit_album.vue'
import upload_playlist from '../views/upload_playlist.vue'
import All_playlists from '../views/All_playlists.vue'
import Playlist_song from '../views/Playlist-song.vue'
import Edit_Playlist from '../views/edit_playlist.vue'
import All_Users from '../views/All_Users.vue'
import Search_Result from '../views/Search_Result.vue'
import Profile from '../views/Profile.vue'
const routes = [
  {
    path: '/',
    name: 'HelloWorld',
    component: HelloWorld
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path:'/signup',
    name:'signup',
    component:RegisterUser,
  },
  {
    path:'/login',
    name:'login',
    component:LoginView
  },
  {
    path:'/admlogin',
    name:'adminlogin',
    component:AdminLogin

  },
  {
    path:'/userhome',
    name:'userhome',
    component:UserHome,
    beforeEnter:(to,from,next)=>{
      const authtoken=localStorage.getItem('auth-token')
      const userrole=localStorage.getItem('role')

      if (authtoken && (userrole=='norm_user' || userrole=='creator')){
        next()
      }else {
        next({path:'/login',query:{message:'Please login first!'}})
      }

    }
  },
  {
    path:'/adminhome',
    name:'adminhome',
    component:AdminHome,
    beforeEnter:(to,from,next)=>{
      const authtoken=localStorage.getItem('auth-token')
      const userrole=localStorage.getItem('role')
      if (authtoken && userrole=='admin'){
        next()
      }else {
        next({path:'/login',query:{message:'Please login first!'}})
      }


    }

  },
  {
    path:'/all_stuff/:id',
    //1->all_songs, 2->all_albums, 3->all_playlists, 4-> all users
    name:'all_stuff',
    component:All_Stuff,

  },
  {
    path:'/creatorhome',
    name:'creator_home',
    component:CreatorHome
  },
  {
    path:'/:pathMatch(.*)*',
    name:'Not_found',
    component:NotFound

  },
  {
    path:'/upload-album',
    name:'uploadAlbum',
    component:uploadAlbum
  },
{
  path:'/album_song/:wish/:aid',
  name:'albumsong',
  component:albumsong

},
{
  path:'/all_songs/:wish',
  name:'songs',
  component:songv
  //100->all songs for user(rating) and admin(flag)

},
{
  path:'/all_albums/:wish',
  name:'albums',
  component:All_Albums
  //100->all albums for user and admin(flag)
  //300->for creator with own particular albums
},
{
  path:'/edit_album/:a_id',
  name:'edit_album',
  component:Edit_Album
},
{
  path:'/upload_playlist',
  name:'upload_playlist',
  component:upload_playlist
},
{
  path:'/all_playlists',
  name:'all_playlists',
  component:All_playlists
},
{
  path:'/playlist_song/:pid',
  name:'Playlist_song',
  component:Playlist_song

},
{
  path:'/edit_playlist/:pid',
  name:'Edit_Playlist',
  component:Edit_Playlist
},
{
  path:'/all_users',
  name:'All_users',
  component:All_Users
},
{
  path:'/search_result',
  name:'search_Result',
  component:Search_Result
},
{
  path:'/profile/:id',
  name:'profile',
  component:Profile
}

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
