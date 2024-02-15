<template>
  <div class="fixed z-10 inset-0 overflow-y-auto" id="modal" :class="hiddenClass">
    <div
      class="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0"
    >
      <div class="fixed inset-0 transition-opacity">
        <div class="absolute inset-0 bg-gray-800 opacity-75"></div>
      </div>

      <!-- This element is to trick the browser into centering the modal contents. -->
      <span class="hidden sm:inline-block sm:align-middle sm:h-screen">&#8203;</span>

      <div
        class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full"
      >
        <!-- Add margin if you want to see some of the overlay behind the modal-->
        <div class="py-4 text-left px-6">
          <!--Title-->
          <div class="flex justify-between items-center pb-4">
            <p class="text-2xl font-bold">{{ $t('auth.title') }}</p>
            <!-- Modal Close Button -->
            <div class="modal-close cursor-pointer z-50" @click="changeOpen">
              <i class="fas fa-times"></i>
            </div>
          </div>

          <!-- Tabs -->
          <ul class="flex flex-wrap mb-4">
            <li class="flex-auto text-center">
              <a
                class="block rounded py-3 px-4 transition"
                href="#"
                @click.prevent="switchLoginMode"
                :class="{
                  'hover:text-white text-white bg-blue-600': loginMode,
                  'hover:text-blue-600': !loginMode
                }"
                >{{ $t('auth.login.title') }}</a
              >
            </li>
            <li class="flex-auto text-center">
              <a
                class="block rounded py-3 px-4 transition"
                href="#"
                @click.prevent="switchLoginMode"
                :class="{
                  'hover:text-white text-white bg-blue-600': !loginMode,
                  'hover:text-blue-600': loginMode
                }"
                >{{ $t('auth.register.title') }}</a
              >
            </li>
          </ul>

          <!-- Login Form -->
          <login-form v-if="loginMode"></login-form>
          <!-- Registration Form -->
          <register-form v-else></register-form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import LoginForm from '@/components/form/LoginForm.vue'
import RegisterForm from '@/components/form/RegisterForm.vue'
import { useModalStore } from '@/stores/modal'
import { storeToRefs } from 'pinia'

const modalStore = useModalStore()
const { hiddenClass } = storeToRefs(modalStore)
const { changeOpen } = modalStore

const { loginMode } = storeToRefs(modalStore)
const { switchLoginMode } = modalStore
</script>
