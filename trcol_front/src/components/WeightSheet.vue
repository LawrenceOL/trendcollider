<template>
  <div class="weight_chart">
    <h1>Weight Sheet</h1>

    <div v-for="(item, index) in weightList" :key="index">
      <table style="width: 100%" border="1px solid black" class="table">
        <tr>
          <th>Date</th>
          <th>Weight</th>
          <th>Edit</th>
        </tr>
        <tr>
          <td>{{ item.date }}</td>
          <td>{{ item.weight }}</td>
          <td>
            <button>
              <svg
                @click="counter++"
                v-on:click="alert('hi')"
                xmlns="http://www.w3.org/2000/svg"
                width="16"
                height="16"
                fill="currentColor"
                class="bi bi-pencil-square"
                viewBox="0 0 16 16"
              >
                <path
                  d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"
                />
                <path
                  fill-rule="evenodd"
                  d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"
                />
              </svg>
            </button>
          </td>
        </tr>
      </table>
    </div>
    <p>The button above has been clicked {{ counter }} times.</p>
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
    counter: 0,
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
