import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import i18n from './includes/i18n'
import progressBar from './includes/progressBar'

import './assets/base.css'
import './assets/main.css'
import 'nprogress/nprogress.css'

progressBar(router)

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(i18n)

app.mount('#app')
