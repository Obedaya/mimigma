<template>
  <div class="col-6" style='display: inline-block;'>

    <!-- Button trigger modal -->
    <div data-bs-toggle="modal" data-bs-target="#SettingsModal" id="settings-button">
      <img class="icons" src="../assets/zahnrad.png">
    </div>
    <!-- Modal -->
    <div class="modal fade" id="SettingsModal" tabindex="-1" aria-labelledby="SettingsModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content modalbackground">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Einstellungen</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"
                    id="modal-close-button"></button>
          </div>
          <div class="modal-body">
            <div data-mdb-input-init class="form-outline">
              <label class="col-6" for="typeNumber">Rotorenanzahl</label>
              <!-- der Value Wert sollte dann durch die aktuelle Anzahl der Rotoren getauscht werden!!-->
              <input value="3" min="3" max="10" type="number" v-model="rotorCount" id="rotorCount" class="col-6"
                     @input="changeRotorCount"/>
            </div>
            <br>
            <!-- Anzeige Plugboard -->
            <div>
              <input type="checkbox" v-model="showPlugboard"> Plugboard anzeigen
            </div>
            <br>
            <table class="table table-responsive table-bordered settings-table">
              <!--  erste Zeile -->
              <thead>
              <tr>
                <div class="dropdown">
                  Reflector
                  <button class="btn btn-outline-secondary dropdown-toggle" type="button" id="DropdownReflector"
                          data-bs-toggle="dropdown">
                    {{ selectedReflectorOption }}
                  </button>
                  <div class="dropdown-menu reflector-menu" :aria-labelledby="'dropdown' + index"
                       style="max-height: 100px; overflow-y: auto;">
                    <a class="dropdown-item dropdown-reflector" v-for="(value, key) in dropdownReflectorOptions"
                       :key="key" @click="selectReflectorOption(index, value)">{{ value }}</a>
                  </div>
                </div>

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
                    <div class="dropdown-menu variant-menu" :aria-labelledby="'dropdown' + index"
                         style="max-height: 100px; overflow-y: auto;">
                      <a class="dropdown-item dropdown-variant" v-for="(value, key) in dropdownRotorOptions"
                         :key="key" @click="selectRotorOption(index, value)">{{ value }}</a>
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
                    <div class="dropdown-menu initial-menu" :aria-labelledby="'dropdownPosition' + index"
                         style="max-height: 100px; overflow-y: auto;">
                      <a class="dropdown-item dropdown-initial" v-for="letter in alphabet" :key="'position' + index"
                         @click="selectInitialPosition(index, letter)">{{ letter }}</a>
                    </div>
                  </div>
                </td>
              </tr>

              <tr>
                <td>Ringposition</td>
                <td v-for="(RingPosition, index) in selectedRingPositions" :key="'ringPosition' + index">
                  <div class="dropdown">
                    <button class="btn btn-outline-secondary dropdown-toggle" type="button"
                            :id="'DropdownRing' + index" data-bs-toggle="dropdown">
                      {{ RingPosition }}
                    </button>
                    <div class="dropdown-menu ring-menu" :aria-labelledby="'dropdownRing' + index"
                         style="max-height: 100px; overflow-y: auto;">
                      <a class="dropdown-item dropdown-ring" v-for="letter in numbers"
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
            <button @click="sendSettingsToBackend" type="button modalSendButton" data-bs-dismiss="modal"
                    class="btn btn-primary" id="modal-submit-button">Save changes
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import {
  useAuthStore
} from '@/stores/auth';

export default {
  data() {
    return {
      rotorCount: 3,
      enigmaVariant: 'M3',
      // Plugboard Anzeigen Variable
      showPlugboard: true,

      RotorTitle: {
        1: 'Rotor 1',
        2: 'Rotor 2',
        3: 'Rotor 3'
      }, //hier kann die Titel für Rotoren erweitert werden

      rotorHeaders: {
        1: 'I',
        2: 'II',
        3: 'III'
      }, //Titel der Dropdowns for Rotoren. hier kann man die Spalten der Rotoren erweitern
      dropdownRotorOptions: {
        1: 'I',
        2: 'II',
        3: 'III',
        4: 'IV',
        5: 'V'
      },
      alphabet: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
        'U', 'V', 'W', 'X', 'Y', 'Z'
      ],
      numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26],

      selectedInitialPositions: {
        1: 'A',
        2: 'A',
        3: 'A'
      }, // Hier werden die ausgewählten AusgangsPositionen gespeichert
      selectedRingPositions: {
        1: '1',
        2: '1',
        3: '1'
      }, // Hier werden die ausgewählten RingPositionen gespeichert

      ReflectorTitle: {
        'A': 'UKW_A',
        'B': 'UKW_B',
        'C': 'UKW_C',
        'N': 'UKW_N'
      },
      dropdownReflectorOptions: {
        1: 'UKW_A',
        2: 'UKW_B',
        3: 'UKW_C',
        4: 'UKW_N'
      },
      selectedReflectorOption: "UKW_B",

    };
  },
  props: {
    plugs: Array,
  },
  //Watcher, ob das Plugboard angezeigt wird oder nicht
  watch: {
    showPlugboard(newVal) {
      this.$emit('toggle-plugboard', newVal);
    }
  },
  methods: {

    sendRotorCountToBackend(count) {
      axios.post(`/rotor/count?count=${count}`)
          .then(response => {
            console.log("Received data from backend: ", response.data);
            this.$emit('count', count);
          })
          .catch(error => {
            console.error("Error while fetching data: ", error);
          });
    },
    sendRotorToBackend(rotor) {
      axios.post(`/rotor`, rotor)
          .then(response => {
            console.log("Received data from backend: ", response.data);
            this.$emit('initialRotor', this.selectedInitialPositions);
            this.$emit('rotorVariants', this.rotorHeaders);
          })
          .catch(error => {
            console.error("Error while fetching data: ", error);
          });
    },
    sendReflectorToBackend(selectedReflectorOption) {
      const auth = useAuthStore();
      axios.post(`/reflector?user_id=${auth.currentUserID}&reflector=${selectedReflectorOption}`)
          .then(response => {
            console.log("Received data from backend: ", response.data);
          })
          .catch(error => {
            console.error("Error while fetching data: ", error);
          });
    },

    createRotor() {
      // Initialize arrays for rotors, rotor_positions, and ring_positions
      let rotors = [];
      let rotor_positions = [];
      let ring_positions = [];

      const auth = useAuthStore();

      // Populate the arrays
      for (let i = 1; i <= this.rotorCount; i++) {
        rotors.push(this.rotorHeaders[i]);
        rotor_positions.push(this.selectedInitialPositions[i]);
        // Add ring position to the array and convert to corresponding letter
        ring_positions.push(String.fromCharCode(parseInt(this.selectedRingPositions[i]) + 64));
      }

      // Create the initialRotor object
      let initialRotor = {
        user_id: auth.currentUserID,
        machine_type: this.enigmaVariant,
        rotors: rotors,
        rotor_positions: rotor_positions.join(''),
        ring_positions: ring_positions.join(''),
        plugboard: this.plugs,
      };
      return initialRotor;
    },
    addRotor(number) {
      // Add new rotor to the settings
      this.RotorTitle[number] = 'Rotor ' + number;
      this.rotorHeaders[number] = 'I';
      this.selectedInitialPositions[number] = 'A';
      this.selectedRingPositions[number] = 'A';
    },
    removeRotor(number) {
      // Remove rotor from the settings
      delete this.RotorTitle[number];
      delete this.rotorHeaders[number];
      delete this.selectedInitialPositions[number];
      delete this.selectedRingPositions[number];
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
    selectReflectorOption(index, reflector) {
      this.selectedReflectorOption = reflector;
    },
    sendSettingsToBackend() {
      this.sendRotorCountToBackend(this.rotorCount);
      let rotors = this.createRotor();
      console.log(rotors)
      // Send rotor as json to backend
      this.sendRotorToBackend(rotors);
      this.sendReflectorToBackend(this.selectedReflectorOption);
    },
    changeRotorCount() {
      if (this.rotorCount >= 3 && this.rotorCount <= 10) {
        for (let i = 4; i <= this.rotorCount; i++) {
          if (!this.RotorTitle[i]) {
            this.addRotor(i);
          }
        }
        for (let i = 10; i > this.rotorCount; i--) {
          if (this.RotorTitle[i]) {
            this.removeRotor(i);
          }
        }
      } else {
        console.error('Ungültige Anzahl von Rotoren.');
      }
    },
  },
  created() {
    this.sendSettingsToBackend();
  },
};
</script>

<style>
.settings-table {
  padding-top: 2rem;
}

#SettingsModal .modal-dialog {
  color: black;
  max-width: 60%;
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