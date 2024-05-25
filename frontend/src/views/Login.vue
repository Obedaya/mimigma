<template>
  <div>
    <h1 class="website-title">Mimigma</h1>
    <div class="container-wrapper">
      <div :class="{ 'login-container': true, 'error-border': showErrorBorder }">
        <h2 :class="{ 'login-title': true, 'error-text': showErrorBorder }">Login</h2>
        <form @submit.prevent="login" class="login-form">
          <div class="form-group">
            <label for="username" class="form-label"></label>
            <input type="text" id="username" v-model="username" class="form-input" placeholder="Username" required>
          </div>
          <div class="form-group">
            <label for="passwort" class="form-label"></label>
            <input type="password" id="passwort" v-model="password" class="form-input" placeholder="Password" required>
          </div>
          <button type="submit" class="login-button">Go!</button>
        </form>
        <div v-if="showErrorBorder" class="try-again">Try again</div>
      </div>
    </div>
  </div>
</template>

<script>
import { useAuthStore } from '@/stores/auth';
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: '',
      showErrorBorder: false
    };
  },
  
  methods: {
    login() {
      axios.post(`/login?username=${this.username}&password=${this.password}`)
        .then(response => {
          console.log('Response:', response.data);
          if (response.status === 200) {
            const auth = useAuthStore();
            const userData = response.data.user;
            auth.login(userData);
            this.$router.push('/main');
          } else {
            console.log('Login failed: Invalid status code');
            this.showErrorBorder = true;
          }
        })
        .catch(error => {
          if (error.response && error.response.status === 401) {
            console.log('Login failed: Unauthorized');
            this.showErrorBorder = true;
          } else {
            console.error('Error while fetching data: ', error);
          }
        });
    }
  }
};
</script>

<style>
body {
  background-color: #2a2a2a !important;
}

.website-title {
  font-size: 100px;
  text-align: center;
  color: #00fddc;
  margin-bottom: 120px;
  margin-top: 0px;
}

.container-wrapper {
  max-width: 238px;
  margin: 0 auto;
}

.login-container {
  padding: 20px;
  border: 1px solid #cccccc;
  border-radius: 5px;
}

.error-border {
  border-color: #ff5666;
}

.login-title {
  font-size: 24px;
  margin-bottom: 20px;
  text-align: center;
  color: #cccccc;
}

.error-text {
  color: #ff5666;
}

.login-form {
  display: flex;
  flex-direction: column;
}

.form-group {
  margin-bottom: 15px;
}

.form-label {
  margin-bottom: 5px;
}

.form-input {
  padding: 10px;
  border: 1px solid #cccccc;
  border-radius: 5px;
  background-color: #2a2a2a;
  color: #ffffff;
  width: -moz-available;
  /* WebKit-based browsers will ignore this. */
  width: -webkit-fill-available;
  /* Mozilla-based browsers will ignore this. */
  width: 100%;
}

.form-input:focus {
  border-color: #00fddc;
  outline: 2px solid #00fddc;
}

.login-button {
  padding: 10px;
  background-color: #00fddc;
  color: #000000;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.login-button:hover {
  background-color: #00fddbc0;
}

.try-again {
  margin-top: 10px;
  text-align: center;
  color: #ff5666;
}
</style>