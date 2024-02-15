import { createRouter, createWebHistory } from 'vue-router'
import { useUserStore } from '@/stores/user'
const Home = () => import('@/pages/Home.vue')
const About = () => import('@/pages/About.vue')
const Manage = () => import('@/pages/Manage.vue')
const Song = () => import('@/pages/Song.vue')

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/about',
      name: 'about',
      component: About
    },
    {
      path: '/manage',
      name: 'manage',
      alias: '/music-manage',
      component: Manage,
      meta: { requiresAuth: true }
    },
    {
      path: '/song/:songId',
      name: 'song',
      component: Song
    },
    {
      path: '/:notFound(.*)',
      redirect: { name: 'home' }
    }
  ],
  linkExactActiveClass: 'text-yellow-500'
})

router.beforeEach((to, from, next) => {
  const userStore = useUserStore()
  if (to.meta.requiresAuth && !userStore.userLoggedIn) {
    next({ name: 'home' })
  } else {
    next()
  }
})

export default router
