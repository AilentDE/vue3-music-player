import { ref, onBeforeUnmount } from 'vue'

export const formatTime = (time) => {
  if (time == 'Infinity') {
    return '00:00'
  }
  const minutes = Math.floor(time / 60) || 0
  const seconds = Math.round(time - minutes * 60 || 0)

  return `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`
}

export const handleScroll = async (
  callback,
  limit = ref(20),
  skip = ref(0),
  pendingRequest = ref(false)
) => {
  const runFunction = async () => {
    const { scrollTop, offsetHeight } = document.documentElement
    const { innerHeight } = window
    const bottomOfWindow = Math.round(scrollTop) + innerHeight === offsetHeight

    if (pendingRequest.value) {
      return
    } else if (bottomOfWindow) {
      pendingRequest.value = true
      console.log('load data!')
      skip.value += limit.value
      await callback(limit.value, skip.value)
      pendingRequest.value = false
    }
  }

  // created
  pendingRequest.value = true
  await callback(limit.value, skip.value)
  pendingRequest.value = false

  window.addEventListener('scroll', runFunction)
  // Issue: can't use Lifecycle Hooks outside of setup
  onBeforeUnmount(() => {
    window.removeEventListener('scroll', runFunction)
  })
}
