<template>
  <all-movies/>
</template>

<script>
import AllMovies from '../components/AllMovies'

export default {
  name: 'Dashboard',
  components: {
    AllMovies
  }
}
</script>

<style lang="stylus" scoped>
  .v-progress-circular
    margin: 1rem
</style>
