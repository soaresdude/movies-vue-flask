import moviesApi from '../../services/moviesApi'

const state = {
  allMovies: null,
  loading: false
}

const mutations = {
  GET_ALL_MOVIES_SUCCESS (state, { result }) {
    state.allMovies = result.movies[0]
    state.loading = false
  },
  GET_ALL_MOVIES_FAILED (state, { error }) {
    state.allMovies = error
    state.loading = false
  },
  GET_ALL_MOVIES_PENDING (state) {
    state.loading = true
  }
}

const actions = {
  getAllMovies ({ commit }, page) {
    commit('GET_ALL_MOVIES_PENDING')
    moviesApi.fetchAllMovies(page)
      .then(result => {
        const { error } = result
        if (error) commit('GET_ALL_MOVIES_FAILED', { error })
        else commit('GET_ALL_MOVIES_SUCCESS', { result })
      })
      .catch(error => {
        commit('GET_ALL_MOVIES_FAILED', { error })
      })
  }
}

export default {
  state,
  mutations,
  actions
}
