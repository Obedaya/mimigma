import { defineStore } from 'pinia';

export const useAuthStore = defineStore({
  id: 'auth',
  state: () => ({
    user: null,
    returnUrl: null
  }),
  actions: {
    login(user) {
      this.user = user;
    },
    logout() {
      this.user = null;
    }
  }
});
