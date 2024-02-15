import { computed, reactive, ref } from 'vue'
import { defineStore } from 'pinia'
import { Howl } from 'howler'
import { formatTime } from '@/includes/helper'

export const usePlayerStore = defineStore('player', () => {
  const currentSong = reactive({})
  const setCurrentSong = (song) => {
    Object.assign(currentSong, song)
  }

  const sound = reactive({})
  const playerProgress = ref('0%')
  const newSong = async (song_id) => {
    if (sound.howl && sound.howl instanceof Howl) {
      sound.howl.unload()
    }
    const songUrl = 'http://localhost:8000/file/song/' + song_id + '/play'
    sound.howl = new Howl({
      src: [songUrl],
      html5: true,
      volume: 0.5
    })
    sound.currentSoundId = sound.howl.play()
    sound.howl.on('play', () => {
      requestAnimationFrame(progress)
    })
  }
  const progress = () => {
    sound.seek = sound.howl.seek()
    playerProgress.value = `${(sound.howl.seek() / currentSong.duration) * 100}%`

    if (sound.howl.playing()) {
      requestAnimationFrame(progress)
    }
  }
  const seek = computed(() => formatTime(sound.seek))
  const duration = computed(() => formatTime(currentSong.duration))
  const playingState = computed(() => {
    if (!sound.howl?.playing) {
      return false
    }

    return sound.howl.playing()
  })

  const toggleAudio = async () => {
    if (!sound.howl?.playing) {
      return
    }
    if (sound.howl.playing()) {
      sound.howl.pause()
    } else {
      sound.howl.play()
    }
  }
  const updateSeek = (progressPercent) => {
    if (!sound.howl?.playing) {
      return
    }
    console.log(progressPercent, '%')
    // ex. Document=2000, Timeline=1000, clientX=1000, Distance=500
    const seconds = currentSong.duration * progressPercent
    console.log('秒數', seconds)

    sound.howl.seek(seconds)
    sound.howl.once('seek', progress)
  }

  return {
    currentSong,
    seek,
    duration,
    playerProgress,
    playingState,
    setCurrentSong,
    newSong,
    toggleAudio,
    updateSeek
  }
})
