<template>
  <div>
  <!-- Список всех постов всех пользователей-->
  </div>
</template>

<script>
    export default {
        name: "index",

        mounted() {
          axios
            .get('https://api.coindesk.com/v1/bpi/currentprice.json')
            .then(response => (this.info = response));
        }
    }
</script>

<style scoped>
</style>
