<template>
  <v-card>
    <v-container>
      <v-layout wrap>
        <v-flex xs12 mr-1 ml-1>
          <v-card>
            <v-card-title primary-title>
              <div>
                <h2 class="headline mb-0">{{selectedMovie.movie_title}}-{{selectedMovie.Year}}</h2>
                <p>{{ selectedMovie.Plot}} </p>
                <h3>Actors:</h3>{{selectedMovie.Actors}}
                <h4>Awards:</h4> {{selectedMovie.Awards}}
                <p>Genre: {{selectedMovie.Genre}}</p>
              </div>
            </v-card-title>
            <v-card-actions>
              <v-btn flat color="green" @click="back">back</v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>

      <v-layout row wrap>
        <v-flex xs12>
          <div class="text-xs-center">
            <v-dialog
              v-model="dialog"
              width="500">
              <v-btn
                slot="activator"
                color="green"
                dark>
                View Ratings
              </v-btn>
              <v-card>
                <v-card-title
                  class="headline grey lighten-2"
                  primary-title
                >
                  Ratings
                </v-card-title>
                <v-card-text>
                  <table style="width:100%" border="1" >
                    <tr>
                      <th>Source</th>
                      <th>Ratings</th>
                    </tr>
                    <tr v-for="(rating,index) in selectedMovie.ratings" :key="index">
                      <td align="center">{{selectedMovie.ratings[index].Source}}</td>
                      <td align="center">{{selectedMovie.ratings[index].Value}}</td>
                    </tr>
                  </table>
                </v-card-text>
                <v-divider></v-divider>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn
                    color="primary"
                    flat
                    @click="dialog = false"
                  >
                    OK
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </div>
        </v-flex>
      </v-layout>
    </v-container>
  </v-card>
</template>

<script>
export default {
  name: 'Movie',
  props: {
    selectedMovie: Object
  },
  created () {
    // this.$store.dispatch('getMovie', this.id)
  },
  methods: {
    back () {
      this.$router.push('/')
    }
  }
}
</script>

<style lang="stylus" scoped>
  .v-progress-circular
    margin: 1rem
</style>
