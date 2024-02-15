<template>
  <section class="container mx-auto mt-6">
    <div class="bg-white rounded border border-gray-200 relative flex flex-col">
      <div class="px-6 pt-6 pb-5 font-bold border-b border-gray-200">
        <!-- Comment Count -->
        <span class="card-title">{{
          $t('song.commentCount', commentCount, { count: commentCount })
        }}</span>
        <i class="fa fa-comments float-right text-green-400 text-2xl"></i>
      </div>
      <div class="p-6" v-if="userLoggedIn">
        <div
          class="text-white text-center font-bold p-4 mb-4"
          :class="log.alertVariant"
          v-if="log.showAlert"
        >
          {{ log.alertMsg }}
        </div>
        <form @submit="commentSubmit">
          <textarea
            class="block w-full py-1.5 px-3 text-gray-800 border border-gray-300 transition duration-500 focus:outline-none focus:border-black rounded mb-4"
            placeholder="Your comment here..."
            v-model="content"
            v-bind="contentAttrs"
            :disabled="log.inSubmission"
          ></textarea>
          <p class="text-red-600">{{ errors.content }}</p>
          <button
            type="submit"
            class="py-1.5 px-3 rounded text-white bg-green-600 block"
            :disabled="log.inSubmission"
          >
            Submit
          </button>
        </form>
        <!-- Sort Comments -->
        <select
          class="block mt-4 py-1.5 px-3 text-gray-800 border border-gray-300 transition duration-500 focus:outline-none focus:border-black rounded"
          @change="changeSortBy"
        >
          <option value="-1">Latest</option>
          <option value="1">Oldest</option>
        </select>
      </div>
    </div>
  </section>
</template>

<script setup>
import { computed, ref, reactive, toRefs } from 'vue'
import { useForm } from 'vee-validate'
import { toTypedSchema } from '@vee-validate/yup'
import * as yup from 'yup'
import { useUserStore } from '@/stores/user'
import { storeToRefs } from 'pinia'
import axios from 'axios'

const props = defineProps(['songId', 'sortBy', 'commentCount', 'loadSong'])
const { sortBy } = toRefs(props)
const emits = defineEmits(['postComment', 'changeSortBy'])
const userStore = useUserStore()
const { userLoggedIn } = storeToRefs(userStore)

// comment schema
const commentSchema = toTypedSchema(
  yup.object({
    content: yup.string().required().min(3).max(500)
  })
)
const { errors, handleSubmit, resetForm, defineField } = useForm({
  validationSchema: commentSchema
})
const [content, contentAttrs] = defineField('content')
const log = reactive({
  inSubmission: false,
  showAlert: false,
  alertVariant: 'bg-blue-500',
  alertMsg: 'Please wait. Comment sending.'
})
const newCommentCount = ref(0)
const commentSubmit = handleSubmit(async (values) => {
  log.inSubmission = true
  log.showAlert = false

  values.songId = props.songId
  await axios
    .post(import.meta.env.VITE_API_BASE_URL + '/comment/song', values, {
      headers: { Authorization: `Bearer ${localStorage.token}` }
    })
    .then((response) => {
      resetForm()
      if (sortBy.value == -1) {
        emits('postComment', response.data)
      }
      newCommentCount.value += 1
      log.inSubmission = false
      log.showAlert = true
      log.alertVariant = 'bg-green-500'
      log.alertMsg = 'Success!'
      setTimeout(() => {
        log.showAlert = false
      }, 1000)
    })
    .catch((error) => {
      log.inSubmission = false
      log.showAlert = true
      log.alertVariant = 'bg-red-500'
      log.alertMsg = error.response?.data.detail[0].msg || error.message
    })
})

const changeSortBy = (event) => {
  emits('changeSortBy', event.target.value)
}

const commentCount = computed(() => {
  if (props.commentCount && newCommentCount) {
    return props.commentCount + newCommentCount.value
  } else {
    return 0
  }
})
</script>
