import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/pages/Home'
import Result from '@/pages/Result'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/test/',
      name: 'Result',
      component: Result
    }
  ]
})
