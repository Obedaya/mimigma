<template>
  <div class="container">
    <!--row 1-->
    <div class="row">
      <div class="col-3" style="align-self: center;">

        <!-- User Settings Icon + Modal-->
        <Usersettings />

        <!-- Test-->
        <!-- Enigma Settings Icon + Modal-->
        <Settings @count="rotorNumber" @toggle-plugboard="togglePlugboard" @update-rotors="updateRotors" @update-output="updateOutput" @update-plugs="updatePlugs" :plugs="plugs"
          ref="settings" />

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
        <div
          style="overflow: auto; height: 412px; display: flex; flex-direction: column-reverse; overflow-anchor: auto !important;"
          class="border border-white">
          <!--<History :current_key="currentKey" />-->
          <History ref="history" />
        </div>
      </div>
    </div>
    <!--row 3-->
    <div class="row">
      <div class="col">

      </div>
      <div class="col-6">
        <Plugboard v-if="showPlugboard" @updatePlugboard="updatePlugboard" ref="plugboard" />

      </div>
      <div class="col-3" style="padding: 1rem;">

        <div style="word-wrap: break-word; overflow: auto; overflow-anchor: auto !important;"
          class="border border-white">
          <Output ref="output" />
        </div>
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
  import Output from '../components/Output.vue';

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
      History,
      Output
    },
    methods: {
      update(key) {
        // Methode die aufgerufen wird, wenn ein Key gedrückt wird
        console.log("Key pressed:", key);
        this.currentKey = key;
        this.$refs.rotorPanel.updateRotorsFromBackend();
        this.$refs.history.getHistory();
        this.$refs.output.getHistory();
      },

      rotorNumber(count) {
        console.log("Rotor count updated:", count);
        this.newNumber = count;
      },

      togglePlugboard(show) {
        console.log("Toggle plugboard:", show);
        this.showPlugboard = show;
        if (!show) {

          this.$refs.plugboard.updatePlugboardInDB(true);
          this.plugs = [];
        }
      },
      updatePlugboard(plugs) {
        console.log("Plugboard updated:", plugs);
        this.plugs = plugs;
        this.$refs.plugboard.updatePlugboardInDB();
      },
      updateRotors(rotor_positions) {
        console.log("Update rotors:", rotor_positions);
        this.$refs.rotorPanel.updateRotorsFromBackend();
      },
      toggleColor() {


        // Zugriff auf das <body> Element und Toggeln des data-theme Attributs
        const body = document.body;
        const currentTheme = body.getAttribute('data-theme');
        body.setAttribute('data-theme', currentTheme === 'light' ? 'dark' : 'light');
        console.log("Toggled color theme to:", currentTheme === 'light' ? 'dark' : 'light');
      },
      updateOutput() {
        console.log("Updating output...");
        this.$refs.history.getHistory();
        this.$refs.output.getHistory();
        this.plugs = [];
        this.$refs.plugboard.updatePlugboardInDB(true);
      },
      updatePlugs(plugs) {
        console.log("Updating plugs:", plugs);
        this.plugs = plugs;
        this.$refs.plugboard.updatePlugs(plugs);
      }
    }
  };
</script>