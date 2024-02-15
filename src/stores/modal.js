import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useModalStore = defineStore('modal', () => {
  const isOpen = ref(false)
  const hiddenClass = computed(() => (!isOpen.value ? 'hidden' : ''))
  const changeOpen = () => {
    isOpen.value = !isOpen.value
  }

  const loginMode = ref(true)
  const switchLoginMode = () => {
    loginMode.value = !loginMode.value
  }

  return {
    isOpen,
    hiddenClass,
    changeOpen,
    loginMode,
    switchLoginMode
  }
})
