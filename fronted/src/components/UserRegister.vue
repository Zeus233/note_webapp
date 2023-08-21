<template>
    <div class="register-container">
      <h1>注册</h1>
      <form @submit.prevent="register">
        <div>
          <label for="username">用户名:</label>
          <input type="text" id="username" v-model="username" required />
        </div>
        <div>
          <label for="password">密码:</label>
          <input type="password" id="password" v-model="password" required />
        </div>
        <button type="submit">注册</button>
      </form>
      <p v-if="error">{{ error }}</p>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import { useRouter } from 'vue-router';

  const username = ref('');
  const password = ref('');
  const error = ref(null);


  const router = useRouter();

  const register = async () => {
  try {
    const response = await fetch('http://localhost:5000//register', { // 注意这里的URL
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ username: username.value, password: password.value }),
    });

    const data = await response.json();

    if (data.success) {
      router.push('/login');
    } else {
      error.value = data.message;
    }
  } catch (err) {
    console.error('注册失败:', err);
    error.value = '注册失败，请稍后再试';
  }
};

  </script>
  
  <style scoped>
  .register-container {
    width: 300px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
  }
  
  label, input {
    display: block;
    margin-bottom: 10px;
  }
  
  button {
    cursor: pointer;
  }
  </style>
  