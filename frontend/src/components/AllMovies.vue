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
      <v-pagination v-if="allMovies.length > 20"
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
              <div>Year: {{movie.title_year}}</div>
              <div>Type: {{movie.genres.split('|').join(', ')}}</div>
            </div>
          </v-card-title>

          <v-card-actions class="justify-center">
            <v-btn flat
                   color="green"
                   @click="loadImdbInfo(movie)">
              View</v-btn>
          </v-card-actions>

        </v-card>
      </v-flex>
    </v-layout>
    <div class="text-xs-center">
      <v-pagination v-if="allMovies.length > 20"
        v-model="page"
        :length="101"
        @input="changePage(page)"/>
    </div>
  </v-container>

</template>

<script>

export default {
  name: 'AllMovies',
  data () {
    return {
      page: 1
    }
  },
  created () {
    if (!this.allMovies) this.$store.dispatch('getAllMovies', { page: this.page })
    if (this.pageNumber) this.page = this.pageNumber
  },
  computed: {
    loading () {
      return this.$store.state.movies.loading
    },
    allMovies () {
      return this.$store.state.movies.allMovies
    },
    imdbInfo () {
      return this.$store.state.movies.imdbInfo
    },
    pageNumber () {
      return this.$store.state.page
    }
  },
  methods: {
    changePage (page) {
      this.$store.dispatch('getAllMovies', { page })
      this.$store.dispatch('storePageNumber', page)
    },
    loadImdbInfo (movie) {
      Promise.all([this.$store.dispatch('getMovieById', movie.id),
        this.$store.dispatch('getImdbInfo', { title: movie.movie_title, year: movie.title_year })])
        .then(() => {
          this.$router.push('/movie')
        })
    }
  }
}
</script>

<style lang="stylus" scoped>
  .v-progress-circular
    margin: 1rem
</style>
