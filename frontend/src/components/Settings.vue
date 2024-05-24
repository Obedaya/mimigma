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
                        <h5 class="modal-title" id="exampleModalLabel">Einstellungen</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <table class = "table table-striped table-hover table-bordered">
                            <thead>
                                <tr>
                                    <th scope = "col">
                                        <div class="dropdown">
                                            <button class="btn btn-primary dropdown-toggle" type="button" id="dropdownMenuButton" 
                                            data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Reflektor</button>
                                            <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                                                <a class="dropdown-item" href="#" @click="selectRotor('Rotor 1')">UKW-B</a>
                                                <a class="dropdown-item" href="#" @click="selectRotor('Rotor 2')">UKW-C</a>
                                            </div>
                                        </div>
                                    </th>

                                    <th scope = "col">Rotor 1</th>
                                    <th scope = "col">Rotor 2</th>
                                    <th scope = "col">Rotor 3</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>Rotor:</td>
                                    <td>
                                        <div class="dropdown">
                                            <button class="btn btn-primary dropdown-toggle" type="button" id="dropdownRotor1" 
                                                    data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                                {{ selectedRotor1 }}
                                            </button>
                                            <div class="dropdown-menu" aria-labelledby="dropdownRotor1" style="height: auto; max-height: 100px; overflow-y: auto; width: 100%;">
                                                <a class="dropdown-item" v-for="rotor in rotorOptions" :key="'rotor1_' + rotor" @click="selectRotor1(rotor)">
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
                                            <div class="dropdown-menu" aria-labelledby="dropdownRotor2" style="height: auto; max-height: 100px; overflow-y: auto; width: 100%;">
                                                <a class="dropdown-item" v-for="rotor in rotorOptions" :key="'rotor2_' + rotor" @click="selectRotor2(rotor)">
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
                                            <div class="dropdown-menu" aria-labelledby="dropdownRotor3" style="height: auto; max-height: 100px; overflow-y: auto; width: 100%;">
                                                <a class="dropdown-item" v-for="rotor in rotorOptions" :key="'rotor3_' + rotor" @click="selectRotor3(rotor)">
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
                                            <div class="dropdown-menu" aria-labelledby="dropdownPosition1" style="height: auto; max-height: 100px; overflow-y: auto; /* top: -150%; */ width: 100%;">
                                                <a class="dropdown-item" v-for="letter in alphabetArray" :key="'position1_' + letter" @click="selectPostion1(letter)">{{ letter }}</a>
                                            </div>
                                        </div>
                                    </td>
                                    <td><div class="dropdown">
                                            <button class="btn btn-primary dropdown-toggle" type="button" id="dropdownPosition2" 
                                                data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                                {{ selectedPosition2 }}
                                            </button>
                                            <div class="dropdown-menu" aria-labelledby="dropdownPosition2" style="height: auto; max-height: 100px; overflow-y: auto; /* top: -150%; */ width: 100%;">
                                                <a class="dropdown-item" v-for="letter in alphabetArray" :key="'position2_' + letter" @click="selectPostion2(letter)">{{ letter }}</a>
                                            </div>
                                        </div>
                                    </td>
                                    <td>
                                        <div class="dropdown">
                                            <button class="btn btn-primary dropdown-toggle" type="button" id="dropdownPosition3" 
                                                data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                                {{ selectedPosition3 }}
                                            </button>
                                            <div class="dropdown-menu" aria-labelledby="dropdownPosition3" style="height: auto; max-height: 100px; overflow-y: auto; /* top: -150%; */ width: 100%;">
                                                <a class="dropdown-item" v-for="letter in alphabetArray" :key="'position3_' + letter" @click="selectPostion3(letter)">{{ letter }}</a>
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
                                            <div class="dropdown-menu" aria-labelledby="dropdownMenuButton" style="height: auto; max-height: 100px; overflow-y: auto; top: -150%; width: auto;">
                                                <a class="dropdown-item" v-for="letter in alphabetArray" :key="'ring1_' + letter" @click="selectPosition_Ring1(letter)">{{ letter }}</a>
                                            </div>
                                        </div>
                                    </td>
                                    <td>
                                        <div class="dropdown">
                                            <button class="btn btn-primary dropdown-toggle" type="button" id="dropdownRing" 
                                                data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                                {{ selectedPosition_Ring2 }}
                                            </button>
                                            <div class="dropdown-menu" aria-labelledby="dropdownRing" style="height: auto; max-height: 100px; overflow-y: auto; top: -150%; width: auto;">
                                                <a class="dropdown-item" v-for="letter in alphabetArray" :key="'ring1_' + letter" @click="selectPosition_Ring2(letter)">{{ letter }}</a>
                                            </div>
                                        </div>
                                    </td>
                                    <td>
                                        <div class="dropdown">
                                            <button class="btn btn-primary dropdown-toggle" type="button" id="dropdownRing" 
                                                data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                                {{ selectedPosition_Ring3 }}
                                            </button>
                                            <div class="dropdown-menu" aria-labelledby="dropdownRing" style="height: auto; max-height: 100px; overflow-y: auto; top: -150%; width: auto;">
                                                <a class="dropdown-item" v-for="letter in alphabet" :key="'ring1_' + letter" @click="selectPosition_Ring3(letter)">{{ letter }}</a>
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
            console.log('Ausgewählter Rotor 1:', rotor);
        },
        selectRotor2(rotor) {
            this.selectedRotor2 = rotor;
            console.log('Ausgewählter Rotor 2:', rotor);
        },
        selectRotor3(rotor) {
            this.selectedRotor3 = rotor;
            console.log('Ausgewählter Rotor 3:', rotor);
        },
        selectPosition1(position) {
            this.selectedPosition1 = position;
            console.log('Ausgewählte Ausgangsposition 1:', position);
        },
        selectPosition2(position) {
            this.selectedPosition2 = position;
            console.log('Ausgewählte Ausgangsposition 2:', position);
        },
        selectPosition3(position) {
            this.selectedPosition3 = position;
            console.log('Ausgewählte Ausgangsposition 3:', position);
        },
        selectPosition_Ring1(Ring_Position) {
            this.selectedPosition_Ring1 = Ring_Position;
            console.log('Ausgewählte Ausgangsposition 1:', Ring_Position);
        },
        selectPosition_Ring2(Ring_Position) {
            this.selectedPosition_Ring2 = Ring_Position;
            console.log('Ausgewählte Ausgangsposition 2:', Ring_Position);
        },
        selectPosition_Ring3(Ring_Position) {
            this.selectedPosition_Ring3 = Ring_Position;
            console.log('Ausgewählte Ausgangsposition 3:', Ring_Position);
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
    }
    .table-hover tbody tr:hover{
        background-color: #f5f5f5;
    }
    .modal-body{
        overflow-x: auto; 
    }
    .dropdown-menu {
    padding: 0;
    width: auto !important;
    }

    .dropdown-menu .dropdown-item {
    padding: 0.25rem 0.5rem; /* Adjust padding for narrower items */
    }

    .dropdown-toggle::after {
    margin-left: 0.25rem; /* Adjust margin to make the arrow closer to the text */
    }

    #dropdownMenuButton {
    min-width: 50px; /* Adjust the width of the button */
    }
</style>