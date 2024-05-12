<template>
  <section>
    <div>
      <div >{{ output }}</div>
    </div>
  </section>
</template>

<script>
// import VueNativeSock from 'vue-native-websocket';

//var ws = new WebSocket("ws://localhost:9000/ws");
export default {
  data() {
    return {
      output: 'Backend not yet connected, please wait...',
    };
  },
  created: function() {
    console.log("History starting connection to WebSocket Server")
    this.connection = new WebSocket("ws://localhost:9000/ws")

    this.connection.onmessage = (event) => {
      // console.log(event);
      console.log("Event has been received: ", event);
      this.output = event.data;
    }

    this.connection.onopen = function(event) {
      console.log(event)
      console.log("History successfully connected to the websocket server...")
    }
  }

    
}
//   created() {
//     this.$options.sockets.onmessage = (event) => {
//       const data = JSON.parse(event.data);
//       if (data.hasOwnProperty('output')) {
//         this.output = data.output;
//       }
//     };
//   },
//   mounted() {
//     this.connectWebSocket();
//   },
//   methods: {
//     connectWebSocket() {
//       this.$options.sockets.connect('ws://localhost:9000/ws');
//     }
//   }
};
</script>

