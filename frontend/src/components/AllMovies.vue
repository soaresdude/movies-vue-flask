<template>

  <v-container v-if="loading">
    <div class="text-xs-center">
      <v-progress-circular
        indeterminate
        :size="150"
        :width="8"
        color="green">
      </v-progress-circular>
    </div>
  </v-container>

  <v-container v-else grid-list-xl>

    <div class="text-xs-center">
      <v-pagination
        v-model="page"
        :length="101"
        @input="changePage(page)"/>
    </div>

    <v-layout wrap>
      <v-flex xs4
              v-for="movie in allMovies"
              :key="movie.id"
              mb-2>
        <v-card>
          <v-card-title primary-title>
            <div>
              <h2>{{movie.movie_title}}</h2>
              <div>Title: {{movie.imdbID}}</div>
              <div>Year: {{movie.title_year}}</div>
              <div>Type: {{movie.genres.split('|').join(', ')}}</div>
            </div>
          </v-card-title>

          <v-card-actions class="justify-center">
            <v-btn flat
                   color="green"
                   @click="movieDetails = true"
            >View
            </v-btn>
            <v-dialog v-model="movieDetails" max-width="600px">
              <selected-movie :selected-movie="movie" @close="movieDetails = false"/>
            </v-dialog>
          </v-card-actions>

        </v-card>
      </v-flex>
    </v-layout>
    <div class="text-xs-center">
      <v-pagination
        v-model="page"
        :length="101"
        @input="changePage(page)"/>
    </div>
  </v-container>

</template>

<script>
import SelectedMovie from './SelectedMovie'

export default {
  name: 'AllMovies',
  data () {
    return {
      page: 1,
      movieDetails: false
    }
  },
  components: {
    SelectedMovie
  },
  created () {
    if (!this.allMovies) this.$store.dispatch('getAllMovies', { page: this.page })
  },
  computed: {
    loading () {
      return this.$store.state.movies.loading
    },
    allMovies () {
      return this.$store.state.movies.allMovies
    }
  },
  methods: {
    changePage (page) {
      this.$store.dispatch('getAllMovies', { page })
    }
  }
}
</script>

<style lang="stylus" scoped>
  .v-progress-circular
    margin: 1rem
</style>
