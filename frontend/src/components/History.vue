<template>
  <section>
    <div id="output">
      <div class="overflow-scroll" v-html="output"></div>
      <!--<div :key="output"> {{ output }}</div>-->
    </div>
  </section>
</template>

<script>
import axios from "axios";

export default {
  name: "History",
  data() {
    return {
      output: 'Backend not yet connected, please wait...',
    };
  },
  methods: {
    // Fetch the history from the backend
    getHistory() {
      axios.get("/history")
        .then(response => {
          console.log("Received data from backend: ", response.data);
          const { plain, encrypted } = response.data;
          let combinedOutput = "";
          for (let i = 0; i < encrypted.length; i++) { 
            combinedOutput += `${plain[i]} : ${encrypted[i]}<br>`;
          }
          this.output = combinedOutput;
        })
        .catch(error => {
          console.error("Error while fetching data: ", error);
        });
    }
  },
  updated() {
    this.getHistory();
  },
  mounted() {
    this.getHistory();
  },
};
</script>
