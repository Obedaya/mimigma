import { defineStore } from 'pinia';
import axios from 'axios';

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
      // set the default Authorization header for axios
      axios.defaults.headers.common['Authorization'] = `Bearer ${this.token}`;
      console.log('User logged in:', this.user);
    },
    logout() {
      this.user = null;
      this.token = null;
      localStorage.removeItem('authToken');
      localStorage.removeItem('user');
      // remove the default Authorization header for axios
      delete axios.defaults.headers.common['Authorization'];
      console.log('User logged out');
    },
    checkAuth() {
      console.log('Checking authentication status...');
      const token = localStorage.getItem('authToken');
      const user = localStorage.getItem('user');
      if (token && user) {
        try {
          this.token = token;
          this.user = JSON.parse(user);
          // set the default Authorization header for axios
          axios.defaults.headers.common['Authorization'] = `Bearer ${this.token}`;
          console.log('User authenticated from local storage:', this.user);
        } catch (error) {
          console.error('Error parsing stored user data:', error);
          this.token = null;
          this.user = null;
          localStorage.removeItem('authToken');
          localStorage.removeItem('user');
        }
      } else {
        this.token = null;
        this.user = null;
        console.log('No authentication data found in local storage');
      }
    }
  },
  getters: {
    currentUserID() {
      return this.user ? this.user.id : null;
    }
  }
});
