import { createRouter, createWebHistory } from 'vue-router';
import UserRegister from './components/UserRegister.vue'; // 更改组件名
import UserLogin from './components/UserLogin.vue'; // 更改组件名
import UserNotes from './components/UserNotes.vue'; // 更改组件名

const routes = [
  { path: '/register', component: UserRegister },
  { path: '/login', component: UserLogin },
  { path: '/notes', component: UserNotes },
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
