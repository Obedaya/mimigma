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
                                    <th scope = "col">Reflektor: </th>
                                    <th scope = "col">Rotor 1</th>
                                    <th scope = "col">Rotor 2</th>
                                    <th scope = "col">Rotor 3</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>Rotor</td>
                                    <td>Rotor 1</td>
                                    <td>Rotor 2</td>
                                    <td>Rotor 3</td>
                                </tr>
                                <tr>
                                    <td>Ausgangsposition</td>
                                    <td>Ausgangsposition 1</td>
                                    <td>Ausgangsposition 2</td>
                                    <td>Ausgangsposition 3</td>
                                </tr>
                            </tbody>
                        </table>
                        <!--Dropdown-Feld für die Rotoren Auswahl-->
                        <div class="popover-container">
                            <button class="btn btn-primary" data-bs-toggle="popover" data-bs-placement="top" :data-bs-content="popoverContent">
                                Rotoren auswählen
                            </button>
                        </div>
                        <div id="rotorPopoverContent" class="d-none">
                            <div>
                                <h5>Verfügbare Rotoren</h5>
                                <ul>
                                    <li v-for="rotor in rotors" :key="rotor.id" @click="selectRotor(rotor)">{{ rotor.name }}</li>
                                </ul>
                            </div>
                        </div>
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
</script>

<style>
    #SettingsModal .modal-dialog{
        color: black;
        max-width: 80%;
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