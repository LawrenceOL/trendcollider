<template>
  <div>
    <!-- <NavBar /> -->

    <h1 id="trendcollider">Trend Collider</h1>
    <h2 font-style="italic">Collide your Trends</h2>
    <img
      src="../assets/tr.png"
      alt="image featuring someone's weight and someone's stock pick"
    />
    <div v-for="(item, index) in weightList" :key="index">
      <h2>{{ item }}</h2>
    </div>
  </div>
</template>
<script>
export default {};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  display: flex;
  flex-direction: column;
  align-items: center;
}
img {
  width: 90vw;
  margin-top: 50px;
}
#trendcollider {
  margin-top: 20px;
}
</style>
