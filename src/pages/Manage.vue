<template>
  <main>
    <!-- Main Content -->
    <section class="container mx-auto mt-6">
      <div class="md:grid md:grid-cols-3 md:gap-4">
        <div class="col-span-1">
          <app-upload @addThisSong="addSong"></app-upload>
        </div>
        <div class="col-span-2">
          <div class="bg-white rounded border border-gray-200 relative flex flex-col">
            <div class="px-6 pt-6 pb-5 font-bold border-b border-gray-200">
              <span class="card-title">{{ $t('manage.mySongs') }}</span>
              <i class="fa fa-compact-disc float-right text-green-400 text-2xl"></i>
            </div>
            <div class="p-6">
              <!-- Composition Items -->
              <composition-item
                v-for="song in songs"
                :key="song.id"
                :song="song"
                @modifiedSongName="updateSoneName"
                @removedThisSong="removeSong"
                @unsavedStatu="unSavedSong"
              ></composition-item>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>
</template>

<script setup>
import { reactive } from 'vue'
import AppUpload from '@/components/Upload.vue'
import CompositionItem from '@/components/CompositionItem.vue'
import axios from 'axios'
import { onBeforeRouteLeave } from 'vue-router'

const songs = reactive([])
const getsongs = async () => {
  await axios
    .get(import.meta.env.VITE_API_BASE_URL + '/file/userSongs', {
      headers: { Authorization: `Bearer ${localStorage.token}` }
    })
    .then((response) => {
      songs.push(...response.data)
    })
    .catch((error) => {
      console.log(error)
    })
}
getsongs()

const addSong = (data) => {
  songs.push(data)
}
const unSavedSong = (data) => {
  const tar = songs.find((song) => song.id === data.id)
  if (tar) {
    tar.unsaved = data.unsaved
  }
}
const updateSoneName = (data) => {
  const tar = songs.find((song) => song.id === data.id)
  if (tar) {
    tar.modifiedName = data.content.modifiedName
  }
}
const removeSong = (data) => {
  const indexToRemove = songs.findIndex((song) => song.id === data.id)
  if (indexToRemove !== -1) {
    songs.splice(indexToRemove, 1)
  }
}

onBeforeRouteLeave((to, from, next) => {
  const unsavedStatu = songs.find((song) => song.unsaved == true)
  if (unsavedStatu !== undefined) {
    const leave = confirm('You have unsaved changes. Are you sure to leave?')
    next(leave)
  } else {
    next()
  }
})
</script>
