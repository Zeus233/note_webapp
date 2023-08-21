<template>
  <div id="app">
    <nav>
      <router-link to="/register">注册</router-link>
      <router-link to="/login">登录</router-link>
      <router-link to="/notes">便签</router-link>
    </nav>
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'App'
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

nav {
  display: flex;
  justify-content: space-around;
  background-color: #f3f3f3;
  padding: 1rem 0;
}

router-link {
  text-decoration: none;
  color: #2c3e50;
}
</style>
