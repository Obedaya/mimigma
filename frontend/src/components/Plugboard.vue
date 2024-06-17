<template>
  <section>
    <div class="plugboard">
      <div v-for="key in keys1" :key="key" :class="['plug', getColorClass(key)]" @click="handlePlugClick(key)">{{ key }}</div>
      <div></div>
      <div v-for="key in keys2" :key="key" :class="['plug', 'shift-left', getColorClass(key)]" @click="handlePlugClick(key)">{{ key }}</div>
      <div v-for="key in keys3" :key="key" :class="['plug', getColorClass(key)]" @click="handlePlugClick(key)">{{ key }}</div>
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
      temporaryPlug: null
    };
  },
  methods: {
    handlePlugClick(key) {
      const pairIndex = this.pairs.findIndex(pair => pair.includes(key));

      if (pairIndex !== -1) {
        // Paar löschen
        const [firstPlug, secondPlug] = this.pairs.splice(pairIndex, 1)[0];
        delete this.plugColors[firstPlug];
        delete this.plugColors[secondPlug];
        if (this.temporaryPlug === firstPlug || this.temporaryPlug === secondPlug) {
          this.temporaryPlug = null;
        }
        return;
      }

      if (this.selectedPlug) {
        if (this.selectedPlug !== key && this.pairs.length < 5) {
          this.pairs.push([this.selectedPlug, key]);
          const color = this.colors[this.pairs.length - 1];
          this.plugColors[this.selectedPlug] = color;
          this.plugColors[key] = color;
          this.temporaryPlug = null;
        }
        this.selectedPlug = null;
      } else {
        if (Object.keys(this.plugColors).length < 10) {  // weniger als 5 Paare selectable
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
</style>
