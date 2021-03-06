import { createWebHistory, createRouter } from "vue-router";
import HomePage from "./components/HomePage.vue";
import WeighIn from "./components/WeighIn.vue";
import WeightSheet from "./components/WeightSheet.vue";
import UpdateWeight from "./components/UpdateWeight.vue";
import StockPage from "./components/StockPage.vue";
// import WeightChart from './components/WeightChartPage.vue'
// import StockChart from './components/StockChartPage.vue'

const routes = [
  { path: "/", component: HomePage, name: "HomePage" },
  { path: "/weightsheet", component: WeightSheet, name: "WeightSheet" },
  { path: "/weighin", component: WeighIn, name: "WeighIn" },
  { path: "/update/:id/:date", component: UpdateWeight, name: "UpdateWeight" },
  { path: "/stockpage", component: StockPage, name: "StockPage" },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
