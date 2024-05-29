<template>
  <section>
    <div id="output">
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
    };
  },
  methods: {
    // get key from backend
    getKey() {
      axios.get("/lamp")
        .then(response => {
          console.log("Received data from backend: ", response.data);
          this.output = response.data.status;
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