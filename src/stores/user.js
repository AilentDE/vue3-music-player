import { ref } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useUserStore = defineStore('user', () => {
  const router = useRouter()
  const userLoggedIn = ref(false)
  const setLoggedIn = () => {
    userLoggedIn.value = true
  }

  let url = 'http://localhost:8000/auth'
  const register = async (values) => {
    const formData = new FormData()
    formData.append('username', values.email)
    formData.append('password', values.password)
    await axios.post(url + '/register', formData).then((response) => {
      // localStorage
      localStorage.setItem('token', response.data.accessToken)
      localStorage.setItem('tokenExpiration', response.data.tokenExpiration)
      userLoggedIn.value = true
    })
    await axios
      .post(url + '/createUser', values, {
        headers: { Authorization: `Bearer ${localStorage.token}` }
      })
      .then((response) => {
        console.log(response)
      })
  }
  const login = async (values) => {
    const formData = new FormData()
    formData.append('username', values.email)
    formData.append('password', values.password)
    await axios.post(url + '/login', formData).then((response) => {
      // localStorage
      localStorage.setItem('token', response.data.accessToken)
      localStorage.setItem('tokenExpiration', response.data.tokenExpiration)
      userLoggedIn.value = true
    })
  }
  const signOut = () => {
    localStorage.removeItem('token')
    localStorage.removeItem('tokenExpiration')
    userLoggedIn.value = false

    router.replace({ name: 'home' })
  }

  return {
    userLoggedIn,
    register,
    setLoggedIn,
    login,
    signOut
  }
})
