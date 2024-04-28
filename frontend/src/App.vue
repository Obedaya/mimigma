<template>
  <div id="app">
    <!-- Hier werden Tastatur + Leuchtbrett + Rotorenpanel eingebunden -->
    
    <Keyboard />
    <Plugboard/>
    <Rotorpanel/>
  </div>
</template>

<script>
// Import von Tastatur-Komponente, welche oben genutzt wird
import Keyboard from './components/Keyboard.vue';
import Plugboard from './components/Plugboard.vue';
import Rotorpanel from './components/Rotorpanel.vue';

export default {
  name: 'App',
  components: {
    Keyboard,
    Plugboard,
    Rotorpanel,
  },
};
</script>
