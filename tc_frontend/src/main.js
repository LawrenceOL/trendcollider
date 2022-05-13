import { createApp } from "vue";
import App from "./App.vue";
import { createAuth0 } from "@auth0/auth0-vue";

const app = createApp(App);

app.use(
  createAuth0({
    domain: "dev-oe854-ql.us.auth0.com",
    client_id: "z5cSnSTKaiEIb99ov1GXB8AEREQAJ2No",
    redirect_uri: "http://127.0.0.1:8000/callback",
  })
);

app.mount("#app");
