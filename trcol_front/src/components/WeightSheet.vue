<template>
  <div class="weight_chart">
    <h1>Weight Sheet</h1>

    <div v-for="(item, index) in weightList" :key="index">
      <table style="width: 100%" border="1px solid black" class="table">
        <tr>
          <th>Date</th>
          <th>Weight</th>
          <!-- <th>ID</th> -->
          <th>Edit</th>
          <th>Delete</th>
        </tr>
        <tr>
          <td class="editable {{ item.id }} {{ item.date }}">
            {{ item.date }}
          </td>

          <td class="editable {{ item.id }} {{ item.date }}">
            {{ item.weight }}
          </td>

          <!-- editing mode -->

          <td class="editing">
            <button
              @click="this.handleClick"
              v-bind:id="item.id"
              v-bind:class="item.date"
              class="editing"
            >
              <svg
                v-bind:id="item.id"
                v-bind:class="item.date"
                xmlns="http://www.w3.org/2000/svg"
                width="16"
                height="16"
                fill="currentColor"
                class="editing"
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
          <td>
            <button
              @click="this.handleClick"
              v-bind:id="item.id"
              class="deleting"
            >
              ❌
            </button>
          </td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "WeightSheet",
  components: {},
  data: () => ({
    weightList: [],
    userId: null,
    editingId: null,
    newDate: "",
    newWeight: "",
    addWeight: "",
    addDate: "",
    editingDate: "",
  }),
  mounted: function () {
    this.getWeightList();
  },
  methods: {
    async addWeighIn(addWeight, addDate) {
      await axios.post(
        `http://127.0.0.1:8000/weigh_in_detail/${addWeight}/${addDate}`
      );
    },

    async getWeightList() {
      const res = await axios.get("http://localhost:8000/weigh_ins");
      this.weightList = res.data;
      this.userId = res.data[0].weigh_in_user;
    },
    navigateItem(id, date) {
      this.$router.push(`/update/${id}/${date}`);
    },

    handleClick(event, index) {
      console.log(`${event.target.id}`);
      this.editingDate = event.target.classList[0];
      this.navigateItem(event.target.id, this.editingDate);
      console.log(`${event.target.classList}`);

      if (event.target.classList == "deleting") {
        this.removeWeighIn(event, index);
      }
      if (event.target.classList == "editing") {
        this.editingId = event.target.id;
      }
    },
    async removeWeighIn(event, index) {
      let remove = confirm("Are you sure? This will delete the weigh-in data.");
      if (remove === true) {
        this.weightList.splice(index, 1);
        // console.log(event.target.id);
        await axios.delete(
          `http://127.0.0.1:8000/weigh_in_detail/${event.target.id}`
        );
      }
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
