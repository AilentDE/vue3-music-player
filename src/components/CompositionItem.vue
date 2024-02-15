<template>
  <div class="border border-gray-200 p-3 mb-4 rounded">
    <div v-if="!showForm" class="flex items-center justify-between">
      <h4 class="flex-grow text-2xl font-bold">{{ song.modifiedName }}</h4>
      <div class="flex">
        <button
          class="ml-1 py-1 px-2 text-sm rounded text-white bg-blue-600 float-right"
          @click.prevent="changeShowForm"
        >
          <i class="fa fa-pencil-alt"></i>
        </button>
        <button
          class="ml-1 py-1 px-2 text-sm rounded text-white bg-red-600 float-right"
          :disabled="log.inSubmission"
          @click.prevent="deleteSong"
        >
          <i class="fa fa-times"></i>
        </button>
      </div>
    </div>
    <div v-else>
      <div
        class="text-white text-center font-bold p-4 mb-4"
        :class="log.alertVariant"
        v-if="log.showAlert"
      >
        {{ log.alertMsg }}
      </div>
      <form>
        <div class="mb-3">
          <label class="inline-block mb-2">{{ $t('manage.songItem.title') }}</label>
          <input
            type="text"
            class="block w-full py-1.5 px-3 text-gray-800 border border-gray-300 transition duration-500 focus:outline-none focus:border-black rounded"
            placeholder="Enter Song Title"
            v-model="modifiedName"
            v-bind="modifiedNameAttrs"
            @input="unsavedData"
          />
        </div>
        <p class="text-red-600">{{ errors.modifiedName }}</p>
        <div class="mb-3">
          <label class="inline-block mb-2">{{ $t('manage.songItem.genre') }}</label>
          <input
            type="text"
            class="block w-full py-1.5 px-3 text-gray-800 border border-gray-300 transition duration-500 focus:outline-none focus:border-black rounded"
            placeholder="Enter Genre"
            v-model="genre"
            v-bind="genreAttrs"
            @input="unsavedData"
            disabled="true"
          />
        </div>
        <p class="text-red-600">{{ errors.genre }}</p>
        <button
          type="submit"
          class="py-1.5 px-3 rounded text-white bg-green-600"
          @click.prevent="editSubmit"
          :disabled="log.inSubmission"
        >
          Submit
        </button>
        <button
          type="button"
          class="py-1.5 px-3 rounded text-white bg-gray-600"
          @click.prevent="changeShowForm"
          :disabled="log.inSubmission"
        >
          Go Back
        </button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
import { useForm } from 'vee-validate'
import { toTypedSchema } from '@vee-validate/yup'
import * as yup from 'yup'
import axios from 'axios'

const props = defineProps({
  song: {
    type: Object,
    required: true
  }
})
const emit = defineEmits(['modifiedSongName', 'removedThisSong', 'unsavedStatu'])

const showForm = ref(false)
const changeShowForm = () => {
  showForm.value = !showForm.value
}

const unsavedData = () => {
  emit('unsavedStatu', { id: props.song.id, unsaved: true })
}
// song schema
const songSchema = toTypedSchema(
  yup.object({
    modifiedName: yup.string().required(),
    genre: yup.string()
  })
)
const { errors, handleSubmit, defineField } = useForm({
  validationSchema: songSchema,
  initialValues: {
    modifiedName: props.song.modifiedName
  }
})
const [modifiedName, modifiedNameAttrs] = defineField('modifiedName')
const [genre, genreAttrs] = defineField('genre')

const log = reactive({
  inSubmission: false,
  showAlert: false,
  alertVariant: 'bg-blue-500',
  alertMsg: 'Now updating...'
})
const editSubmit = handleSubmit(async (values) => {
  log.inSubmission = true
  log.showAlert = false
  await axios
    .patch(import.meta.env.VITE_API_BASE_URL + '/file/song/' + props.song.id, values, {
      headers: { Authorization: `Bearer ${localStorage.token}` }
    })
    .then(() => {
      emit('modifiedSongName', { id: props.song.id, content: values })
      emit('unsavedStatu', { id: props.song.id, unsaved: false })
      log.inSubmission = false
      log.showAlert = true
      log.alertVariant = 'bg-green-500'
      log.alertMsg = 'Success!'
      setTimeout(() => {
        log.showAlert = false
        showForm.value = false
      }, 500)
    })
    .catch((error) => {
      log.inSubmission = false
      log.showAlert = true
      log.alertVariant = 'bg-red-500'
      log.alertMsg = error.response.data.detail[0].msg
    })
})

const deleteSong = async () => {
  await axios
    .delete(import.meta.env.VITE_API_BASE_URL + '/file/song/' + props.song.id, {
      headers: { Authorization: `Bearer ${localStorage.token}` }
    })
    .then(() => {
      emit('removedThisSong', { id: props.song.id })
    })
    .catch((error) => {
      log.inSubmission = false
      log.showAlert = true
      log.alertVariant = 'bg-red-500'
      log.alertMsg = error.response.data.detail[0].msg
    })
}
</script>
