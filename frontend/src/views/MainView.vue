<template>
  <div class="container">
    <!--row 1-->
    <div class="row">
      <div class="col-3" style="align-self: center;">

        <!-- User Settings Icon + Modal-->
        <Usersettings />

        <!-- Test-->
        <!-- Enigma Settings Icon + Modal-->
        <Settings @count="rotorNumber" @toggle-plugboard="togglePlugboard" @update-rotors="updateRotors" :plugs="plugs" ref="settings"/>

      </div>
      <div class="col-6">
        <Rotorpanel :newNumber="newNumber" ref="rotorPanel" />
      </div>
      <div class="col-3">
      </div>
    </div>
    <!--row 2-->
    <div class="row">
      <div class="col">
        <!--Mimigma-Bild-->
        <img class="mimigma" @click="toggleColor" src="../assets/mimigma.png">
      </div>
      <div class="col-6">
        <Keyboard @key="update" />

      </div>
      <div class="col">
        <!-- HISTORY-->
        <div style="overflow: auto; height: 412px; display: flex; flex-direction: column-reverse; overflow-anchor: auto !important; " class="overflow-scroll border border-white">
          <!--<History :current_key="currentKey" />-->
          <History  ref="history"/>
        </div>
      </div>
    </div>
    <!--row 3-->
    <div class="row">
      <div class="col">

      </div>
      <div class="col-6">
        <Plugboard v-if="showPlugboard" @updatePlugboard="updatePlugboard" ref="plugboard"/>

      </div>
      <div class="col">
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

  export default {
    data() {
      return {
        currentKey: "",
        newNumber: 0,
        initialRotorsettings: {},
        enigmaVariant: "M3",
        rotorVariants: {},
        showPlugboard: true,
        plugs: [],

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
        // Methode die aufgerufen wird, wenn ein Key gedrückt wird
        this.currentKey = key;
        this.$refs.rotorPanel.updateRotorsFromBackend();
        this.$refs.history.getHistory();
      },

      rotorNumber(count) {
        this.newNumber = count;
      },

      togglePlugboard(show) {
        this.showPlugboard = show;
        if (!show) {

          this.$refs.plugboard.updatePlugboardInDB(true);
          this.plugs = [];
        }
      },
      updatePlugboard(plugs) {
        this.plugs = plugs;
        this.$refs.plugboard.updatePlugboardInDB();
      },
      updateRotors(rotor_positions) {
        this.$refs.rotorPanel.updateRotorsFromBackend();
      },
      toggleColor(){
       

// Zugriff auf das <body> Element und Toggeln des data-theme Attributs
const body = document.body;
const currentTheme = body.getAttribute('data-theme');
body.setAttribute('data-theme', currentTheme === 'light' ? 'dark' : 'light');

        

      }

    }
  };
</script>
