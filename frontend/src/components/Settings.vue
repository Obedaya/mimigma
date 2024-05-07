<template>
    <div class="col-6" style='display: inline-block;'>

        <!-- Button trigger modal -->
        <div data-bs-toggle="modal" data-bs-target="#SettingsModal">
            <img class="icons" src="../../zahnrad.png">
        </div>
        <!-- Modal -->
        <div class="modal fade" id="SettingsModal" tabindex="-1" aria-labelledby="SettingsModalLabel"
            aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLabel">Einstellungen</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        bingbong
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
    #SettingsModal {
        color: black;
    }
</style>