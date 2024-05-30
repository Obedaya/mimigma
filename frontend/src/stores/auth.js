import { defineStore } from 'pinia';

export const useAuthStore = defineStore({
  id: 'auth',
  state: () => ({
    user: null,
    token: null,
    returnUrl: null
  }),
  actions: {
    login(user) {
      this.user = { id: user.id, username: user.username };
      this.token = user.token;
      // save in local storage to make persistent
      localStorage.setItem('authToken', this.token);
      localStorage.setItem('user', JSON.stringify(this.user));
    },
    logout() {
      this.user = null;
      this.token = null;
      localStorage.removeItem('authToken');
      localStorage.removeItem('user');
    },
    checkAuth() {
      const token = localStorage.getItem('authToken');
      const user = localStorage.getItem('user');
      if (token && user) {
        this.token = token;
        this.user = JSON.parse(user);
      }
    }
  }
});
