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

  <v-container v-else>
    <v-layout wrap>
      <v-flex xs12 mr-1 ml-1>
        <v-card>
          <v-img v-if="imdbInfo"
                 :src="imdbInfo.Poster"
                 aspect-ratio="2"
          ></v-img>
          <v-card-title primary-title>
            <div>
              <a :href="selectedMovie.movie_imdb_link" target="_blank" class="headline mb-0">
                <h2>{{selectedMovie.movie_title}}-{{selectedMovie.title_year}}</h2>
              </a>
              <h3>Director name:</h3> {{selectedMovie.director_name}}
              <h3>Actors: </h3>
              <p>
                <span v-if="selectedMovie.actor_1_name">{{selectedMovie.actor_1_name}}</span>
                <span v-if="selectedMovie.actor_2_name">, {{selectedMovie.actor_2_name}}</span>
                <span v-if="selectedMovie.actor_3_name">, {{selectedMovie.actor_3_name}}</span>
              </p>
              <h4 v-if="imdbInfo">Awards:</h4>
              <p v-if="imdbInfo">{{imdbInfo.Awards}}</p>
              <h4>Genres:</h4>
              <p>{{selectedMovie.genres.split('|').join(', ')}}</p>
              <h4 v-if="imdbInfo">Plot:</h4>
              <p v-if="imdbInfo">{{imdbInfo.Plot}}</p>
            </div>
          </v-card-title>
          <v-card-actions>
            <v-btn flat color="green" @click="back">back</v-btn>
            <v-flex xs12>
              <div class="text-xs-right">
                <v-dialog
                  v-model="dialog"
                  width="500">
                  <v-btn
                    slot="activator"
                    color="green"
                    dark>
                    View Ratings
                  </v-btn>
                  <v-card v-if="imdbInfo">
                    <v-card-title
                      class="headline grey lighten-2"
                      primary-title>
                      Ratings
                    </v-card-title>
                    <v-card-text>
                      <table style="width:100%" border="1">
                        <tr>
                          <th>Source</th>
                          <th>Ratings</th>
                        </tr>
                        <tr v-for="(rating, index) in imdbInfo.Ratings" :key="index">
                          <td align="center">{{rating.Source}}</td>
                          <td align="center">
                            <v-rating :half-increments="true" :value="rating.Value | filterRating"></v-rating>
                          </td>
                          {{rating.Value | filterRating}}
                        </tr>
                      </table>
                    </v-card-text>
                    <v-divider></v-divider>
                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn
                        color="primary"
                        flat
                        @click="dialog = false">
                        OK
                      </v-btn>
                    </v-card-actions>
                  </v-card>
                </v-dialog>
              </div>
            </v-flex>
          </v-card-actions>

        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  name: 'SelectedMovie',
  data () {
    return {
      dialog: false
    }
  },
  computed: {
    loading () {
      return this.$store.state.movies.loading
    },
    imdbInfo () {
      return this.$store.state.movies.imdbInfo
    },
    selectedMovie () {
      return this.$store.state.movies.selectedMovie
    }
  },
  methods: {
    back () {
      this.$router.push('/')
    }
  },
  filters: {
    filterRating (value) {
      return parseFloat(value.split(/\/|%/)[0].replace('.', '')) / 20
    }
  }
}
</script>

<style lang="stylus" scoped>
  .v-progress-circular
    margin: 1rem
</style>
