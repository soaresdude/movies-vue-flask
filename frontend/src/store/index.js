import Vue from 'vue'
import Vuex from 'vuex'
import movies from './modules/movies'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    page: 1
  },
  mutations: {
    STORE_PAGE_NUMBER (state, { page }) {
      state.page = page
    }
  },
  actions: {
    storePageNumber ({ commit }, page) {
      commit('STORE_PAGE_NUMBER', { page })
    }
  },
  modules: {
    movies
  }
})
