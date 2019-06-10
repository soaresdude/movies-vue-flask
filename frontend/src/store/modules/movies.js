import moviesApi from '../../services/moviesApi'

const state = {
  allMovies: null,
  loading: false,
  imdbInfo: null,
  error: null,
  selectedMovie: null
}

const mutations = {
  GET_ALL_MOVIES_SUCCESS (state, { result }) {
    state.allMovies = result.movies[0]
    state.loading = false
  },
  GET_ALL_MOVIES_FAILED (state, { error }) {
    state.error = error
    state.loading = false
  },
  GET_ALL_MOVIES_PENDING (state) {
    state.loading = true
  },

  GET_IMDB_INFO_SUCCESS (state, { result }) {
    state.imdbInfo = result
    state.loading = false
  },
  GET_IMDB_INFO_FAILED (state, { error }) {
    state.error = error
    state.loading = false
  },
  GET_IMDB_INFO_PENDING (state) {
    state.loading = true
  },

  GET_MOVIE_SUCCESS (state, { result }) {
    state.selectedMovie = result.movie[0]
    state.loading = false
  },
  GET_MOVIE_FAILED (state, { error }) {
    state.error = error
    state.loading = false
  },
  GET_MOVIE_PENDING (state) {
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
  },
  getMovieById ({ commit }, id) {
    commit('GET_MOVIE_PENDING')
    moviesApi.fetchMovieDetails(id)
      .then(result => {
        const { error } = result
        if (error) commit('GET_MOVIE_FAILED', { error })
        else commit('GET_MOVIE_SUCCESS', { result })
      })
      .catch(error => {
        commit('GET_MOVIE_FAILED', { error })
      })
  },
  getImdbInfo ({ commit }, params) {
    commit('GET_IMDB_INFO_PENDING')
    moviesApi.fetchImdbInfo(params)
      .then(result => {
        const { Error } = result
        if (Error) commit('GET_IMDB_INFO_FAILED', { Error })
        else commit('GET_IMDB_INFO_SUCCESS', { result })
      })
      .catch(error => {
        commit('GET_IMDB_INFO_FAILED', { error })
      })
  }
}

export default {
  state,
  mutations,
  actions
}
