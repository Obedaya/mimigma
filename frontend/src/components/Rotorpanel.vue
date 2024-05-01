<template>
  <section>
    <div class="rotor_panel">
      <div class="rotor" ref="rotor1">
        <div class="nextletter" @click="rotateRotor('rotor1')">B</div>
        <div class="currentletter" @click="rotateRotor('rotor1')">A</div>
        <div class="prevletter" @click="rotateRotor('rotor1')">Z</div>
      </div>

      <div class="rotor" ref="rotor2">
        <div class="nextletter" @click="rotateRotor('rotor2')">B</div>
        <div class="currentletter" @click="rotateRotor('rotor2')">A</div>
        <div class="prevletter" @click="rotateRotor('rotor2')">Z</div>
      </div>

      <div class="rotor" ref="rotor3">
        <div class="nextletter" @click="rotateRotor('rotor3')">B</div>
        <div class="currentletter" @click="rotateRotor('rotor3')">A</div>
        <div class="prevletter" @click="rotateRotor('rotor3')">Z</div>
      </div>
    </div>
  </section>
</template>

<script>
  export default {
    data() {
      return {
        alphabet: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        rotors: {
          rotor1: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
          rotor2: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
          rotor3: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
      }
      };
    },
    methods: {
      rotateRotor(rotorId) {
      const rotor = this.rotors[rotorId];
      // Drehlogik: Der erste Buchstabe wird nach hinten verschoben und der letzte Buchstabe wird zum ersten
      const rotatedRotor = rotor.substring(1) + rotor.charAt(0);
      this.rotors[rotorId] = rotatedRotor;
      
    }
    }
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