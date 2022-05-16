<template>
  <nav>
    <router-link to="/" name="HomePage">Home</router-link>
    <router-link to="/weightsheet">Monthly Weight Sheet</router-link>
    <router-link to="/weighin">Log Today's Weight</router-link>
  </nav>
</template>

<script>
export default {
  name: "NavBar",
};
</script>

<style>
.router-link-exact-active {
  color: #fff;
}

nav {
  background: #b98542;
  padding: 1em;
  width: 90vw;
}

nav a {
  margin: 1em;
  color: #0d1217;
  text-decoration: none;
  font-weight: 800;
}
</style>
