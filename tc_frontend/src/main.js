import { createApp } from "vue";
import App from "./App.vue";
import { createAuth0 } from "@auth0/auth0-vue";

const app = createApp(App);

app.use(
  createAuth0({
    domain: process.env.AUTH0_DOMAIN,
    client_id: process.env.AUTH0_CLIENT_ID,
    redirect_uri: "http://127.0.0.1:8000/callback",
  })
);

app.mount("#app");
