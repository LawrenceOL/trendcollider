<template>
  <div class="weight_chart">
    <h1>Weight Sheet</h1>
    <!-- <div v-for="(item, index) in weightList" :key="index">
      <h2>{{ item }}</h2>
      <WeightChart :weightList="weightList" />
    </div> -->
  </div>
</template>

<script>
// import WeightChart from "./WeightChart.vue";

export default {
  // name: "WeightChart",
  // props: ["weightList"],
  // components: { WeightChart },
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
