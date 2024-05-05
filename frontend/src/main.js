import './assets/main.css';
import { createApp } from 'vue';
import { createPinia } from 'pinia';
import router from './router';
import App from './App.vue';
// import App from './views/MainView.vue';

const app = createApp(App);

// Pinia initialisieren
const pinia = createPinia();
app.use(pinia);

// Router verwenden
app.use(router);

// Die App an das HTML-Element mit der ID "app" anhängen
app.mount('#app');
