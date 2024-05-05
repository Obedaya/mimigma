<template>
    <div id="app">
      <Rotorpanel />
      <Keyboard />
      <Plugboard />
      <!-- <RouterView/> -->
    </div>
  </template>
  
<script>
import Keyboard from '../components/Keyboard.vue';
import Plugboard from '../components/Plugboard.vue';
import Rotorpanel from '../components/Rotorpanel.vue';
import { RouterLink, RouterView } from 'vue-router'

export default {
  // name: 'App',
  components: {
    Keyboard,
    Plugboard,
    Rotorpanel
  }
};
</script>

