<template>
  <div class="bg-white rounded border border-gray-200 relative flex flex-col">
    <div class="px-6 pt-6 pb-5 font-bold border-b border-gray-200">
      <span class="card-title">{{ $t('manage.upload') }}</span>
      <i class="fas fa-upload float-right text-green-400 text-2xl"></i>
    </div>
    <div class="p-6">
      <!-- Upload Dropbox -->
      <div
        class="w-full px-10 py-20 rounded text-center cursor-pointer border border-dashed border-gray-400 text-gray-400 transition duration-500 hover:text-white hover:bg-green-400 hover:border-green-400 hover:border-solid"
        :class="{ 'bg-green-400 border-green-400 border-solid': isDragover }"
        @drag.prevent.stop=""
        @dragstart.prevent.stop=""
        @dragend.prevent.stop="setIsDragover(false)"
        @dragover.prevent.stop="setIsDragover(true)"
        @dragenter.prevent.stop="setIsDragover(true)"
        @dragleave.prevent.stop="setIsDragover(false)"
        @drop.prevent.stop="upload"
      >
        <h5>{{ $t('manage.uploadZone') }}</h5>
      </div>
      <input type="file" multiple @change="upload" />
      <hr class="my-6" />
      <!-- Progess Bars -->
      <div class="mb-4" v-for="item in uploadItems" :key="item.name">
        <!-- File Name -->
        <div class="font-bold text-sm" :class="item.textClass">
          <i :class="item.icon"></i>{{ item.name }}
        </div>
        <div class="flex h-4 overflow-hidden bg-gray-200 rounded">
          <!-- Inner Progress Bar -->
          <div
            class="transition-all progress-bar"
            :class="item.variant"
            :style="{ width: item.currentProgress + '%' }"
          ></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, onBeforeUnmount } from 'vue'
import axios from 'axios'

const emit = defineEmits(['addThisSong'])

const isDragover = ref(false)
const setIsDragover = (value = false) => {
  isDragover.value = value
}
const uploadItems = reactive([])
const upload = (event) => {
  setIsDragover(false)
  const files = event.dataTransfer ? [...event.dataTransfer.files] : [...event.target.files]
  files.forEach(async (file) => {
    console.log('Now upload', file)
    if (file.type !== 'audio/mpeg') {
      return
    } else {
      let formData = new FormData()
      formData.append('file', file)
      const cancelTokenSource = axios.CancelToken.source()
      const uploadIndex =
        uploadItems.push({
          file,
          currentProgress: 0,
          name: file.name,
          variant: 'bg-blue-400',
          icon: 'fas fa-spinner fa-spin',
          textClass: '',
          cancelUploadToken: cancelTokenSource
        }) - 1
      await axios
        .post(import.meta.env.VITE_API_BASE_URL + '/file/song', formData, {
          headers: { Authorization: `Bearer ${localStorage.token}` },
          cancelToken: cancelTokenSource.token,
          onUploadProgress: (progressEvent) => {
            const uploadProgress = Math.round((progressEvent.loaded / progressEvent.total) * 100)
            uploadItems[uploadIndex].currentProgress = uploadProgress
          }
        })
        .then((response) => {
          uploadItems[uploadIndex].variant = 'bg-green-400'
          uploadItems[uploadIndex].icon = 'fas fa-check'
          uploadItems[uploadIndex].textClass = 'text-green-400'
          console.log('Upload success!', response)
          emit('addThisSong', response.data)
        })
        .catch((error) => {
          uploadItems[uploadIndex].variant = 'bg-red-400'
          uploadItems[uploadIndex].icon = 'fas fa-times'
          uploadItems[uploadIndex].textClass = 'text-red-400'
          console.log('Upload fail!', error)
        })
    }
  })
}
onBeforeUnmount(() => {
  uploadItems.forEach((item) => {
    item.cancelUploadToken.cancel()
    console.log('Cancel upload!', item.name)
  })
})
</script>
