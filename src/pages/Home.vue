<template>
  <main>
    <!-- Introduction -->
    <section class="mb-8 py-20 text-white text-center relative">
      <div
        class="absolute inset-0 w-full h-full bg-contain introduction-bg"
        style="background-image: url(assets/img/header.png)"
      ></div>
      <div class="container mx-auto">
        <div class="text-white main-header-content">
          <h1 class="font-bold text-5xl mb-5">{{ $t('home.listen') }}</h1>
          <p class="w-full md:w-8/12 mx-auto">
            {{ $t('home.introduce') }}
          </p>
        </div>
      </div>

      <img
        class="relative block mx-auto mt-5 -mb-20 w-auto max-w-full"
        src="/assets/img/introduction-music.png"
      />
    </section>

    <!-- Main Content -->
    <section class="container mx-auto">
      <div class="bg-white rounded border border-gray-200 relative flex flex-col">
        <div class="px-6 pt-6 pb-5 font-bold border-b border-gray-200">
          <span class="card-title">{{ $t('home.songs') }}</span>
          <!-- Icon -->
          <i class="fa fa-headphones-alt float-right text-green-400 text-xl"></i>
        </div>
        <!-- Playlist -->
        <ol id="playlist">
          <song-item v-for="song in songs" :key="song.id" :song="song"></song-item>
        </ol>
        <div v-show="pendingRequest" class="flex my-6 justify-center">
          <i class="fas fa-spinner fa-spin"></i>
        </div>
        <!-- .. end Playlist -->
      </div>
    </section>
  </main>
</template>

<script setup>
import { ref, reactive, onBeforeUnmount } from 'vue'
import axios from 'axios'
import qs from 'qs'
import SongItem from '@/components/SongItem.vue'

const songs = reactive([])
const limit = 5
let skip = 0
const pendingRequest = ref(false)
const getSongs = async () => {
  pendingRequest.value = true

  const params = qs.stringify({ limit, skip }, { addQueryPrefix: true })
  await axios
    .get(import.meta.env.VITE_API_BASE_URL + '/file/songs' + params)
    .then((response) => {
      if (response.data.length === 0) {
        pendingRequest.value = false
      } else {
        songs.push(...response.data)
        skip += limit
        pendingRequest.value = false
      }
    })
    .catch((error) => {
      console.log(error)
    })
}
// created
getSongs()
// handleScroll
const handleScroll = async () => {
  const { scrollTop, offsetHeight } = document.documentElement
  const { innerHeight } = window
  const bottomOfWindow = Math.round(scrollTop) + innerHeight === offsetHeight

  if (pendingRequest.value) {
    return
  } else if (bottomOfWindow) {
    console.log('load data!')
    getSongs()
  }
}
window.addEventListener('scroll', handleScroll)
onBeforeUnmount(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>
