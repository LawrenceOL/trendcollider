import { createApp } from "vue";
import App from "./App.vue";
// import { createAuth0 } from "@auth0/auth0-vue";
import router from "./router";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";

createApp(App).use(router).mount("#app");

// app.use(
//   // createAuth0({
//   //   domain: "dev-oe854-ql.us.auth0.com",
//   //   client_id: "hkTJGbONLK5hdsI6sfdO5GWe5kl8FZ55",
//   //   redirect_uri: "http://127.0.0.1:8080",
//   // }
//   router
// );

// app.mount("#app");
