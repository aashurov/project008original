<template>
    <div class="container">
        <h1>Детали о пользователе</h1>
        ID: {{USER.id}}
        <br>
        Username: {{USER.username}}
        <br>
        FIO: {{USER.first_name}} {{USER.last_name}}
        <br>
        Phone Number: {{USER.phone_number}}
        <br>
        Role: {{USER.role}}
        <br>
        Email: {{USER.email}}
        <br>
        Addres: {{USER.address}}
        <br>sa
        DATE: {{ moment(USER.date_joined).format("DD-MM-YYYY, HH:mm a") }}

    </div>
    <div>
        <router-link class="btn btn-success btn-sm" @click.prevent="CLEAR" to="/listusers">Назад</router-link>
    </div>
</template>

<script>
    import {mapActions, mapGetters, mapMutations} from 'vuex'
    import moment from 'moment'

    export default {
        name: "UserDetail",
        props: {
            id: {
                type: String,
                required: true,
            }
        },
        inject: ['MySpinner'],
        computed: {
            ...mapGetters('users', ['USER']),
            ...mapGetters("loading", ["LOADING"])
        },
        methods: {
            ...mapActions('users', ['GET_USER_FROM_API']),
            ...mapMutations('users', ['CLEAR']),
            loader() {
                if (this.LOADING) {
                    this.MySpinner.val = this.LOADING
                }
            }
        },
        created: function () {
            this.moment = moment;
        },
        mounted() {
            this.GET_USER_FROM_API(this.id)
            this.loader()
        },
    }
</script>

<style scoped>

</style>