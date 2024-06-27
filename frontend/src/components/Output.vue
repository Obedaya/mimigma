<template>
  <section>
    <div id="output">
      <div v-html="output" style="font-size: 90%;"></div>
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
        output: '',
      };
    },
    methods: {
      // Fetch the history from the backend
      getHistory() {
        axios.get("/history")
          .then(response => {
            console.log("Received data from backend: ", response.data);
            const {
              plain,
              encrypted
            } = response.data;
            let combinedOutput = "";
            combinedOutput += encrypted;
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
    async mounted() {
      const delay = ms => new Promise(res => setTimeout(res, ms));
      this.getHistory();
      await delay(6969);
      this.getHistory();
    },
  };
</script>
