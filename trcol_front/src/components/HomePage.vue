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
    <!--  <button @click="login">Log in</button> -->
  </div>
</template>
<script>
// import { useAuth0 } from "@auth0/auth0-vue";
// import axios from "axios";
// import WeightChart from './components/WeightChart.vue'
// const API_KEY =  ''

// import NavBar from "./NavBar.vue";

export default {
  //   setup() {
  //     const { loginWithRedirect } = useAuth0();
  //     return {
  //       login: () => {
  //         loginWithRedirect();
  //       },
  //     };
  //   },
  //   name: "HomePage",
  //   components: {
  //     // NavBar,
  //   },
  //   data: () => ({
  //     weightList: [],
  //   }),
  //   mounted: function () {
  //     this.getWeightList();
  //   },
  //   methods: {
  //     async getWeightList() {
  //       const res = await axios.get("http://127.0.0.1:8000/weigh_ins");
  //       this.weightList = res.data;
  //     },
  //   },
};
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
