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
    }
  ]
});

router.beforeEach((to, from, next) => {
  const auth = useAuthStore();
  auth.checkAuth();  // Check auth state on each route change
  if (to.matched.some(record => record.meta.requiresAuth) && !auth.user) {
    next('/');
  } else {
    next();
  }
});

export default router;
