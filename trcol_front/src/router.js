import { createWebHistory, createRouter } from "vue-router";
import HomePage from "./components/HomePage.vue";

import WeightSheet from "./components/WeightSheet.vue";
// import WeightChart from './components/WeightChartPage.vue'
// import StockChart from './components/StockChartPage.vue'

const routes = [
  { path: "/", component: HomePage, name: "HomePage" },
  // { path: "/app", component: App, name: "App" },
  { path: "/weightsheet", component: WeightSheet, name: "WeightSheet" },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;