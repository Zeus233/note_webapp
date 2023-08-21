<template>
    <div class="notes-container">
      <h1>我的便签</h1>
      <form @submit.prevent="addNote">
        <input type="text" v-model="newNote" placeholder="添加新便签" required />
        <button type="submit">添加</button>
      </form>
      <ul>
        <li v-for="note in notes" :key="note.id">
          <span @click="editNote(note.id)">
            {{ note.username }}: {{ note.content }}
          </span>
          <button @click="deleteNote(note.id)">删除</button>
        </li>
      </ul>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  const newNote = ref('');
  const notes = ref([]);


  
  const fetchNotes = async () => {
    const token = localStorage.getItem('access_token'); // 获取保存在本地存储中的JWT令牌
    const headers = {
      'Authorization': `Bearer ${token}`, // 添加JWT令牌到请求头
      'Content-Type': 'application/json',
    };
    const response = await fetch('http://localhost:5000/notes', { headers });
    if (!response.ok) {
      // 处理错误
      console.error("获取便签失败");
      return;
    }

    const data = await response.json();
    notes.value = data.notes; // 使用 data.notes 而不是整个 data 对象
  };

  
  const addNote = async () => {
    const token = localStorage.getItem('access_token'); // 获取保存在本地存储中的JWT令牌
    const headers = {
      'Authorization': `Bearer ${token}`, // 添加JWT令牌到请求头
      'Content-Type': 'application/json',
    };
    await fetch('http://localhost:5000//notes', { 
      method: 'POST', 
      headers,
      body: JSON.stringify({ content: newNote.value }) 
    });
    newNote.value = '';
    await fetchNotes();
  };

  const editNote = (id) => {
    const token = localStorage.getItem('access_token'); // 获取保存在本地存储中的JWT令牌
    const headers = {
      'Authorization': `Bearer ${token}`, // 添加JWT令牌到请求头
      'Content-Type': 'application/json',
    };
    const noteContent = prompt('请输入新的便签内容', notes.value.find(n => n.id === id).content);
    fetch(`http://localhost:5000//notes/${id}`, { 
      method: 'PUT', 
      headers,
      body: JSON.stringify({ content: noteContent }) 
    }).then(() => fetchNotes());
  };


  
  const deleteNote = async (id) => {
    const token = localStorage.getItem('access_token'); // 获取保存在本地存储中的JWT令牌
    const headers = {
      'Authorization': `Bearer ${token}`, // 添加JWT令牌到请求头
      'Content-Type': 'application/json',
    };
    await fetch(`http://localhost:5000/notes/${id}`, { method: 'DELETE' ,headers});
    await fetchNotes();
  };


  
  fetchNotes();
  </script>
  
  <style scoped>
  .notes-container {
    width: 400px;
    margin: 0 auto;
  }
  
  form {
    margin-bottom: 20px;
  }
  
  li {
    margin: 10px 0;
    display: flex;
    justify-content: space-between;
  }
  
  button {
    cursor: pointer;
  }
  </style>
  