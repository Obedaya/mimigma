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
export default {
  data() {
    return {
      rotors: [],
      rotationCount: 0, // Zählvariable für die Anzahl der Aufrufe
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
      this.rotationCount++;
          break;
        case 'prev':
          rotor.next = rotor.current;
          rotor.current = rotor.prev;
          rotor.prev = String.fromCharCode(((rotor.prev.charCodeAt(0) - 65 + 25) % 26) + 65);
          break;
        case 'current':
          break;
      }

      // Wenn 26 Rotationen erreicht sind, rufe die nächste Rotorrotation auf
      if (this.rotationCount === 26) {
        this.rotationCount = 0; // Zurücksetzen der Zählvariable
        const prevRotorIndex = rotorIndex - 1;
        if (prevRotorIndex >= 0) {
          const prevRotorRef = 'rotor' + (prevRotorIndex + 1);
          this.rotateRotor(prevRotorRef, 'next');
        }
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
  },
  created() {
    const initialRotorCount = 3; // Anzahl der anfänglichen Rotoren
    this.initializeRotors(initialRotorCount);
  },
  props: {
    newNumber: Number,
    initialRotorsettings: Object,
  },
  watch: {
    newNumber(newVal) {
      this.changeRotorCount(newVal);
    },
    initialRotorsettings(newVal) {
      const length = Object.keys(newVal).length;
      for (let i = 0; i < length; i++) {
        this.rotors[i].current = newVal[i+1];
        this.rotors[i].next = String.fromCharCode(((newVal[i+1].charCodeAt(0) - 65 + 1) % 26) + 65);
        this.rotors[i].prev = String.fromCharCode(((newVal[i+1].charCodeAt(0) - 65 + 25) % 26) + 65);
      }

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