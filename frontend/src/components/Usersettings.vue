<template>
    <div class="col-6" style='display: inline-block;'>
        <!-- Button trigger modal -->
        <div data-bs-toggle="modal" data-bs-target="#UserModal" id="user-settings-btn">
            <img class="icons" src="../assets/nutzer.png">
        </div>
        <!-- Modal -->
        <div class="modal fade" id="UserModal" tabindex="-1" aria-labelledby="UserModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content modalbackground">
                    <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLabel">Benutzer</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        {{ auth.user.username }}
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" @click="logout" data-bs-dismiss="modal">Log out</button>
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="button" class="btn btn-primary" data-bs-dismiss="modal">Save changes</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { useAuthStore } from '@/stores/auth';
import { useRouter } from 'vue-router';

export default {
    setup() {
        const auth = useAuthStore();
        const router = useRouter();
        
        const logout = () => {
            auth.logout();
            console.log('User logged out');
            router.push('/');
        };

        return { auth, logout };
    }
};
</script>

<style>
#UserModal {
    color: black;
}
</style>