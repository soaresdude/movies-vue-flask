<template>
  <v-app>
    <v-toolbar app>
      <v-toolbar-title class="headline text-uppercase">
        <router-link
          to='/'
          tag='span'
          style='cursor: pointer'>
          Vue Movies
        </router-link>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-flex xs12 sm6 md3>
        <v-autocomplete v-model="searchString"
          @update:searchInput="inspectString"
          :items="movieNames"
          color="green"
          label="Movie Name">
        </v-autocomplete>
      </v-flex>
      <v-btn
        flat
        :disabled="!dataAvailable"
        @click="searchMovie">
        <span class="mr-2">Search</span>
      </v-btn>
    </v-toolbar>

    <v-content>
      <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script>

export default {
  name: 'App',
  data () {
    return {
      searchString: '',
      searchLength: 0,
      hasSearched: false
    }
  },
  created () {
    this.$store.dispatch('getMoviesNames')
  },
  computed: {
    dataAvailable () {
      return this.searchString !== null && this.searchString !== ''
    },
    movieNames () {
      return this.$store.state.movies.movieNames
    }
  },
  methods: {
    searchMovie () {
      this.$store.dispatch('getAllMovies', { filter: { movie_title: this.searchString } })
      this.hasSearched = true
    },
    inspectString (value) {
      if (value === '' && this.hasSearched) {
        this.$store.dispatch('getAllMovies')
        this.hasSearched = false
      }
    }
  }
}
</script>
