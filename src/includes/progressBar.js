import NProgress from 'nprogress'

export default (router) => {
  router.beforeEach((to, from, next) => {
    NProgress.start()
    next()
  })
  router.afterEach((to, from) => {
    NProgress.done()
  })
}
