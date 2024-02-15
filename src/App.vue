<template>
  <!-- Header -->
  <Header :logInStatus="userLoggedIn" />

  <router-view v-slot="{ Component }">
    <transition name="route" mode="out-in">
      <component :is="Component"></component>
    </transition>
  </router-view>

  <!-- Player -->
  <app-player></app-player>

  <!-- Auth Modal -->
  <Auth />
</template>

<script setup>
import Header from './components/layout/Header.vue'
import AppPlayer from './components/Player.vue'
import Auth from './components/auth/Auth.vue'
import { useUserStore } from './stores/user'
import { storeToRefs } from 'pinia'
const userStore = useUserStore()
const { userLoggedIn } = storeToRefs(userStore)

const loggedInCheck = () => {
  const token = localStorage.getItem('token')
  const tokenExpiration = localStorage.getItem('tokenExpiration')
  if (token && tokenExpiration) {
    const tokenExpirationDate = new Date(tokenExpiration)
    const currentDate = new Date()
    if (tokenExpirationDate < currentDate) {
      localStorage.removeItem('token')
      localStorage.removeItem('tokenExpiration')
      location.reload()
    } else {
      userStore.setLoggedIn()
    }
  }
}
loggedInCheck()
setInterval(loggedInCheck, 1000 * 60 * 10)
</script>

<style>
.route-enter-from,
.route-leave-to {
  opacity: 0;
}
.route-enter-active,
.route-leave-active {
  transition: all 0.3s linear;
}
.route-ento-to,
.route-leave-from {
  opacity: 1;
  transition: all 0.3s linear;
}
</style>
