<template>
  <div>
    <h1>Update Weight</h1>
    <h1>{{ params_date }}</h1>
    <form @submit.prevent="onSubmit" @submit="UpdateWeight()">
      <input v-model="newWeight" placeholder="Update Weight" />
      <button>Submit</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "UpdateWeight",

  components: {},
  data: () => ({
    newWeight: null,
    params_id: null,
    params_date: null,
  }),
  mounted: function () {
    this.params_id = this.$route.params.id;
    this.params_date = this.$route.params.date;
  },
  methods: {
    async UpdateWeight() {
      let payload = { weight: this.newWeight, date: this.params_date };

      await axios.put(
        `http://127.0.0.1:8000/weigh_in_detail/${this.params_id}`,
        payload
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
