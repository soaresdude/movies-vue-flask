import Vue from 'vue'
import Router from 'vue-router'
import Dashboard from '../views/Dashboard'
import SelectedMovie from '../components/SelectedMovie'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Dashboard',
      component: Dashboard
    },
    {
      path: '/movie',
      name: 'SelectedMovie',
      component: SelectedMovie
    }
  ]
})
