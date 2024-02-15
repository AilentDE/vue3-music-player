<template>
  <main>
    <!-- Music Header -->
    <section class="w-full mb-8 py-14 text-center text-white relative">
      <div
        class="absolute inset-0 w-full h-full box-border bg-contain music-bg"
        style="background-image: url(/assets/img/song-header.png)"
      ></div>
      <div class="container mx-auto flex items-center">
        <!-- Play/Pause Button -->
        <button
          @click.prevent="playSong"
          type="button"
          class="z-50 h-24 w-24 text-3xl bg-white text-black rounded-full focus:outline-none"
        >
          <i class="fas" :class="allowPlaySong ? 'fa-play' : 'fa-pause'"></i>
        </button>
        <div class="z-50 text-left ml-8">
          <!-- Song Info -->
          <div v-if="!song.modifiedName">
            <span class="text-3xl text-white">
              <i class="fas fa-spinner fa-spin"></i>
            </span>
          </div>
          <div class="text-3xl font-bold">{{ song.modifiedName }}</div>
          <div>{{ song.genre }}</div>
        </div>
      </div>
    </section>
    <!-- Form -->
    <song-comment-form
      :songId="route.params.songId"
      :sortBy="sortBy"
      :commentCount="song.commentCount"
      @postComment="updateComment"
      @changeSortBy="changeSortBy"
    ></song-comment-form>
    <!-- Comments -->
    <ul class="container mx-auto" name="comments">
      <li
        v-for="comment in comments"
        class="p-6 bg-gray-50 border border-gray-200"
        :key="comment.id"
      >
        <!-- Comment Author -->
        <div class="mb-5">
          <div class="font-bold">{{ comment.user.name }}</div>
          <time>{{ comment.createdAt }}</time>
        </div>

        <p>
          {{ comment.content }}
        </p>
      </li>
      <li v-show="pendingRequest" class="flex justify-center p-6 bg-gray-50 border border-gray-200">
        <i class="fas fa-spinner fa-spin"></i>
      </li>
    </ul>
  </main>
</template>

<script setup>
import SongCommentForm from '@/components/form/SongCommentForm.vue'
import { reactive, ref, computed, onBeforeUnmount } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'
import qs from 'qs'
import { usePlayerStore } from '@/stores/player'
import { storeToRefs } from 'pinia'

const route = useRoute()
const router = useRouter()
const playerStore = usePlayerStore()
const { playingState } = storeToRefs(playerStore)
const allowPlaySong = computed(() => {
  if (playerStore.currentSong?.id == song.id && playingState.value) {
    return false
  } else {
    return true
  }
})

const song = reactive({})
const loadSong = async () => {
  await axios
    .get(import.meta.env.VITE_API_BASE_URL + '/file/song/' + route.params.songId)
    .then((response) => {
      Object.assign(song, response.data)
    })
    .catch((error) => {
      console.log(error)
      router.push({ name: 'home' })
    })
}
const playSong = () => {
  if (playerStore.currentSong?.id == song.id) {
    playerStore.toggleAudio()
  } else {
    playerStore.newSong(route.params.songId)
    playerStore.setCurrentSong(song)
  }
}
// created
loadSong()

let comments = reactive([])
const limit = 20
let skip = 0
const sortBy = ref('-1')
const pendingRequest = ref(false)
const loadComment = async () => {
  pendingRequest.value = true

  const params = qs.stringify({ limit, skip, sortBy: sortBy.value }, { addQueryPrefix: true })
  await axios
    .get(import.meta.env.VITE_API_BASE_URL + '/comment/song/' + route.params.songId + params)
    .then((response) => {
      if (response.data.length === 0) {
        pendingRequest.value = false
      } else {
        comments.push(...response.data)
        skip += limit
        pendingRequest.value = false
      }
    })
    .catch((error) => {
      console.log(error)
    })
}
// created
loadComment()
// handleScroll
const handleScroll = async () => {
  const { scrollTop, offsetHeight } = document.documentElement
  const { innerHeight } = window
  const bottomOfWindow = Math.round(scrollTop) + innerHeight === offsetHeight

  if (pendingRequest.value) {
    return
  } else if (bottomOfWindow) {
    console.log('load data!')
    loadComment()
  }
}
window.addEventListener('scroll', handleScroll)
onBeforeUnmount(() => {
  window.removeEventListener('scroll', handleScroll)
})

const updateComment = async () => {
  const params = qs.stringify({ limit: 1, skip: 0, sortBy: sortBy.value }, { addQueryPrefix: true })
  await axios
    .get(import.meta.env.VITE_API_BASE_URL + '/comment/song/' + route.params.songId + params)
    .then((response) => {
      comments.unshift(...response.data)
    })
    .catch((error) => {
      console.log(error)
    })
}
const changeSortBy = async (value) => {
  sortBy.value = value
  skip.value = 0
  comments = reactive([])
  const params = qs.stringify(
    { limit: limit.value, skip: skip.value, sortBy: sortBy.value },
    { addQueryPrefix: true }
  )
  await axios
    .get(import.meta.env.VITE_API_BASE_URL + '/comment/song/' + route.params.songId + params)
    .then((response) => {
      comments.push(...response.data)
    })
    .catch((error) => {
      console.log(error)
    })
}
</script>
