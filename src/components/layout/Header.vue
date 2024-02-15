<template>
  <header id="header" class="bg-gray-700">
    <nav class="container mx-auto flex justify-start items-center py-5 px-4">
      <!-- App Name -->
      <router-link
        class="text-white font-bold uppercase text-2xl mr-4"
        :to="{ name: 'home' }"
        exact-active-class=""
        >Music</router-link
      >

      <div class="flex flex-grow items-center justify-between">
        <!-- Primary Navigation -->
        <ul class="flex flex-row mt-1">
          <!-- Navigation Links -->
          <li>
            <router-link class="px-2 text-white" :to="{ name: 'about' }">{{
              $t('header.about')
            }}</router-link>
          </li>
          <li v-if="!logInStatus">
            <a class="px-2 text-white" href="#" @click.prevent="changeOpen">{{
              $t('header.login')
            }}</a>
          </li>
          <div v-else class="flex flex-row">
            <li>
              <router-link class="px-2 text-white" :to="{ name: 'manage' }">{{
                $t('header.manage')
              }}</router-link>
            </li>
            <li>
              <a class="px-2 text-white" href="#" @click.prevent="signOut">{{
                $t('header.logout')
              }}</a>
            </li>
          </div>
        </ul>
        <ul>
          <a href="#" class="px-2 text-white" @click.prevent="changeLocale">{{ currentLocale }}</a>
        </ul>
      </div>
    </nav>
  </header>
</template>

<script setup>
import { useModalStore } from '@/stores/modal'
import { useUserStore } from '@/stores/user'
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'

const props = defineProps({
  logInStatus: Boolean
})

const modalStore = useModalStore()
const { changeOpen } = modalStore
const userStore = useUserStore()
const { signOut } = userStore

const { locale } = useI18n()
const currentLocale = computed(() => {
  switch (locale.value) {
    case 'en':
      return 'English'
    case 'zh':
      return 'Chinese'
    default:
      return ''
  }
})
const changeLocale = () => {
  if (locale.value == 'en') {
    locale.value = 'zh'
  } else {
    locale.value = 'en'
  }
}
</script>
