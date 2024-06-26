<template>
  <section>
    <!-- upper keyboard -->
    <div class="keyboard" style="pointer-events: none;">
      <div v-for="key in keys1" :key="key"
        :class="{ 'key': true, 'highlighted': key === highlightedKeyUpper, 'lamp': true }">
        {{ key }}
      </div>
      <div></div>
      <div v-for="key in keys2" :key="key"
        :class="{ 'key': true, 'highlighted': key === highlightedKeyUpper, 'lamp': true }">
        {{ key }}
      </div>
      <div v-for="key in keys3" :key="key"
        :class="{ 'key': true, 'highlighted': key === highlightedKeyUpper, 'lamp': true }">
        {{ key }}
      </div>
    </div>
  </section>
  <section>
    <!-- lower keyboard -->
    <div class="keyboard lower">
      <div v-for="key in keys1" :key="key"
        :class="{ 'key': true, 'highlighted': key === highlightedKeyLower, 'keyboard': true }"
        @click="highlightLowerMouse(key)">
        {{ key }}
      </div>
      <div></div>
      <div v-for="key in keys2" :key="key"
        :class="{ 'key': true, 'highlighted': key === highlightedKeyLower, 'keyboard': true }"
        @click="highlightLowerMouse(key)">
        {{ key }}
      </div>
      <div v-for="key in keys3" :key="key"
        :class="{ 'key': true, 'highlighted': key === highlightedKeyLower, 'keyboard': true }"
        @click="highlightLowerMouse(key)">
        {{ key }}
      </div>
    </div>
  </section>
  <History :current_key="highlightedKeyUpper" />
</template>

<script>
  import axios from "axios";
  import {
    useAuthStore
  } from '@/stores/auth';

  export default {
    data() {
      return {
        keys1: ['Q', 'W', 'E', 'R', 'T', 'Z', 'U', 'I', 'O'],
        keys2: ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K'],
        keys3: ['P', 'Y', 'X', 'C', 'V', 'B', 'N', 'M', 'L'],
        highlightedKeyUpper: null,
        highlightedKeyLower: null,
        isBeingProcessed: false,
      };
    },
    methods: {
      highlightLowerKeyboard(key) {
        if (!this.isBeingProcessed) {
          this.isBeingProcessed = true;
          this.highlightedKeyLower = key;
          this.sendKeyToBackend(key); // send pressed key to backend
        }
      },
      highlightLowerMouse(key) {
        this.highlightLowerKeyboard(key);
        setTimeout(() => {
          this.resetHighlight();
          this.isBeingProcessed = false;
        }, 1000); // 1 sec 
      },
      resetHighlight() {
        this.highlightedKeyLower = null;
        this.highlightedKeyUpper = null;
      },
      handleKeyPress(event) {
        const key = event.key.toUpperCase();
        if (this.keys1.includes(key) || this.keys2.includes(key) || this.keys3.includes(key)) {
          this.highlightLowerKeyboard(key);
        }
      },
      handleKeyUp() {
        this.isBeingProcessed = false;
        this.resetHighlight();
      },
      async sendKeyToBackend(key) {
        axios.post(`/keyboard?key=${key}`)
          .then(response => {
            console.log("Received data from backend: ", response.data);
            this.getEncryptedKey(key);
          })
          .catch(error => {
            console.error("Error while fetching data: ", error);
          });
      },
      async getEncryptedKey(key) {
        const auth = useAuthStore();
        const user_id = auth.currentUserID;
        axios.get(`/lamp?user_id=${user_id}`)
          .then(response => {
            console.log("Received data from backend: ", response.data);
            this.highlightedKeyUpper = response.data.encrypted_key; // update upper keyboard with encrypted key
            this.$emit('key', key);
          })
          .catch(error => {
            console.error("Error while fetching data: ", error);
          });
      }
    },
    mounted() {
      window.addEventListener('keydown', this.handleKeyPress);
      window.addEventListener('keyup', this.handleKeyUp);

      // // eventlistener on click lower keyboard
      // const lowerKeys = document.querySelectorAll('.lower .key');
      // lowerKeys.forEach(key => {
      //   key.addEventListener('click', () => {
      //     this.highlightLowerMouse(key.textContent);
      //   });
      // });
    },
    beforeDestroy() {
      window.removeEventListener('keydown', this.handleKeyPress);
      window.removeEventListener('keyup', this.handleKeyUp);

      // remove eventlistener
      // const lowerKeys = document.querySelectorAll('.lower .key');
      // lowerKeys.forEach(key => {
      //   key.removeEventListener('click', () => {
      //     this.highlightLowerMouse(key.textContent);
      //   });
      // });
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
    color: var(--color-highlighted);
  }

  .key {
    width: 50px;
    height: 50px;
    border: 1px solid var(--color-border);
    margin: 5px;
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
  }

  .highlighted {
    background-color: rgb(255, 239, 160);
    color: var(--color-background);
    font-weight: bold;
  }
</style>