<template>
  <div>
    <h1>Today's Weight</h1>
    <form @submit.prevent="onSubmit" @submit="addWeighIn()">
      <input v-model="newWeight" placeholder="Enter Today's Weight" />
      <button>Submit</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "HomePage",
  components: {},
  data: () => ({
    newWeight: null,
  }),
  mounted: function () {},
  methods: {
    async addWeighIn() {
      await axios.post(
        `http://127.0.0.1:8000/weigh_in_detail/${this.newWeight}`
      );
      this.newWeight = null;
      await this.$router.push("/WeightSheet");
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
