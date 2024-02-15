<template>
  <li
    class="flex justify-between items-center p-3 pl-6 cursor-pointer transition duration-300 hover:bg-gray-50"
  >
    <div>
      <router-link :to="songPage" class="font-bold block text-gray-600">{{
        song.modifiedName
      }}</router-link>
      <span class="text-gray-500 text-sm">{{ song.user.name }}</span>
    </div>

    <div class="text-gray-600 text-lg">
      <router-link custom :to="songComment" v-slot="{ navigate }">
        <span class="comments" @click="navigate">
          <i class="fa fa-comments text-gray-600"></i>
          {{ song.commentCount }}
        </span>
      </router-link>
    </div>
  </li>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps(['song'])
const songPage = computed(() => {
  return {
    name: 'song',
    params: { songId: props.song.id }
  }
})
const songComment = computed(() => {
  return {
    name: 'song',
    params: { songId: props.song.id },
    hash: '#comments'
  }
})
</script>
