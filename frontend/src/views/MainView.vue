<template>
  <div class="container">
    <!--row 1-->
    <div class="row">
      <div class="col-3" style="align-self: center;">

        <div class="col-6" style='display: inline-block;'>
          <img class="icons" src="../../nutzer.png">

        </div>

        <div class="col-6" style='display: inline-block;'>
          <img class="icons" src="../../zahnrad.png">
        </div>

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
        <Keyboard />

      </div>
      <div class="col">
        <!-- HISTORY-->
        <div class="border border-white"></div>
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
  import {
    RouterLink,
    RouterView
  } from 'vue-router'

  export default {
    // name: 'App',
    components: {
      Keyboard,
      Plugboard,
      Rotorpanel
    }
  };
</script>