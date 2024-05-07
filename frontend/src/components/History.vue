<template>
  <section>
    <div>
      <div class="output-field">Output will appear here</div>
    </div>
  </section>
</template>

<script>
  //TODO EventBus
  //import { EventBus } from '@/EventBus.js'; // HERE

  export default {
    
    /* created() {
      EventBus.$on('keySentToBackend', () => {
        this.fetchData();
      });
    },*/ // HERE
    methods: {
      async fetchData() {
        try {
          const response = await fetch('http://localhost:9000/output');
          const data = await response.json();
          // Update the content of the div
          document.querySelector('.output-field').innerText = data;
        } catch (error) {
          console.error('Error fetching data:', error);
        }
      }
    }
  };
</script>

