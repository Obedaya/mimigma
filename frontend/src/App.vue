<template>
  <div id="app">
    <!-- Hier werden Tastatur + Leuchtbrett eingebunden -->
    <Keyboard />
    <Plugboard />
  </div>
</template>



<script>
// Import von Tastatur-Komponente, welche oben genutzt wird
import Keyboard from './components/Keyboard.vue';
import Plugboard from './components/Plugboard.vue';

export default {
  name: 'App',
  components: {
    Keyboard,
    Plugboard,
  },
};
</script>
