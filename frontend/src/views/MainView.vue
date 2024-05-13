<template>
  <div class="container">
    <!--row 1-->
    <div class="row">
      <div class="col-3" style="align-self: center;">

        <!-- User Settings Icon + Modal-->
        <Usersettings />

        <!-- Enigma Settings Icon + Modal-->
        <Settings />

      </div>
      <div class="col-6">
        <Rotorpanel />

      </div>
      <div class="col-3">
      </div>
    </div>
    <!--row 2-->
    <div class="row">
      <div class="col">
        <!--Mimigma-Bild-->
        <img class="mimigma" src="../../mimigma.png">
      </div>
      <div class="col-6">
        <Keyboard @key="update"/>

      </div>
      <div class="col">
        <!-- HISTORY-->
        <div class="border border-white">
          <History :current_key="currentKey"/>
        </div>
      </div>
    </div>
    <!--row 3-->
    <div class="row">
      <div class="col">

      </div>
      <div class="col-6">
        <Plugboard />

      </div>
      <div class="col">
        <!--INPUT-->
        <div class="border border-white"></div>
      </div>
    </div>
  </div>


</template>
<script>
  import Keyboard from '../components/Keyboard.vue';
  import Plugboard from '../components/Plugboard.vue';
  import Rotorpanel from '../components/Rotorpanel.vue';
  import Usersettings from '../components/Usersettings.vue';
  import Settings from '../components/Settings.vue';
  import History from '../components/History.vue';
  import {
    RouterLink,
    RouterView
  } from 'vue-router'

  export default {
    data() {
      return {
        currentKey: "",
      };
    },
    // name: 'App',
    components: {
      Keyboard,
      Plugboard,
      Rotorpanel,
      Usersettings,
      Settings,
      History
    },
    methods: {
      update(key) {
        this.currentKey = key;
        console.log(key);
      }
    }
  };
</script>
