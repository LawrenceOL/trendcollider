<template>
  <div class="weight_chart">
    <h1>Weight Sheet</h1>
    <div v-for="(item, index) in weightList" :key="index">
      <table style="width: 100%" border="1px solid black" class="table">
        <tr>
          <th>Date</th>
          <th>Weight</th>
        </tr>
        <tr>
          <td>{{ item.date }}</td>
          <td>{{ item.weight }}</td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script>
// import { useAuth0 } from "@auth0/auth0-vue";
import axios from "axios";
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

  name: "HomePage",
  components: {
    // NavBar,
  },
  data: () => ({
    weightList: [],
  }),
  mounted: function () {
    this.getWeightList();
  },
  methods: {
    async getWeightList() {
      const res = await axios.get("http://127.0.0.1:8000/weigh_ins");

      this.weightList = res.data;
    },
    // async getWeigh_Ins(coords) {
    //   const res = await axios.get(`path`);
    //   this.weigh_ins = res.data;
    // },
  },
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
