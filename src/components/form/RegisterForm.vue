<template>
  <form>
    <!-- Name -->
    <div class="mb-3">
      <label class="inline-block mb-2">{{ $t('auth.register.name') }}</label>
      <input
        type="text"
        class="block w-full py-1.5 px-3 text-gray-800 border border-gray-300 transition duration-500 focus:outline-none focus:border-black rounded"
        placeholder="Enter Name"
        v-model="name"
        v-bind="nameAttrs"
      />
      <p class="text-red-600">{{ registerErrors.name }}</p>
    </div>
    <!-- Email -->
    <div class="mb-3">
      <label class="inline-block mb-2">{{ $t('auth.register.email') }}</label>
      <input
        type="email"
        class="block w-full py-1.5 px-3 text-gray-800 border border-gray-300 transition duration-500 focus:outline-none focus:border-black rounded"
        placeholder="Enter Email"
        v-model="registerEmail"
        v-bind="registerEmailAttrs"
      />
      <p class="text-red-600">{{ registerErrors.email }}</p>
    </div>
    <!-- Age -->
    <div class="mb-3">
      <label class="inline-block mb-2">{{ $t('auth.register.age') }}</label>
      <input
        type="number"
        class="block w-full py-1.5 px-3 text-gray-800 border border-gray-300 transition duration-500 focus:outline-none focus:border-black rounded"
        v-model="age"
        v-bind="ageAttrs"
      />
      <p class="text-red-600">{{ registerErrors.age }}</p>
    </div>
    <!-- Password -->
    <div class="mb-3">
      <label class="inline-block mb-2">{{ $t('auth.register.password') }}</label>
      <input
        type="password"
        class="block w-full py-1.5 px-3 text-gray-800 border border-gray-300 transition duration-500 focus:outline-none focus:border-black rounded"
        placeholder="Password"
        v-model="registerPassword"
        v-bind="registerPasswordAttrs"
      />
      <p class="text-red-600">{{ registerErrors.password }}</p>
    </div>
    <!-- Confirm Password -->
    <div class="mb-3">
      <label class="inline-block mb-2">{{ $t('auth.register.confirmPassword') }}</label>
      <input
        type="password"
        class="block w-full py-1.5 px-3 text-gray-800 border border-gray-300 transition duration-500 focus:outline-none focus:border-black rounded"
        placeholder="Confirm Password"
        v-model="confirmPassword"
        v-bind="confirmPasswordAttrs"
      />
      <p class="text-red-600">{{ registerErrors.confirmPassword }}</p>
    </div>
    <!-- Country -->
    <div class="mb-3">
      <label class="inline-block mb-2">{{ $t('auth.register.country') }}</label>
      <select
        class="block w-full py-1.5 px-3 text-gray-800 border border-gray-300 transition duration-500 focus:outline-none focus:border-black rounded"
        v-model="country"
        v-bind="countryAttrs"
      >
        <option value="USA">USA</option>
        <option value="Mexico">Mexico</option>
        <option value="Germany">Germany</option>
      </select>
      <p class="text-red-600">{{ registerErrors.country }}</p>
    </div>
    <!-- TOS -->
    <div class="mb-3 pl-6">
      <input
        type="checkbox"
        class="w-4 h-4 float-left -ml-6 mt-1 rounded"
        id="tos"
        v-model="tos"
        v-bind="tosAttrs"
      />
      <i18n-t class="inline-block" keypath="auth.register.accept" tag="label" for="tos">
        <a href="#" class="text-blue-600">{{ $t('auth.register.tos') }}</a>
      </i18n-t>
      <!-- <label class="inline-block" for="tos">Accept terms of service</label> -->
      <p class="text-red-600 block">{{ registerErrors.tos }}</p>
    </div>
    <button
      class="block w-full bg-purple-600 text-white py-1.5 px-3 rounded transition hover:bg-purple-700 disabled:bg-gray-500"
      @click.prevent="registerSubmit"
      :disabled="reg.inSubmission"
    >
      Submit
    </button>
    <div
      class="text-white text-center font-bold p-4 my-4 rounded"
      v-if="reg.showAlert"
      :class="reg.alertVariant"
    >
      {{ reg.alertMsg }}
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

// register schema
const registerSchema = toTypedSchema(
  yup.object({
    name: yup.string().required(),
    email: yup.string().required().email(),
    age: yup.number().required().integer().min(18),
    password: yup.string().required().min(6),
    confirmPassword: yup
      .string()
      .required()
      .min(6)
      .oneOf([yup.ref('password')], 'Passwords must match'),
    country: yup.string().required(),
    tos: yup
      .boolean()
      .required('You must accept the Terms of Service.')
      .isTrue('You must accept the Terms of Service.')
  })
)
const {
  errors: registerErrors,
  handleSubmit: registerHandleSubmit,
  defineField: registerDefineField
} = useForm({
  validationSchema: registerSchema,
  initialValues: {
    country: 'USA'
  }
})
const [name, nameAttrs] = registerDefineField('name')
const [registerEmail, registerEmailAttrs] = registerDefineField('email')
const [age, ageAttrs] = registerDefineField('age')
const [registerPassword, registerPasswordAttrs] = registerDefineField('password')
const [confirmPassword, confirmPasswordAttrs] = registerDefineField('confirmPassword')
const [country, countryAttrs] = registerDefineField('country')
const [tos, tosAttrs] = registerDefineField('tos')

const reg = reactive({
  inSubmission: false,
  showAlert: false,
  alertVariant: 'bg-green-500',
  alertMsg: 'Please wait. Your account is being created.'
})
const registerSubmit = registerHandleSubmit(async (values) => {
  reg.inSubmission = true
  reg.showAlert = false
  try {
    await userStore.register(values)
    reg.showAlert = true
    reg.alertVariant = 'bg-green-500'
    reg.alertMsg = 'Success! User creted.'
  } catch (error) {
    reg.inSubmission = false
    reg.showAlert = true
    reg.alertVariant = 'bg-red-500'
    reg.alertMsg = error.response.data.detail[0].msg
  }
})
</script>
