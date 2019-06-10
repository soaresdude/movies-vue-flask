import axios from 'axios'

const omdbUrl = 'http://www.omdbapi.com/?apikey=3e43754c&plot=full'

export default {
  fetchAllMovies (params = null) {
    return axios.get('/movies', { params })
      .then(response => Promise.resolve(response.data))
      .catch(error => Promise.reject(error))
  },
  fetchMovieDetails (id) {
    return axios.get(`/movie/${id}`)
      .then(response => Promise.resolve(response.data))
      .catch(error => Promise.reject(error))
  },
  fetchImdbInfo (params) {
    return axios.get(omdbUrl, { params: { t: params.title, y: params.year } })
      .then(response => Promise.resolve(response.data))
      .catch(error => Promise.reject(error))
  }
}
