<template>
  <section>
    <div class="rotor_panel">
      <div v-for="(rotor, index) in rotors" :key="index" :ref="'rotor' + (index + 1)" class="rotor">
        <div class="nextletter" @click="rotateRotor('rotor' + (index + 1), 'next')">{{ rotor.next }}</div>
        <div class="currentletter" @click="rotateRotor('rotor' + (index + 1), 'current')">{{ rotor.current }}</div>
        <div class="prevletter" @click="rotateRotor('rotor' + (index + 1), 'prev')">{{ rotor.prev }}</div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      rotors: [],
      rotationCount: 0, // Zählvariable für die Anzahl der Aufrufe
      rotorRotationCounts: [],
      rotorTurnovers: [],
      turnovers: {},
    };
  },
  methods: {
    initializeRotors(i) {
      for (let j = 0; j < i; j++) {
        this.rotors.push({
          next: 'B',
          current: 'A',
          prev: 'Z',
        });
        this.rotorRotationCounts.push(0);
      }
    },
    rotateRotor(rotorRef, direction) {
      const rotorIndex = parseInt(rotorRef.substr(5)) - 1;
      const rotor = this.rotors[rotorIndex];
      switch (direction) {
        case 'next':
          rotor.prev = rotor.current;
          rotor.current = rotor.next;
          rotor.next = String.fromCharCode(((rotor.next.charCodeAt(0) - 65 + 1) % 26) + 65);
          if (this.rotorRotationCounts[rotorIndex] === this.rotorTurnovers[rotorIndex]) {
            this.rotorRotationCounts[rotorIndex] = 0;
            this.rotorTurnovers[rotorIndex] = 25;
          } else {
            this.rotorRotationCounts[rotorIndex]++;
          }
          break;
        case 'current':
          break;
        case 'prev':
          rotor.next = rotor.current;
          rotor.current = rotor.prev;
          rotor.prev = String.fromCharCode(((rotor.prev.charCodeAt(0) - 65 + 25) % 26) + 65);
          if (this.rotorRotationCounts[rotorIndex] === 0) {
            this.rotorRotationCounts[rotorIndex] = 25;
            this.rotorTurnovers[rotorIndex] = 25;
          } else {
            this.rotorRotationCounts[rotorIndex]--;
          }
          break;
      }
    },
    changeRotorCount(newRotorCount) {
      if (newRotorCount > 0 && newRotorCount <= 10) {
        const currentRotorCount = this.rotors.length;
        if (newRotorCount > currentRotorCount) {
          for (let i = currentRotorCount; i < newRotorCount; i++) {
            this.rotors.push({
              next: 'B',
              current: 'A',
              prev: 'Z',
            });
          }
        } else if (newRotorCount < currentRotorCount) {
          this.rotors.splice(newRotorCount);
        }
      } else {
        console.error('Ungültige Anzahl von Rotoren.');
      }
    },
    rotateRotorOnKey() {
      for (let i = 0; i < this.rotorRotationCounts.length; i++) {
        const rotor = this.rotors[this.rotors.length - 1 - i];
        if (this.rotorRotationCounts[this.rotorRotationCounts.length - 1 - i] === this.rotorTurnovers[this.rotorTurnovers.length - 1 - i]) {
          rotor.prev = rotor.current;
          rotor.current = rotor.next;
          rotor.next = String.fromCharCode(((rotor.next.charCodeAt(0) - 65 + 1) % 26) + 65);
          this.rotorRotationCounts[this.rotorRotationCounts.length - 1 - i] = 0;
          this.rotorTurnovers[this.rotorTurnovers.length - 1 - i] = 25;
        } else {
          rotor.prev = rotor.current;
          rotor.current = rotor.next;
          rotor.next = String.fromCharCode(((rotor.next.charCodeAt(0) - 65 + 1) % 26) + 65);
          this.rotorRotationCounts[this.rotorRotationCounts.length - 1 - i]++;
          break;
        }
      }
    },
    async getStandardSettings() {
      return axios.get(`/rotor/standard?variant=${this.enigmaVariant}`)
          .then(response => {
            console.log("Received data from backend: ", response.data);
            this.turnovers = response.data.turnovers;
          })
          .catch(error => {
            console.error("Error while fetching data: ", error);
          });
    },
    calculateRotorTurnover(index) {
      const rotorVariant = this.rotorVariants[index + 1];
      const turnoverLetter = this.turnovers[rotorVariant];
      const turnoverPosition = turnoverLetter.charCodeAt(0) - 'A'.charCodeAt(0);
      const rotorPosition = this.initialRotorsettings[index + 1].charCodeAt(0) - 'A'.charCodeAt(0);
      this.rotorTurnovers[index] = (turnoverPosition) % 26;
      this.rotorRotationCounts[index] = rotorPosition;
    },

    async getRotations() {
      await this.getStandardSettings();
      const rotorCount = Object.keys(this.initialRotorsettings).length;
      for (let i = 0; i < rotorCount; i++) {
        this.calculateRotorTurnover(i);
      }
      console.log("Rotor Turnovers: ", this.rotorTurnovers);
      console.log("Rotor Rotation Counts: ", this.rotorRotationCounts);
    },
    async onSettingsChange() {
      console.log(this.rotorVariants);
      const length = Object.keys(this.initialRotorsettings).length;
      for (let i = 0; i < length; i++) {
        this.rotors[i].current = this.initialRotorsettings[i + 1];
        this.rotors[i].next = String.fromCharCode(((this.initialRotorsettings[i + 1].charCodeAt(0) - 65 + 1) % 26) + 65);
        this.rotors[i].prev = String.fromCharCode(((this.initialRotorsettings[i + 1].charCodeAt(0) - 65 + 25) % 26) + 65);
      }
      await this.getRotations();
    },

  },
  created() {
    const initialRotorCount = 3; // Anzahl der anfänglichen Rotoren
    this.initializeRotors(initialRotorCount);
  },
  props: {
    newNumber: Number,
    rotorVariants: Object,
    initialRotorsettings: Object,
    enigmaVariant: String,
  },
  watch: {
    newNumber(newVal) {
      this.changeRotorCount(newVal);
    },
  },
};
</script>


<style>
.rotor_panel {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
}

.rotor {

  text-align: center;
  user-select: none;
  cursor: pointer;
  box-sizing: border-box;
  /*float: left;*/
  margin: 0px 20px;
  width: 23px;
  height: 130px;
  border: 4px solid black;
  position: relative;
  /*top: -750px;
    left: 250px;*/
  background: linear-gradient(0deg, rgba(0, 0, 0, 1) 0%, rgba(42, 42, 42, 1) 2%, rgba(245, 245, 245, 1) 28%, rgba(52, 52, 52, 1) 30%, rgba(216, 216, 216, 1) 31%, rgba(255, 255, 255, 1) 50%, rgba(212, 212, 212, 1) 67%, rgba(45, 45, 45, 1) 69%, rgba(226, 226, 226, 1) 70%, rgba(42, 42, 42, 1) 98%, rgba(0, 0, 0, 1) 100%);
}

.nextletter {
  width: 1vw;
  text-align: center;
  user-select: none;
  cursor: pointer;
  box-sizing: border-box;
  font-family: Tahoma;
  color: #222222;
  font-size: 12pt;
  padding-top: 7px;
  padding-bottom: 6px;
  text-shadow: 0px 1px #AAAAAA;
}

.currentletter {
  width: 1vw;
  text-align: center;
  user-select: none;
  cursor: pointer;
  box-sizing: border-box;
  font-family: Tahoma;
  color: #222222;
  font-size: 12pt;
  padding-top: 11px;
  padding-bottom: 6px;
  text-shadow: 0px 1px #AAAAAA;
}

.prevletter {
  width: 1vw;
  text-align: center;
  user-select: none;
  cursor: pointer;
  box-sizing: border-box;
  font-family: Tahoma;
  color: #222222;
  font-size: 12pt;
  padding-top: 11px;
  padding-bottom: 11px;
  text-shadow: 0px 1px #AAAAAA;
}
</style>