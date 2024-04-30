import { createRouter, createWebHistory } from 'vue-router';
import Login from '../views/Login.vue';
import MainView from '../views/MainView.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: Login
    },
    {
      path: '/main',
      name: 'main',
      component: MainView,
      children: [
        { path: 'keyboard', component: () => import('../components/Keyboard.vue') },
        { path: 'plugboard', component: () => import('../components/Plugboard.vue') },
        { path: 'rotorpanel', component: () => import('../components/Rotorpanel.vue') }
      ]
    }
  ]
});

export default router;
