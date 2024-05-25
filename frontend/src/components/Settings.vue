<template>
    <div class="col-6" style='display: inline-block;'>

        <!-- Button trigger modal -->
        <div data-bs-toggle="modal" data-bs-target="#SettingsModal">
            <img class="icons" src="../assets/zahnrad.png">
        </div>
        <!-- Modal -->
        <div class="modal fade" id="SettingsModal" tabindex="-1" aria-labelledby="SettingsModalLabel"
            aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content modalbackground">
                    <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLabel">Einstellungen</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <div data-mdb-input-init class="form-outline">
                            <label class="col-6" for="typeNumber">Rotorenanzahl</label>
                            <!-- der Value Wert sollte dann durch die aktuelle Anzahl der Rotoren getauscht werden!!-->
                            <input value="3" min="1" max="10" type="number" v-model="rotorCount" id="rotorCount" class="col-6" />
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button @click="sendRotorCountToBackend(rotorCount)" type="button modalSendButton" class="btn btn-primary">Save
                            changes</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from "axios";

    export default {
        methods: {

            sendRotorCountToBackend(count) {
                console.log(count);
                axios.post(`/rotor?count=${count}`)
                    .then(response => {
                        console.log("Received data from backend: ", response.data);
                        this.$emit('count', count);
                    })
                    .catch(error => {
                        console.error("Error while fetching data: ", error);
                    });
            },
        },
    };
</script>

<style>
    #SettingsModal {
        color: black;
    }
</style>