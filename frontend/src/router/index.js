import { createRouter, createWebHistory } from 'vue-router';
import { useAuthStore } from '@/stores/auth';
import Login from '@/views/Login.vue';
import MainView from '@/views/MainView.vue';

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
      meta: { requiresAuth: true },
      component: MainView
      /*children: [
        { path: 'keyboard', component: () => import('../components/Keyboard.vue') },
        { path: 'plugboard', component: () => import('../components/Plugboard.vue') },
        { path: 'rotorpanel', component: () => import('../components/Rotorpanel.vue') }
      ]*/
    }
  ]
});

router.beforeEach((to, from, next) => {
  const auth = useAuthStore();
  
  if (to.matched.some(record => record.meta.requiresAuth) && !auth.user) {
    if (to.path !== '/') {
      next('/');
    } else {
      next();
    }
  } else {
    next();
  }
});

export default router;
