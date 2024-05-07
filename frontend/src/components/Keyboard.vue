<template>
  <section>
    <!-- Obere Tastatur -->
    <div class="keyboard" style="pointer-events: none;">
      <div v-for="key in keys1" :key="key" :class="{ 'key': true, 'highlighted': key === highlightedKeyUpper }">
        {{ key }}</div>
      <div></div>
      <div v-for="key in keys2" :key="key" :class="{ 'key': true, 'highlighted': key === highlightedKeyUpper }">
        {{ key }}</div>
      <div v-for="key in keys3" :key="key" :class="{ 'key': true, 'highlighted': key === highlightedKeyUpper }">
        {{ key }}</div>
    </div>
  </section>
  <section>
    <!-- Untere Tastatur -->
    <div class="keyboard lower">
      <div v-for="key in keys1" :key="key" @click="highlightLower(key)"
        :class="{ 'key': true, 'highlighted': key === highlightedKeyLower }">{{ key }}</div>
      <div></div>
      <div v-for="key in keys2" :key="key" @click="highlightLower(key)"
        :class="{ 'key': true, 'highlighted': key === highlightedKeyLower }">{{ key }}</div>
      <div v-for="key in keys3" :key="key" @click="highlightLower(key)"
        :class="{ 'key': true, 'highlighted': key === highlightedKeyLower }">{{ key }}</div>
    </div>
  </section>
</template>

<script>
  //TODO EventBus 
  //import { EventBus } from '@/EventBus.js'; //HERE
  export default {
    data() {
      return {
        keys1: ['Q', 'W', 'E', 'R', 'T', 'Z', 'U', 'I', 'O'],
        keys2: ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K'],
        keys3: ['P', 'Y', 'X', 'C', 'V', 'B', 'N', 'M', 'L'],
        highlightedKeyUpper: null,
        highlightedKeyLower: null,
      };
    },
    methods: {
      highlightUpper(key) {
        this.highlightedKeyUpper = key;
      },
      highlightLower(key) {
        this.highlightedKeyUpper =
        key; // Hier abändern, wenn Verschlüsselung steht; das ist der Punkt, wo entschieden wird, welcher Buchstabe gehighlighted wird
        this.highlightedKeyLower = key;
        this.sendKeyToBackend(key); // Send the pressed key to the backend
        // Löschen des Highlights nach einer kurzen Verzögerung (hier 1,2sek Millisekunden)
        setTimeout(() => {
          this.highlightedKeyUpper = null;
          this.highlightedKeyLower = null;
        }, 1200);
      },
      async sendKeyToBackend(key) {
        try {
          const response = await fetch(`http://localhost:9000/input?key=${key}`, {
            method: 'POST',
          });
          // EventBus.$emit('keySentToBackend'); // HERE
        } catch (error) {
          console.error('Error sending key to backend:', error);
        }
      },
      handleKeyPress(event) {
        const key = event.key.toUpperCase();
        if (this.keys1.includes(key) || this.keys2.includes(key) || this.keys3.includes(key)) {
          this.highlightLower(key);
        }
      },
    },
    mounted() {
      window.addEventListener('keydown', this.handleKeyPress);
    },
    beforeDestroy() {
      window.removeEventListener('keydown', this.handleKeyPress);
    },
  };
</script>

<style>
  .keyboard {
    display: grid;
    grid-template-columns: repeat(9, 1fr);
    gap: 5px;
    justify-content: center;
  }

  .lower .key.highlighted {
    background-color: grey;
    color: white;
  }

  .key {
    width: 50px;
    height: 50px;
    border: 1px solid #ccc;
    margin: 5px;
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
  }

  .highlighted {
    background-color: yellow;
    color: #2a2a2a;
  }
</style>
