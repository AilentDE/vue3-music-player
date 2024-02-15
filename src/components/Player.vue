<template>
  <div class="fixed bottom-0 left-0 bg-white px-4 py-2 w-full">
    <!-- Track Info -->
    <div class="text-center" v-if="currentSong.modifiedName && currentSong.user?.name">
      <span class="song-title font-bold">{{ currentSong.modifiedName }}</span>
      by
      <span class="song-artist">{{ currentSong.user.name }}</span>
    </div>
    <div class="flex flex-nowrap gap-4 items-center">
      <!-- Play/Pause Button -->
      <button type="button" @click.prevent="toggleAudio">
        <i class="fa text-gray-500 text-xl" :class="playingState ? 'fa-pause' : 'fa-play'"></i>
      </button>
      <!-- Current Position -->
      <div class="player-currenttime">{{ seek }}</div>
      <!-- Scrub Container  -->
      <div
        @click.prevent="playBarInfo"
        ref="playerBar"
        class="w-full h-2 rounded bg-gray-200 relative cursor-pointer"
      >
        <!-- Player Ball -->
        <span
          class="absolute -top-2.5 -ml-2.5 text-gray-800 text-lg"
          :style="{ left: playerProgress }"
        >
          <i class="fas fa-circle"></i>
        </span>
        <!-- Player Progress Bar-->
        <span
          class="block h-2 rounded bg-gradient-to-r from-green-500 to-green-400"
          :style="{ width: playerProgress }"
        ></span>
      </div>
      <!-- Duration -->
      <div class="player-duration">{{ duration }}</div>
    </div>
  </div>
</template>

<script setup>
import { usePlayerStore } from '@/stores/player'
import { storeToRefs } from 'pinia'
import { ref } from 'vue'

const playerStore = usePlayerStore()
const { toggleAudio, updateSeek } = playerStore
const { currentSong, playingState, seek, duration, playerProgress } = storeToRefs(playerStore)

const playerBar = ref(null)
const playBarInfo = (event) => {
  const { x, width } = playerBar.value.getBoundingClientRect()
  const progressPercent = (event.x - x) / width
  updateSeek(progressPercent)
}
</script>
