import Vue from 'vue'
import Router from 'vue-router'
import Index from '../views/index'
import ind from '../views/index/index'
import summary from '../views/summary/index'
Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: Index
    },
    {
      path: '/ind',
      name: 'index',
      component: ind
    },
    {
      path: '/summary',
      name: 'companysummary',
      component: summary
    }
  ]
})
