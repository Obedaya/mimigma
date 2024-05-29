<template>
    <div class="col-6" style='display: inline-block;'>

        <!-- Button trigger modal -->
        <div data-bs-toggle="modal" data-bs-target="#SettingsModal">
            <img class="icons" src="../assets/zahnrad.png">
        </div>
        <!-- Modal -->
        <div class="modal fade" id="SettingsModal" tabindex="-1" aria-labelledby="SettingsModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLabel">Settings</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <table class = "table table-striped table-hover table-bordered">
                           <!--  erste Zeile --> 
                            <thead>
                                <tr>
                                    <th scope = "col">
                                        <div class="dropdown">
                                            <button class="btn btn-primary dropdown-toggle" type="button" id="dropdownReflektor" 
                                            data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Reflektor</button>
                                            <div class="dropdown-menu" aria-labelledby="dropdownReflektor">
                                                <a class="dropdown-item" href="#" @click="selectRotor('Reflektor1')">UKW-B</a>  
                                                <a class="dropdown-item" href="#" @click="selectRotor('Reflektor2')">UKW-C</a>
                                            </div>
                                        </div>
                                    </th>

                                    <th scope="col" class="text-center">Rotor 1</th>
                                    <th scope="col" class="text-center">Rotor 2</th>
                                    <th scope="col" class="text-center">Rotor 3</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>Rotor:</td>
                                    <td>    <!-- Button Togle -->
                                        <div class="dropdown">
                                            <button class="btn btn-primary dropdown-toggle" type="button" id="dropdownRotor1" 
                                                    data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                                {{ selectedRotor1 }}
                                            </button>
                                            <!-- Liste der Rotoren -->
                                            <div class="dropdown-menu" aria-labelledby="dropdownRotor1" style="max-height: 100px; overflow-y: auto;">
                                                <a class="dropdown-item" v-for="rotor in rotorOptions" :key="'rotor1' + rotor" @click="selectRotor1(rotor)">
                                                    {{ rotor }}
                                                </a>
                                            </div>
                                        </div>
                                    </td>
                                    <td>
                                        <div class="dropdown">
                                            <button class="btn btn-primary dropdown-toggle" type="button" id="dropdownRotor2" 
                                                    data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                                {{ selectedRotor2 }}
                                            </button>
                                            <div class="dropdown-menu" aria-labelledby="dropdownRotor2" style="max-height: 100px; overflow-y: auto;">
                                                <a class="dropdown-item" v-for="rotor in rotorOptions" :key="'rotor2' + rotor" @click="selectRotor2(rotor)">
                                                    {{ rotor }}
                                                </a>
                                            </div>
                                        </div>
                                    </td>
                                    <td>
                                        <div class="dropdown">
                                            <button class="btn btn-primary dropdown-toggle" type="button" id="dropdownRotor3" 
                                                    data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                                {{ selectedRotor3 }}
                                            </button>
                                            <div class="dropdown-menu" aria-labelledby="dropdownRotor3" style="max-height: 100px; overflow-y: auto;">
                                                <a class="dropdown-item" v-for="rotor in rotorOptions" :key="'rotor3' + rotor" @click="selectRotor3(rotor)">
                                                    {{ rotor }}
                                                </a>
                                            </div>
                                        </div>
                                    </td>
                                </tr>
                                <tr>
                                    <td>Ausgangsposition:</td>
                                    <td>
                                        <div class="dropdown">
                                            <button class="btn btn-primary dropdown-toggle" type="button" id="dropdownPosition1" 
                                                data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                                {{ selectedPosition1 }}
                                            </button>
                                            <!-- Liste der Buchstaben -->
                                            <div class="dropdown-menu" aria-labelledby="dropdownPosition1" style="max-height: 100px; overflow-y: auto;">
                                                <a class="dropdown-item" v-for="letter in alphabetArray" :key="'position1' + letter" @click="selectPosition1(letter)">{{ letter }}</a>
                                            </div>
                                        </div>
                                    </td>
                                    <td><div class="dropdown">
                                            <button class="btn btn-primary dropdown-toggle" type="button" id="dropdownPosition2" 
                                                data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                                {{ selectedPosition2 }}
                                            </button>
                                            <div class="dropdown-menu" aria-labelledby="dropdownPosition2" style="max-height: 100px; overflow-y: auto;">
                                                <a class="dropdown-item" v-for="letter in alphabetArray" :key="'position2' + letter" @click="selectPosition2(letter)">{{ letter }}</a>
                                            </div>
                                        </div>
                                    </td>
                                    <td>
                                        <div class="dropdown">
                                            <button class="btn btn-primary dropdown-toggle" type="button" id="dropdownPosition3" 
                                                data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                                {{ selectedPosition3 }}
                                            </button>
                                            <div class="dropdown-menu" aria-labelledby="dropdownPosition3" style="max-height: 100px; overflow-y: auto;">
                                                <a class="dropdown-item" v-for="letter in alphabetArray" :key="'position3' + letter" @click="selectPosition3(letter)">{{ letter }}</a>
                                            </div>
                                        </div>
                                    </td>
                                </tr>
                                <tr>
                                    <td>Ringposition:</td>
                                    <td>
                                        <div class="dropdown">
                                            <button class="btn btn-primary dropdown-toggle" type="button" id="dropdownRing" 
                                                data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                                {{ selectedPosition_Ring1 }}
                                            </button>
                                            <!-- Liste der Buchstaben -->
                                            <div class="dropdown-menu" aria-labelledby="dropdownRing" style="max-height: 100px;overflow-y: auto;">
                                                <a class="dropdown-item" v-for="letter in alphabetArray" :key="'ring1' + letter" @click="selectPosition_Ring1(letter)">{{ letter }}</a>
                                            </div>
                                        </div>
                                    </td>
                                    <td>
                                        <div class="dropdown">
                                            <button class="btn btn-primary dropdown-toggle" type="button" id="dropdownRing" 
                                                data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                                {{ selectedPosition_Ring2 }}
                                            </button>
                                            <div class="dropdown-menu" aria-labelledby="dropdownRing" style="max-height: 100px; overflow-y: auto;">
                                                <a class="dropdown-item" v-for="letter in alphabetArray" :key="'ring1' + letter" @click="selectPosition_Ring2(letter)">{{ letter }}</a>
                                            </div>
                                        </div>
                                    </td>
                                    <td>
                                        <div class="dropdown">
                                            <button class="btn btn-primary dropdown-toggle" type="button" id="dropdownRing" 
                                                data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                                {{ selectedPosition_Ring3 }}
                                            </button>
                                            <div class="dropdown-menu" aria-labelledby="dropdownRing" style="max-height: 100px; overflow-y: auto;">
                                                <a class="dropdown-item" v-for="letter in alphabetArray" :key="'ring1' + letter" @click="selectPosition_Ring3(letter)">{{ letter }}</a>
                                            </div>
                                        </div>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="button" class="btn btn-primary">Save changes</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'App',
    data() {
        return {
            alphabetArray: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split(''),
            rotorOptions: ['I', 'II', 'III', 'IV', 'V'],
            selectedRotor1: 'I',
            selectedRotor2: 'I',
            selectedRotor3: 'I',
            selectedPosition1: 'A',
            selectedPosition2: 'A',
            selectedPosition3: 'A',
            selectedPosition_Ring1: 'A',
            selectedPosition_Ring2: 'A',
            selectedPosition_Ring3: 'A',
        };
    },
    methods: {
        selectRotor1(rotor) {
            this.selectedRotor1 = rotor; 
            
        },
        selectRotor2(rotor) {
            this.selectedRotor2 = rotor;
            
        },
        selectRotor3(rotor) {
            this.selectedRotor3 = rotor;
            
        },
        selectPosition1(position) {
            this.selectedPosition1 = position;
            
        },
        selectPosition2(position) {
            this.selectedPosition2 = position;
            
        },
        selectPosition3(position) {
            this.selectedPosition3 = position;
            
        },
        selectPosition_Ring1(Ring_Position) {
            this.selectedPosition_Ring1 = Ring_Position;
            
        },
        selectPosition_Ring2(Ring_Position) {
            this.selectedPosition_Ring2 = Ring_Position;
            
        },
        selectPosition_Ring3(Ring_Position) {
            this.selectedPosition_Ring3 = Ring_Position;
            
        },
    }
    
};
</script>

<style>
    #SettingsModal .modal-dialog{
        color: black;
        max-width: 50%;
        height: 80%;
    }

    .table thead th{
        background-color: #343a40;
        color: #fff;
        text-align: center;
    }
    .table-hover tbody tr:hover{
        background-color: #f5f5f5;
    }
    .modal-body{
        overflow-x: auto; 
    }

    .dropdown-toggle{
        margin: 0 auto;
        display: block;
    }
</style>