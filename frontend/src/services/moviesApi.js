import axios from 'axios'

export default {
  fetchAllMovies (params = null) {
    return axios.get('/movies', { params })
      .then(response => response.data)
      .catch(error => console.error('Error: ', error))
  },
  fetchMovieDetails (id) {
    return axios.get(`/movie/${id}`)
      .then(response => response.data)
      .catch(error => console.error('Error: ', error))
  }
}
