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
                                    <th scope="col">
                                        <!--Hier wird dann später der Code für Reflector stehen-->


                    <!-- <div class="dropdown">
                      <button class="btn btn-primary dropdown-toggle" type="button" :id="'dropdownReflector' + index" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        {{ /* selectedValues.Reflector || */ 'Reflector' }}
                      </button>
                      <div class="dropdown-menu" aria-labelledby="dropdownReflector">
                        <a class="dropdown-item" href="#" v-for="(value, key) in dropdownOptionsReflector" :key="key" @click="selectReflectorOption(index, value)">{{ value }}</a>
                      </div>
                    </div> -->
                  </th>
                  
                                    <th scope="col" class="text-center">Rotor 1</th>
                                    <th scope="col" class="text-center">Rotor 2</th>
                                    <th scope="col" class="text-center">Rotor 3</th>
                </tr>           
                            </thead>
                            <tbody>
                                <tr>
                                    <td>Rotor:</td>
                  <td v-for="(rotor, index) in rotorHeaders" :key="index">
                    <div class="dropdown">
                      <button class="btn btn-primary dropdown-toggle" type="button" :id="'rotor' + header" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        {{ rotor }}
                      </button>
                      <div class="dropdown-menu" :aria-labelledby="'dropdown' + header">
                        <a class="dropdown-item" href="#" v-for="(value, key) in dropdownRotorOptions" :key="key" @click="selectRotorOption(header, value)">{{ value }}</a>
                      </div>
                    </div>
                  </td>
                  </tr>
                                 
                                <tr>
                                    <td>Ausgangsposition:</td>
                                    <td v-for="(position, index) in selectedInitialPositions" :key="'position' + index">
                    <div class="dropdown">
                      <button class="btn btn-primary dropdown-toggle" type="button" :id="'dropdownPosition' + index" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        {{ position}}
                      </button>
                      <div class="dropdown-menu" :aria-labelledby="'dropdownPosition' + index" style="max-height: 100px; overflow-y: auto;">
                        <a class="dropdown-item" v-for="letter in alphabetArray_Position" :key="'position' + index + letter" @click="selectPosition(index, letter)">{{ letter }}</a>
                      </div>
                    </div>
                  </td>
                                </tr>
                                <tr>
                                    <td>Ringposition:</td>
                                    <td v-for="(ringPosition, index) in selectedRingPositions" :key="'ringPosition' + index">
                    <div class="dropdown">
                      <button class="btn btn-primary dropdown-toggle" type="button" :id="'dropdownRing' + index" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        {{ ringPosition }}
                      </button>
                      <div class="dropdown-menu" :aria-labelledby="'dropdownRing' + index" style="max-height: 100px; overflow-y: auto;">
                        <a class="dropdown-item" v-for="letter in alphabetArray_Ring" :key="'ringPosition' + index + letter" @click="selectRingPosition(index, letter)">{{ letter }}</a>
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
        rotorHeaders: {1: 'I', 2: 'I', 3:'I'}, //Titel der Dropdowns for Rotoren. Füge ein neues Element hinzu um die Spalten zu erweitern
        dropdownRotorOptions: {
        1: 'I',
        2: 'II',
        3: 'III',
        4: 'IV',
        5: 'V'
      },
      /* selectedValues: {
        Reflector: null,
        'Rotor 1': null,
        'Rotor 2': null,
        'Rotor 3': null
      } */
        selectedInitialPositions: {1 : 'A', 2 : 'A', 3 : 'A'}, // Hier werden die ausgewählten Positionen gespeichert
        alphabetArray_Position: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L','M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], // Array der verfügbaren Buchstaben
        
        selectedRingPositions: {1 : 'A', 2 : 'A', 3 : 'A'},
        alphabetArray_Ring: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L','M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'], // Array der verfügbaren Buchstaben
        
        /* dropdownOptionsReflector: {
            '1': 'UKW-A',
            '2': 'UKW-B',
            '3': 'UKW-C'
            // Weitere Optionen können hier hinzugefügt werden
        }, */
    };    
    },

    methods: {
        selectPosition(index, letter) {
            // Hier wird der ausgewählte Buchstabe an der entsprechenden Position im Array gespeichert
            this.selectedPositions[index] = letter;
        },
        selectRotorOption(index, Rotor){
            this.selectRotorOption[index] = Rotor;
        }
        /* selectReflectorOption(KeyReflector, ReflectorOption) {
            this.selectedValues[KeyReflector] = ReflectorOption;
        }, */
        
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