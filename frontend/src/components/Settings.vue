<template>
  <div class="col-6" style='display: inline-block;'>

    <!-- Button trigger modal -->
    <div data-bs-toggle="modal" data-bs-target="#SettingsModal">
      <img class="icons" src="../assets/zahnrad.png">
    </div>
    <!-- Modal -->
    <div class="modal fade" id="SettingsModal" tabindex="-1" aria-labelledby="SettingsModalLabel"
         aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content modalbackground">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Einstellungen</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <div data-mdb-input-init class="form-outline">
              <label class="col-6" for="typeNumber">Rotorenanzahl</label>
              <!-- der Value Wert sollte dann durch die aktuelle Anzahl der Rotoren getauscht werden!!-->
              <input value="3" min="1" max="10" type="number" v-model="rotorCount" id="rotorCount" class="col-6"/>
            </div>
            <br>
            <table class="table table-responsive table-bordered settings-table">
              <!--  erste Zeile -->
              <thead>
              <tr>
                <th scope="col">Platz für Reflector</th>
                <!--Title für Buchstaben-->
                <th v-for="(rotor, key) in RotorTitle" :key="key" scope="col" class="text-center">{{ rotor }}</th>
              </tr>
              </thead>

              <tbody>
              <tr>
                <td>Rotor</td>
                <td v-for="(rotor, index) in rotorHeaders" :key=" 'rotor' + index">
                  <div class="dropdown">
                    <button class="btn btn-outline-secondary dropdown-toggle" type="button"
                            :id="'DropdownRotor' + index" data-bs-toggle="dropdown">
                      {{ rotor }}
                    </button>
                    <div class="dropdown-menu" :aria-labelledby="'dropdown' + index"
                         style="max-height: 100px; overflow-y: auto;">
                      <a class="dropdown-item" v-for="(value, key) in dropdownRotorOptions" :key="key"
                         @click="selectRotorOption(index, value)">{{ value }}</a>
                    </div>
                  </div>
                </td>
              </tr>

              <tr>
                <td>Ausgangsposition</td>
                <td v-for="(InitialPosition, index) in selectedInitialPositions" :key="'position' + index">
                  <div class="dropdown">
                    <button class="btn btn-outline-secondary dropdown-toggle" type="button"
                            :id="'DropdownPosition' + index" data-bs-toggle="dropdown">
                      {{ InitialPosition }}
                    </button>
                    <div class="dropdown-menu" :aria-labelledby="'dropdownPosition' + index"
                         style="max-height: 100px; overflow-y: auto;">
                      <a class="dropdown-item" v-for="letter in alphabetArray_Position" :key="'position' + index"
                         @click="selectInitialPosition(index, letter)">{{ letter }}</a>
                    </div>
                  </div>
                </td>
              </tr>

              <tr>
                <td>Ringposition</td>
                <td v-for="(RingPosition, index) in selectedRingPositions" :key="'ringPosition' + index">
                  <div class="dropdown">
                    <button class="btn btn-outline-secondary dropdown-toggle" type="button" :id="'DropdownRing' + index"
                            data-bs-toggle="dropdown">
                      {{ RingPosition }}
                    </button>
                    <div class="dropdown-menu" :aria-labelledby="'dropdownRing' + index"
                         style="max-height: 100px; overflow-y: auto;">
                      <a class="dropdown-item" v-for="letter in alphabetArray_Ring"
                         :key="'ringPosition' + index + letter" @click="selectRingPosition(index, letter)">{{
                          letter
                        }}</a>
                    </div>
                  </div>
                </td>
              </tr>
              </tbody>
            </table>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button @click="sendRotorCountToBackend(rotorCount)" type="button modalSendButton" data-bs-dismiss="modal"
                    class="btn btn-primary">Save changes
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      RotorTitle: {1: 'Rotor 1', 2: 'Rotor 2', 3: 'Rotor 3'}, //hier kann die Titel für Rotoren erweitert werden

      rotorHeaders: {1: 'I', 2: 'I', 3: 'I'}, //Titel der Dropdowns for Rotoren. hier kann man die Spalten der Rotoren erweitern
      dropdownRotorOptions: {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V'},

      selectedInitialPositions: {1: 'A', 2: 'A', 3: 'A'}, // Hier werden die ausgewählten AusgangsPositionen gespeichert
      alphabetArray_Position: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], // Array der verfügbaren Buchstaben

      selectedRingPositions: {1: 'A', 2: 'A', 3: 'A'}, // Hier werden die ausgewählten RingPositionen gespeichert
      alphabetArray_Ring: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], // Array der verfügbaren Buchstaben
    };
  },
  methods: {

    sendRotorCountToBackend(count) {
      console.log(count);
      axios.post(`/rotor?count=${count}`)
          .then(response => {
            console.log("Received data from backend: ", response.data);
            this.$emit('count', count);
          })
          .catch(error => {
            console.error("Error while fetching data: ", error);
          });
    },
    selectRotorOption(index, rotor) {
      this.rotorHeaders[index] = rotor;
    },

    selectInitialPosition(index, letter) {
      this.selectedInitialPositions[index] = letter;
    },

    selectRingPosition(index, letter) {
      this.selectedRingPositions[index] = letter;
    },
  },
};
</script>

<style>

.settings-table {
  padding-top: 2rem;
}

#SettingsModal .modal-dialog {
  color: black;
  max-width: 50%;
  height: 80%;
}

.table thead th {
  background-color: #191970;
  color: #fff;
  text-align: center;
}

.modal-body {
  overflow-x: auto;
}

/* damit die Toggles in der Mitte bleieben */
.dropdown-toggle {
  margin: 0 auto;
  display: block;
}

.dropdown-item:hover {
  background-color: #faebd7;
  cursor: pointer;
}
</style>