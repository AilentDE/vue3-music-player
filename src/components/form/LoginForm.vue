<template>
  <form>
    <!-- Email -->
    <div class="mb-3">
      <label class="inline-block mb-2">{{ $t('auth.login.email') }}</label>
      <input
        type="email"
        class="block w-full py-1.5 px-3 text-gray-800 border border-gray-300 transition duration-500 focus:outline-none focus:border-black rounded"
        placeholder="Enter Email"
        v-model="email"
        v-bind="emailAttrs"
      />
      <p class="text-red-600">{{ loginErrors.email }}</p>
    </div>
    <!-- Password -->
    <div class="mb-3">
      <label class="inline-block mb-2">{{ $t('auth.login.password') }}</label>
      <input
        type="password"
        class="block w-full py-1.5 px-3 text-gray-800 border border-gray-300 transition duration-500 focus:outline-none focus:border-black rounded"
        placeholder="Password"
        v-model="password"
        v-bind="passwordAttrs"
      />
      <p class="text-red-600">{{ loginErrors.password }}</p>
    </div>
    <button
      class="block w-full bg-purple-600 text-white py-1.5 px-3 rounded transition hover:bg-purple-700"
      @click.prevent="loginSubmit"
      :disabled="log.inSubmission"
    >
      Submit
    </button>
    <div
      class="text-white text-center font-bold p-4 my-4 rounded"
      v-if="log.showAlert"
      :class="log.alertVariant"
    >
      {{ log.alertMsg }}
    </div>
  </form>
</template>

<script setup>
import { reactive } from 'vue'
import { useForm } from 'vee-validate'
import { toTypedSchema } from '@vee-validate/yup'
import * as yup from 'yup'
import { useUserStore } from '@/stores/user'
const userStore = useUserStore()

// login schema
const loginSchema = toTypedSchema(
  yup.object({
    email: yup.string().required().email(),
    password: yup.string().required().min(6)
  })
)
const {
  errors: loginErrors,
  handleSubmit: loginHandleSubmit,
  defineField: loginDefineField
} = useForm({
  validationSchema: loginSchema
})
const [email, emailAttrs] = loginDefineField('email')
const [password, passwordAttrs] = loginDefineField('password')

const log = reactive({
  inSubmission: false,
  showAlert: false,
  alertVariant: 'bg-red-500',
  alertMsg: 'Please wait. Your account is being created.'
})
const loginSubmit = loginHandleSubmit(async (values) => {
  log.inSubmission = true
  log.showAlert = false
  try {
    await userStore.login(values)
    location.reload()
  } catch (error) {
    log.inSubmission = false
    log.showAlert = true
    log.alertMsg = error.response.data.detail[0].msg
  }
})
</script>
