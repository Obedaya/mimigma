<template>
  <section>
    <div>
      <div :key="output">{{ output }}</div>
    </div>
  </section>
</template>

<script>
export default {
  data() {
    return {
      output: 'Backend not yet connected, please wait...',
      connection: null // Store the WebSocket connection object
    };
  },
  mounted() {
    console.log("History starting connection to WebSocket Server");
    this.connection = new WebSocket("ws://localhost:9000/ws");

    this.connection.onmessage = (event) => {
      console.log("Event has been received: ", event);
      this.output = event.data;
      this.$forceUpdate();
    };

    this.connection.onopen = function(event) {
      console.log("History successfully connected to the websocket server...");
    };

    // Optionally, handle WebSocket errors and close events
    this.connection.onerror = function(error) {
      console.error("WebSocket error:", error);
    };

    this.connection.onclose = function(event) {
      console.log("WebSocket connection closed:", event);
    };
  },
  beforeDestroy() {
    // Close the WebSocket connection when the component is destroyed
    if (this.connection) {
      this.connection.close();
    }
  }
};
</script>

