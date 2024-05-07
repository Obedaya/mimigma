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
  export default {
    data() {
      return {
        username: '',
        password: '',
        showErrorBorder: false
      };
    },
    
    methods: {
      async login() {
        try {
          const response = await fetch(`http://localhost:9000/login?username=${this.username}&password=${this.password}`, {
            method: 'POST'
          });
          if (response.ok) {
            const responseData = await response.json();
            console.log(responseData);
            this.$router.push({ name: 'main' });
          } else {
            this.showErrorBorder = true;
            console.error('Login failed:', response.status);
          }
        } catch (error) {
          console.error('Error:', error);
        }
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
    width: -moz-available;          /* WebKit-based browsers will ignore this. */
    width: -webkit-fill-available;  /* Mozilla-based browsers will ignore this. */
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
  
