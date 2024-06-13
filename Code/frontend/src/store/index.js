import { createStore } from 'vuex'

export default createStore({
  state: {
    //collection(albums,playlists) // current-track //whether the audiobar is playling a song
    collection:[],
    currentTrack:null,
    isPlaying:false

  },
  getters: {

  },
  //actions commit mutations, mutations lead to change in the data
  mutations: {
    //set current track
    setCurrentTrack(state,track){
      state.currentTrack=track
      console.log('inside store',state.currentTrack)
    },
    //set whether the application is playling or not
    setPlaying(state,isPlaying){
      state.isPlaying=isPlaying;
    },
    //setting an album or a playlit // use this while applying the autoshuffle functionality as well
    setCollection(state,collection){
      state.collection=collection
    }
  },
  actions: {
    //caution!-> audiobar is set to autoplay mode!
    //playing individual songs 
    playTrack({commit},track){
      commit('setCurrentTrack',track)
      console.log('inside actions',track.song_audio)
      commit('setPlaying',true)
    },
    //pausing a song
    pauseTrack({commit}){
      commit('setPlaying',false)
    },
    //forward>>
    playNextTrack({dispatch,commit,state}){
      const currenti=state.collection.findIndex(j=>j.sid==state.currentTrack.sid) //finding the index of the song from the collection
    
      const nexti=(currenti+1)%state.collection.length
      const nextTrack=state.collection[nexti]
      if (nextTrack){
        dispatch('playTrack',nextTrack);} //only move on, if the next track exists!
    },
    playCollection({dispatch,commit,state},collection){
      console.log('inside play collection acn',collection)
      collection=collection.song    //because collection is an album and album.song contains all the songs, hence, colleciton.song
      commit('setCollection',collection) //commiting a mutation
      
      let track=collection[0]
      console.log(track)
      dispatch('playTrack',track)
      commit('setPlaying',true)
      

    },

    //core functionality: shuffling a collection (an album/a playlist)
    shuffleCollection({dispatch,commit,state},collection){ 
      collection=collection.song;
      function shuffle(array) {
        array.sort(() => Math.random() - 0.5);
      };
      shuffle(collection);
      commit('setCollection',collection)
      
      let track=collection[0]
      console.log(track)
      dispatch('playTrack',track)
      commit('setPlaying',true)
      


    }

  },
  modules: {
  }
})
