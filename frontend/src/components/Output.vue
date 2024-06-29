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
  import {
    useAuthStore
  } from "@/stores/auth.js";

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
        const auth = useAuthStore();
        const user_id = auth.user.id;
        axios.get(`/history?user_id=${user_id}`)
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
