<template>
    <div class="login-container">
      <h1>登录</h1>
      <form @submit.prevent="loginUser">
        <div>
          <label for="username">用户名:</label>
          <input type="text" id="username" v-model="username" required />
        </div>
        <div>
          <label for="password">密码:</label>
          <input type="password" id="password" v-model="password" required />
        </div>
        <button type="submit">登录</button>
      </form>
      <p v-if="errorMessage">{{ errorMessage }}</p>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import { useRouter } from 'vue-router';
  
  const username = ref('');
  const password = ref('');
  const errorMessage = ref('');

  
  // eslint-disable-next-line no-unused-vars
  const router = useRouter();
  
  const loginUser = async () => {
    try {
      const response = await fetch('http://localhost:5000//login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username: username.value, password: password.value }),
      });

      const data = await response.json();

      // 保存 JWT token 到 localStorage
      localStorage.setItem('access_token', data.access_token);

      // 重定向到便签管理页面
      router.push('/notes');
    } catch (error) {
      console.error('登录出错:', error);
      errorMessage.value = '登录失败，请重试。';
    }
  };


  </script>
  
  <style scoped>
  .login-container {
    width: 300px;
    margin: 0 auto;
  }
  
  div {
    margin: 10px 0;
  }
  
  label {
    width: 100px;
    display: inline-block;
  }
  
  button {
    cursor: pointer;
  }
  </style>
  