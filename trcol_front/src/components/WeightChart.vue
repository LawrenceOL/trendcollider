<template>
  <div class="weight_chart">
    <h1>Weight Chart</h1>
    <div v-for="(item, index) in weightList" :key="index">
      <h2>{{ item }}</h2>
    </div>
  </div>
</template>

<script>
export default {
  name: "WeightChart",
  props: ["weightList"],
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
