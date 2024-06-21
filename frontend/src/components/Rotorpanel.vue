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
import { useAuthStore } from "@/stores/auth.js";

export default {
  data() {
    return {
      rotors: [],
    };
  },
  methods: {
    initializeRotors(i) {
      // Methode zum erstmaligen Initialisieren der Rotoren
      for (let j = 0; j < i; j++) {
        this.rotors.push({
          next: 'B',
          current: 'A',
          prev: 'Z',
        });
      }
    },
    changeRotorCount(newRotorCount) {
      // Methode zum Ändern der Anzahl der Rotoren
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
    updateRotorsFromBackend() {
      // Methode zum Aktualisieren der Rotoren mit Daten aus dem Backend
      const auth = useAuthStore();
      const user_id = auth.user.id;
      axios.get(`/settings?user_id=${user_id}`)
          .then(response => {
            console.log("Data from Backend for updated key: ", response.data);
            const rotor_positions = response.data.rotor_positions;
            this.updateRotors(rotor_positions);
          })
          .catch(error => {
            console.error("Error while fetching data: ", error);
          });
    },
    sendRotorsToBackend() {
      // Methode zum Aktualisieren der Rotoren im Backend
      const auth = useAuthStore();
      const user_id = auth.user.id;
      let rotor_positions = '';
      for (let i = 0; i < this.rotors.length; i++) {
        rotor_positions += this.rotors[i].current;
      }
      axios.post(`/rotor/position?user_id=${user_id}&position=${rotor_positions}`)
          .then(response => {
            console.log("Received data from backend: ", response.data);
          })
          .catch(error => {
            console.error("Error while fetching data: ", error);
          });
    },
    updateRotors(rotor_positions) {
      // Methode zum Aktualisieren der Rotoren
      for (let i = 0; i < this.rotors.length; i++) {
        const rotor = this.rotors[i];
        const rotor_position = rotor_positions.charAt(i);
        const rotor_position_index = rotor_position.charCodeAt(0) - 65;
        rotor.next = String.fromCharCode((rotor_position_index + 1) % 26 + 65);
        rotor.current = rotor_position;
        rotor.prev = String.fromCharCode((rotor_position_index + 25) % 26 + 65);
      }
    },
    rotateRotor(rotor, direction) {
      // Methode zum Rotieren eines Rotors
      const rotorIndex = parseInt(rotor.slice(-1)) - 1;
      const rotorPosition = this.rotors[rotorIndex].current;
      const rotorPositionIndex = rotorPosition.charCodeAt(0) - 65;
      let newRotorPositionIndex;
      if (direction === 'next') {
        newRotorPositionIndex = (rotorPositionIndex + 1) % 26;
      } else if (direction === 'prev') {
        newRotorPositionIndex = (rotorPositionIndex + 25) % 26;
      } else {
        return;
      }
      this.rotors[rotorIndex].next = String.fromCharCode((newRotorPositionIndex + 1) % 26 + 65);
      this.rotors[rotorIndex].current = String.fromCharCode(newRotorPositionIndex + 65);
      this.rotors[rotorIndex].prev = String.fromCharCode((newRotorPositionIndex + 25) % 26 + 65);
      this.sendRotorsToBackend();
    },
  },
  created() {
    const initialRotorCount = 3; // Anzahl der anfänglichen Rotoren
    this.initializeRotors(initialRotorCount);
  },
  props: {
    newNumber: Number,
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
  background: rgb(60,60,60);
  background: radial-gradient(circle, rgb(60, 60, 60) 32%, rgba(0,0,0,0.5760504885547969) 100%);
  border: 1px solid rgb(204, 204, 204);  position: relative;
  /*top: -750px;
    left: 250px;*/
}

.nextletter {
  text-align: center;
  user-select: none;
  cursor: pointer;
  box-sizing: border-box;
  font-family: Tahoma;
  font-size: 12pt;
  border-bottom: 1px solid #ccc;
  color: rgb(165, 165, 165);
  padding-top: 7.5px;
  padding-bottom: 7.5px;
}

.currentletter {
  text-align: center;
  user-select: none;
  cursor: pointer;
  box-sizing: border-box;
  font-family: Tahoma;
  font-size: 12pt;
  border-bottom: 1px solid #ccc;
  padding-top: 10px;
  padding-bottom: 10px;
  color: white;
}

.prevletter {
  text-align: center;
  user-select: none;
  cursor: pointer;
  box-sizing: border-box;
  font-family: Tahoma;
  font-size: 12pt;
  color: rgb(165, 165, 165);
  padding-top: 7.5px;
  padding-bottom: 7.5px;
}
</style>