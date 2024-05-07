<template>
  <section>
    <div class="plugboard">
      <div v-for="key in keys1" :class="{ 'plug': true }">{{ key }}</div>
      <div></div>
      <div v-for="key in keys2" :class="{ 'plug': true , 'shift-left': true }">{{ key }}</div>
      <div v-for="key in keys3" :class="{ 'plug': true }">{{ key }}</div>
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
      };
    },
    methods: {}
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
</style>