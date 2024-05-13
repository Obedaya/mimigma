import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap.js';
import './assets/main.css';
import { createApp } from 'vue';
import { createPinia } from 'pinia';
import router from './router';
import App from './App.vue';
import axios from 'axios';
// import App from './views/MainView.vue';

axios.defaults.withCredentials = true;
axios.defaults.baseURL = "http://localhost:9000"

const app = createApp(App);

// Pinia initialisieren
const pinia = createPinia();
app.use(pinia);

// Router verwenden
app.use(router);

// Die App an das HTML-Element mit der ID "app" anhängen
app.mount('#app');
