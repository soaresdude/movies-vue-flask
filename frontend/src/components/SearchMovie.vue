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

  <v-container v-else-if="noData">
    <div class="text-xs-center">
      <h2>No Movie in API with {{this.name}}</h2>
    </div>
  </v-container>

  <v-container v-else grid-list-xl>
    <v-layout wrap>
      <v-flex xs4
              v-for="(item, index) in movieResponse"
              :key="index"
              mb-2>
        <v-card>
          <v-img
            :src="item.Poster"
            aspect-ratio="1"
          ></v-img>

          <v-card-title primary-title>
            <div>
              <h2>{{item.Title}}</h2>
              <div>Year: {{item.Year}}</div>
              <div>Type: {{item.Type}}</div>
              <div>IMDB-id: {{item.imdbID}}</div>
            </div>
          </v-card-title>

          <v-card-actions class="justify-center">
            <v-btn flat
                   color="green"
                   @click="selectedMovie(item.imdbID)"
            >View</v-btn>
          </v-card-actions>

        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  name: 'SearchMovie',
  created () {
    this.$store.dispatch('getAllMovies')
  },
  methods: {
    selectedMovie (id) {
      this.$router.push('/movie/' + id)
    }
  }
}
</script>

<style lang="stylus" scoped>
  .v-progress-circular
    margin: 1rem
</style>
