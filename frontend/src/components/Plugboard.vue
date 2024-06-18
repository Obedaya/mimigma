<template>
  <section>
    <div class="plugboard">
      <div v-for="key in keys1" :key="key" :class="['plug', getColorClass(key)]" @click="handlePlugClick(key)">{{ key }}</div>
      <div></div>
      <div v-for="key in keys2" :key="key" :class="['plug', 'shift-left', getColorClass(key)]" @click="handlePlugClick(key)">{{ key }}</div>
      <div v-for="key in keys3" :key="key" :class="['plug', getColorClass(key)]" @click="handlePlugClick(key)">{{ key }}</div>
    </div>
    <div v-if="showAlert" class="alert alert-warning alert-dismissible fade show" role="alert">
      <strong>Alaaarrrmmmmmmm</strong> Sie können maximal 5 Paare erstellen.
      <button type="button" class="btn-close" @click="closeAlert" aria-label="Close"></button>
    </div>
  </section>
</template>

<script>
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
      showAlert: false
    };
  },
  methods: {
    handlePlugClick(key) {
      console.log("Clicked plug:", key); // Debug log
      const pairIndex = this.pairs.findIndex(pair => pair.includes(key));

      if (pairIndex !== -1) {
        // Paar wird hier gelöscht
        console.log("Removing pair:", this.pairs[pairIndex]); // Debug log
        const [firstPlug, secondPlug] = this.pairs.splice(pairIndex, 1)[0];
        const colorToRemove = this.plugColors[firstPlug];
        delete this.plugColors[firstPlug];
        delete this.plugColors[secondPlug];
        this.usedColors = this.usedColors.filter(color => color !== colorToRemove);
        if (this.temporaryPlug === firstPlug || this.temporaryPlug === secondPlug) {
          this.temporaryPlug = null;
        }
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
            console.log("Current Pair length:", this.pairs.length); // Debug log
          } else { //Warum wirst du nie ausgewählt????
            console.log("Max pairs reached, showing alert."); // Debug log
            this.showAlert = true;
          }
        }
        this.selectedPlug = null;
      } else {
        if (Object.keys(this.plugColors).length < 10) {  // weniger als 10
          console.log("Temporarily selecting plug:", key); // Debug log
          this.selectedPlug = key;
          this.temporaryPlug = key;
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
  background-color: red;
}
.blue {
  background-color: blue;
}
.green {
  background-color: green;
}
.yellow {
  background-color: yellow;
}
.purple {
  background-color: purple;
}

/* bootstrap schließbutton */
.btn-close {
  border: none;
  background: none;
}
</style>
