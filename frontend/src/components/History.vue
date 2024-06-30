<template>
  <section>
    <div id="output">
      <div v-html="output"></div>
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
      console.log("Fetching history...");
      const auth = useAuthStore();
      const user_id = auth.user.id;
      axios.get(`/history?user_id=${user_id}`)
        .then(response => {
          console.log("Received data from backend: ", response.data);
          const { plain, encrypted } = response.data;
          let combinedOutput = "";
          for (let i = 0; i < encrypted.length; i++) { 
            combinedOutput += `${plain[i]} : ${encrypted[i]}<br>`;
          }
          this.output = combinedOutput;
          console.log("History updated.");
        })
        .catch(error => {
          console.error("Error while fetching data: ", error);
        });
    }
  },
  updated() {
    console.log("History component updated.");
    this.getHistory();
  },
  async mounted() {
  console.log("History component mounted.");
  const delay = ms => new Promise(res => setTimeout(res, ms));
  this.getHistory();
  await delay(6969);
  this.getHistory();
  },
};
</script>
