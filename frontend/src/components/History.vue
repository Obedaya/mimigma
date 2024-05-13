<template>
  <section>
    <div>
      <div :key="output">{{ current_key }}</div>
    </div>
  </section>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      output: 'Backend not yet connected, please wait...',
      connection: null, // Store the WebSocket connection object
    };
  },
  methods: {
    // Send a key press event to the backend
    getKey() {
      axios.get("http://localhost:9000/keyboard")
        .then(response => {
          console.log("Received data from backend: ", response.data);
          this.key = response.data;
        })
        .catch(error => {
          console.error("Error while fetching data: ", error);
        });
    }
  },
  updated() {
    this.getKey();
  },
  props: {
    current_key: String,
  },
};
</script>

