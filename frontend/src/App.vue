<template>
  <div id="app">
    <!-- Hier werden Tastatur + Leuchtbrett eingebunden -->
    <Keyboard />
  </div>
</template>



<script>
// Import von Tastatur-Komponente, welche oben genutzt wird
import Keyboard from './components/Keyboard.vue';

export default {
  name: 'App',
  components: {
    Keyboard,
  },
};
</script>
