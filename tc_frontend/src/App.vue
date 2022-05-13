<template>
  <div>
    <button v-if="!isAuthenticated" @click="login">Log in</button>
    <button v-if="!isAuthenticated" @click="logout">Log out</button>
  </div>
</template>

<script>
import { useAuth0 } from "@auth0/auth0-vue";

export default {
  setup() {
    const auth0 = useAuth0();
    const { loginWithRedirect, logout } = useAuth0();

    return {
      login: () => {
        loginWithRedirect();
      },
      isAuthenticated: auth0.isAuthenticated,
      logout: () => {
        logout({ returnTo: window.location.origin });
      },
    };
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
