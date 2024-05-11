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
      <div v-for="key in keys1" :key="key" 
        :class="{ 'key': true, 'highlighted': key === highlightedKeyLower }">{{ key }}</div>
      <div></div>
      <div v-for="key in keys2" :key="key"
        :class="{ 'key': true, 'highlighted': key === highlightedKeyLower }">{{ key }}</div>
      <div v-for="key in keys3" :key="key" 
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
      highlightLowerKeyboard(key) {
        this.highlightedKeyUpper = key;
        this.highlightedKeyLower = key;
      },
      highlightLowerMouse(key) {
        this.highlightLowerKeyboard(key);
        setTimeout(() => {
          this.resetHighlight();
        }, 1000); // Abwählen der virtuellen Taste nach 1 Sekunde
      },
      resetHighlight() {
        this.sendKeyToBackend(this.highlightedKeyUpper); // Send the pressed key to the backend
        this.highlightedKeyUpper = null;
        this.highlightedKeyLower = null;
      },
      handleKeyPress(event) {
        const key = event.key.toUpperCase();
        if (this.keys1.includes(key) || this.keys2.includes(key) || this.keys3.includes(key)) {
          this.highlightLowerKeyboard(key);
        }
      },
      handleKeyUp() {
        this.resetHighlight();
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
    },
    mounted() {
      window.addEventListener('keydown', this.handleKeyPress);
      window.addEventListener('keyup', this.handleKeyUp);

      // Eventlistener für click auf die Tasten der unteren Tastatur hinzufügen
      const lowerKeys = document.querySelectorAll('.lower .key');
      lowerKeys.forEach(key => {
        key.addEventListener('click', () => {
          this.highlightLowerMouse(key.textContent);
        });
      });
    },
    beforeDestroy() {
      window.removeEventListener('keydown', this.handleKeyPress);
      window.removeEventListener('keyup', this.handleKeyUp);

      // Eventlistener für click auf die Tasten der unteren Tastatur entfernen
      const lowerKeys = document.querySelectorAll('.lower .key');
      lowerKeys.forEach(key => {
        key.removeEventListener('click', () => {
          this.highlightLowerMouse(key.textContent);
        });
      });
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
    background-color: rgb(255, 239, 160);
    color: #2a2a2a;
    font-weight: bold;
  }
</style>