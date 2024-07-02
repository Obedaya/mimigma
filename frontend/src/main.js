import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap.js';
import './assets/main.css';
import { createApp } from 'vue';
import { createPinia } from 'pinia';
import router from './router';
import App from './App.vue';
import axios from 'axios';
import { useAuthStore } from '@/stores/auth';

const apiEndpoint = import.meta.env.VITE_API_ENDPOINT;

axios.defaults.withCredentials = true;
axios.defaults.baseURL = apiEndpoint;

const app = createApp(App);

// Pinia initialisieren
const pinia = createPinia();
app.use(pinia);

// Check authentication status on app load
const auth = useAuthStore();
auth.checkAuth();
console.log('Authentication check completed');

// Router verwenden
app.use(router);

// Die App an das HTML-Element mit der ID "app" anhängen
app.mount('#app');
