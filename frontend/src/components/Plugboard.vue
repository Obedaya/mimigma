<template>

  <section v-if="showPlugboard">
    <div class="plugboard">
      <div v-for="key in keys1" :key="key" :class="['plug', getColorClass(key)]" @click="handlePlugClick(key)">{{ key }}
      </div>
      <div></div>
      <div v-for="key in keys2" :key="key" :class="['plug', 'shift-left', getColorClass(key)]"
           @click="handlePlugClick(key)">{{ key }}
      </div>
      <div v-for="key in keys3" :key="key" :class="['plug', getColorClass(key)]" @click="handlePlugClick(key)">{{ key }}
      </div>
    </div>
  </section>
  <div v-if="showAlert" class="alert alert-warning alert-dismissible fade show plugboard_alert" role="alert">
    <strong>Warnung!</strong> Sie können maximal 5 Paare erstellen.
    <button type="button" class="btn-close" @click="closeAlert" aria-label="Close"></button>
  </div>
</template>

<script>
import axios from 'axios';
import {
  useAuthStore
} from '@/stores/auth';

export default {
  data() {
    return {
      keys1: ['Q', 'W', 'E', 'R', 'T', 'Z', 'U', 'I', 'O'],
      keys2: ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K'],
      keys3: ['P', 'Y', 'X', 'C', 'V', 'B', 'N', 'M', 'L'],
      pairs: [],
      selectedPlug: null,
      colors: ['red', 'blue', 'green', 'yellow', 'purple'],
      plugColors: {},
      temporaryPlug: null,
      usedColors: [],
      showAlert: false,
      showPlugboard: true
    };
  },
  methods: {
    handlePlugClick(key) {
      console.log("Clicked plug:", key); // Debug log
      const pairIndex = this.pairs.findIndex(pair => pair.includes(key));

      if (pairIndex !== -1) {
        // Remove the pair
        console.log("Removing pair:", this.pairs[pairIndex]); // Debug log
        const [firstPlug, secondPlug] = this.pairs.splice(pairIndex, 1)[0];
        const colorToRemove = this.plugColors[firstPlug];
        delete this.plugColors[firstPlug];
        delete this.plugColors[secondPlug];
        this.usedColors = this.usedColors.filter(color => color !== colorToRemove);
        if (this.temporaryPlug === firstPlug || this.temporaryPlug === secondPlug) {
          this.temporaryPlug = null;
        }
        this.$emit('updatePlugboard', this.pairs);
        return;
      }

      if (this.selectedPlug) {
        console.log("Selected plug:", this.selectedPlug); // Debug log
        if (this.selectedPlug !== key) {
          if (this.pairs.length < 5) {
            const availableColor = this.colors.find(color => !this.usedColors.includes(color));
            console.log("Adding pair:", [this.selectedPlug, key], "with color:", availableColor); // Debug log
            this.pairs.push([this.selectedPlug, key]);
            this.plugColors[this.selectedPlug] = availableColor;
            this.plugColors[key] = availableColor;
            this.usedColors.push(availableColor);
            this.temporaryPlug = null;
            console.log("Pairs:", this.pairs); // Debug log
            this.$emit('updatePlugboard', this.pairs);
          }
        } else {
          console.log("Deselecting plug:", key); // Debug log
          this.temporaryPlug = null;
        }
        this.selectedPlug = null;
      } else {
        if (this.temporaryPlug != key) {
          if (Object.keys(this.plugColors).length < 10) { // Ensure not more than 10 plugs are selected
            console.log("Temporarily selecting plug:", key); // Debug log
            this.selectedPlug = key;
            this.temporaryPlug = key;
          } else {
            console.log("Max pairs reached, showing alert."); // Debug log
            this.showAlert = true;
          }
        }
      }
    },
    getColorClass(key) {
      if (this.temporaryPlug === key) {
        return 'temporary';
      }
      return this.plugColors[key] || '';
    },
    closeAlert() {
      this.showAlert = false;
    },
    updatePlugboardInDB(reset = false) {
      if (reset) {
        this.pairs = [];
        this.plugColors = {};
        this.usedColors = [];
        this.temporaryPlug = null;
      }
      const auth = useAuthStore();
      let data = {
        user_id: auth.currentUserID,
        plugboard: this.pairs
      };
      axios.post(`/plugboard`, data)
          .then(response => {
            console.log("Received data from backend: ", response.data);
          })
          .catch(error => {
            console.error("Error while fetching data: ", error);
          });
    }
  },
};
</script>

<style>
.plugboard {
  display: grid;
  grid-template-columns: repeat(9, 1fr);
  gap: 2.5px;
  justify-content: center;
}

.plug {
  width: 35px;
  height: 35px;
  border: 1px solid #ccc;
  margin: 2.5px;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  border-radius: 25px;
}

.shift-left {
  position: relative;
  right: 50%;
}

/* Temporary color class */
.temporary {
  background-color: gray;
}

/* Dynamic color classes */
.red {
  background-color: #ff5666;
  color: #6c131c;
}

.blue {
  background-color: #00fddc;
  color: #064f46;
}

.green {
  background-color: #c7ef00;
  color: #5c6f00;
}

.yellow {
  background-color: yellow;
  color: rgb(111, 111, 0);
}

.purple {
  background-color: rgb(204, 0, 204);
  color: rgb(101, 0, 101);
}

/* Bootstrap alert styling for the close button */

.plugboard_alert {
  position: fixed;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
}
</style>