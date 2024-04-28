
<template>
  
    <header>
    <div class="rotor" id = "rotor1">
      <div class = "nextletter" id ="rotor1next">B</div>
      <div class = "currentletter" id = "rotor1current">A</div>
      <div class = "prevletter" id = "rotor1prev">Z</div>
    </div>
      
    <div class="rotor" id = "rotor2">
      <div class = "nextletter" id ="rotor1next">B</div>
      <div class = "currentletter" id = "rotor1current">A</div>
      <div class = "prevletter" id = "rotor1prev">Z</div>
    </div>
      
    <div class="rotor" id = "rotor3">
      <div class = "nextletter" id ="rotor1next">B</div>
      <div class = "currentletter" id = "rotor1current">A</div>
      <div class = "prevletter" id = "rotor1prev">Z</div>
    </div>
      
    </header>
    </template>
    
<script>
export default{
    data (){
        return {    
};
},
    methods: {}
};
    </script>
    
    <style>
    body{
      background-color: black;
    }
    .rotor {
      text-align: center;
      user-select: none;
      cursor: pointer;
      box-sizing: border-box;
      float: left;
      margin: 0px 20px;
      width: 23px;
      height: 130px;
      border: 4px solid black;
      position: relative;
      top: -750px;
      left: 250px;
      background: linear-gradient(0deg, rgba(0,0,0,1) 0%, rgba(42,42,42,1) 2%, rgba(245,245,245,1) 28%, rgba(52,52,52,1) 30%, rgba(216,216,216,1) 31%, rgba(255,255,255,1) 50%, rgba(212,212,212,1) 67%, rgba(45,45,45,1) 69%, rgba(226,226,226,1) 70%, rgba(42,42,42,1) 98%, rgba(0,0,0,1) 100%);
    }
    
    .nextletter{
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
    
    .currentletter{
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
    
    .prevletter{
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