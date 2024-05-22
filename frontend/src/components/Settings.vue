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
                                            <button class="btn btn-primary dropdown-toggle" type="button" id="dropdownMenuButton" 
                                            data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">I</button>
                                            <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                                                <a class="dropdown-item" href="#" @click="selectRotor('Rotor 1.1')">I</a>
                                                <a class="dropdown-item" href="#" @click="selectRotor('Rotor 1.2')">II</a>
                                                <a class="dropdown-item" href="#" @click="selectRotor('Rotor 1.3')">III</a>
                                                <a class="dropdown-item" href="#" @click="selectRotor('Rotor 1.4')">IV</a>
                                                <a class="dropdown-item" href="#" @click="selectRotor('Rotor 1.5')">V</a>
                                            </div>
                                        </div>
                                    </td>
                                    <td>
                                        <div class="dropdown">
                                            <button class="btn btn-primary dropdown-toggle" type="button" id="dropdownMenuButton" 
                                            data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">I</button>
                                            <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                                                <a class="dropdown-item" href="#" @click="selectRotor('Rotor 2.1')">I</a>
                                                <a class="dropdown-item" href="#" @click="selectRotor('Rotor 2.2')">II</a>
                                                <a class="dropdown-item" href="#" @click="selectRotor('Rotor 2.3')">III</a>
                                                <a class="dropdown-item" href="#" @click="selectRotor('Rotor 2.4')">IV</a>
                                                <a class="dropdown-item" href="#" @click="selectRotor('Rotor 2.5')">V</a>
                                            </div>
                                        </div>
                                    </td>
                                    <td>
                                        <div class="dropdown">
                                            <button class="btn btn-primary dropdown-toggle" type="button" id="dropdownMenuButton" 
                                            data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">I</button>
                                            <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                                                <a class="dropdown-item" href="#" @click="selectRotor('Rotor 3.1')">I</a>
                                                <a class="dropdown-item" href="#" @click="selectRotor('Rotor 3.2')">II</a>
                                                <a class="dropdown-item" href="#" @click="selectRotor('Rotor 3.3')">III</a>
                                                <a class="dropdown-item" href="#" @click="selectRotor('Rotor 3.4')">IV</a>
                                                <a class="dropdown-item" href="#" @click="selectRotor('Rotor 3.5')">V</a>
                                            </div>
                                        </div>
                                    </td>
                                </tr>
                                <tr>
                                    <td>Ausgangsposition:</td>
                                    <td>
                                        <div class="dropdown">
                                            <button class="btn btn-primary dropdown-toggle" type="button" id="dropdownMenuButton" 
                                                data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false" style="font-size: smaller;">
                                                {{ selectedPosition }}
                                            </button>
                                            <div class="dropdown-menu" aria-labelledby="dropdownMenuButton" style="height: auto; max-height: 100px; overflow-y: auto; top: -150%; width: auto;">
                                                <a class="dropdown-item" v-for="letter in alphabet" :key="letter" @click="selectPostion(letter)">{{ letter }}</a>
                                            </div>
                                        </div>
                                    </td>
                                    <td><div class="dropdown">
                                            <button class="btn btn-primary dropdown-toggle" type="button" id="dropdownMenuButton" 
                                            data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">A</button>
                                            <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                                                <a class="dropdown-item" href="#" @click="selectRotor('Position_A_Rotor2')">A</a>
                                                
                                            </div>
                                        </div>
                                    </td>
                                    <td>
                                        <div class="dropdown">
                                            <button class="btn btn-primary dropdown-toggle" type="button" id="dropdownMenuButton" 
                                            data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">A</button>
                                            <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                                                <a class="dropdown-item" href="#" @click="selectRotor('Position_A_Rotor3')">A</a>
                                                
                                            </div>
                                        </div>
                                    </td>
                                </tr>
                                <tr>
                                    <td>Ringposition:</td>
                                    <td>
                                        <div class="dropdown">
                                            <button class="btn btn-primary dropdown-toggle" type="button" id="dropdownMenuButton" 
                                                data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false" style="font-size: smaller;">
                                                {{ selectedPosition }}
                                            </button>
                                            <div class="dropdown-menu" aria-labelledby="dropdownMenuButton" style="height: auto; max-height: 100px; overflow-y: auto; top: -150%; width: auto;">
                                                <a class="dropdown-item" v-for="letter in alphabet" :key="letter" @click="selectPostion(letter)">{{ letter }}</a>
                                            </div>
                                        </div>
                                    </td>
                                    <td>
                                        <div class="dropdown">
                                            <button class="btn btn-primary dropdown-toggle" type="button" id="dropdownMenuButton" 
                                                data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false" style="font-size: smaller;">
                                                {{ selectedPosition }}
                                            </button>
                                            <div class="dropdown-menu" aria-labelledby="dropdownMenuButton" style="height: auto; max-height: 100px; overflow-y: auto; top: -150%; width: auto;">
                                                <a class="dropdown-item" v-for="letter in alphabet" :key="letter" @click="selectPostion(letter)">{{ letter }}</a>
                                            </div>
                                        </div>
                                    </td>
                                    <td>
                                        <div class="dropdown">
                                            <button class="btn btn-primary dropdown-toggle" type="button" id="dropdownMenuButton" 
                                                data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false" style="font-size: smaller;">
                                                {{ selectedPosition }}
                                            </button>
                                            <div class="dropdown-menu" aria-labelledby="dropdownMenuButton" style="height: auto; max-height: 100px; overflow-y: auto; top: -150%; width: auto;">
                                                <a class="dropdown-item" v-for="letter in alphabet" :key="letter" @click="selectPostion(letter)">{{ letter }}</a>
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
            alphabet: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
            selectedPosition: 'A',
        };
    },
    methods: {
        selectPosition(position) {
            this.selectedPosition = position;
            console.log('Ausgewählte Ausgangsposition:', position);
        }
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
    
</style>