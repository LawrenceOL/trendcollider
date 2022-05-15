<template>
  <div>
    <h1>Trend Collider</h1>
    <h2>Collide your Trends</h2>
    <!--  <button @click="login">Log in</button> -->
    <HelloWorld />
  </div>
</template>
<script>
// import { useAuth0 } from "@auth0/auth0-vue";
// import axios from 'axios'
// import WeightChart from './components/WeightChart.vue'
// const API_KEY =  ''

export default {
  //   setup() {
  //     const { loginWithRedirect } = useAuth0();

  //     return {
  //       login: () => {
  //         loginWithRedirect();
  //       },
  //     };
  //   },

  name: "App",
  components: {
    HelloWorld,
  },
  data: () => ({}),
  mounted: function () {},
  methods: {
    // async getWeigh_Ins(coords) {
    //   const res = await axios.get(`path`);
    //   this.weigh_ins = res.data;
    // },
  },
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
</style>
