<template>
  <div class="weight_chart">
    <h1>Stocks</h1>

    <div v-for="(stock, index) in stockList" :key="index">
      <ul>
        <b>{{ stock.symbol }}</b>
        :
        <u>{{ stock.description }}</u>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "WeightSheet",
  components: {},
  data: () => ({
    stockList: [],
  }),
  mounted: function () {
    this.getStockList();
  },
  methods: {
    async getStockList() {
      const res = await axios.get("http://localhost:8000/stock_list/");
      this.stockList = res.data;
    },
  },
};
</script>

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

h1 {
  font-weight: bold;
  margin: 35px 0 50px 0;
}
</style>
