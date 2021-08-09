<template>
    <div class="container cont">
        <h4>Редактирование пользователя</h4>
        <form @submit.prevent="updateUser" novalidate>
            <div class="row">
                <div class="col"><input type="number" placeholder="Username" class="form-control" v-model="USER.username">
                </div>
            </div>
            <br>
            <div class="row">
                <div class="col-6"><input autocomplete="off" type="text" placeholder="First Name" class="form-control"
                                          v-model="USER.first_name"></div>
                <div class="col-6"><input autocomplete="off" type="text" placeholder="Last Name" class="form-control" v-model="USER.last_name">
                </div>
            </div>
            <br>
            <div class="row">
                <div class="col-6"><input autocomplete="off" type="text" placeholder="Address" class="form-control" v-model="USER.address">
                </div>
                <div class="col-6"><select name="role" id="role" class="form-select" v-model="USER.role">
                    <option value="Manager">Manager</option>
                    <option value="Senior">Senior</option>
                    <option value="Middle">Middle</option>
                    <option value="Juinor">Junior</option>
                    <option value="Courier">Courier</option>
                    <option value="Customer">Customer</option>
                </select>
                </div>
            </div>
            <br>
            <div class="row">
                <div class="col"><input autocomplete="off" type="text" placeholder="Описание пользователя" class="form-control"
                                        v-model="USER.description"></div>
            </div>
            <br>
            <div class="row">
                <div class="col">
                    <button class="btn btn-success btn-sm" style="margin-top: 10px">Сохранить</button>
                </div>
            </div>
        </form>
        <div v-if="error" class="alert alert-warning alert-dismissable fade show mt-5" role="alert">
            <strong>{{error}}</strong></div>
    </div>
</template>

<script>
    import {mapActions, mapGetters} from 'vuex'
    // import {GET_USER_FROM_API} from "../store/modules/users/actions";

    export default {

        el: '#selector',
        inject: ['MySpinner'],
         props: {
            id: {
                type: String,
                required: true
            }
        },
        data() {
            return {
                username: null,
                role: null,
                first_name: null,
                last_name: null,
                useraddress: null,
                description: null,
                error: null,
                loading: false
            }
        },
        computed: {
            ...mapGetters('loading', ['LOADING']),
            ...mapGetters('users', ['USER']),
        },
        methods: {
            ...mapActions('users', ['UPDATE_USER_IN_API', 'GET_USER_FROM_API']),
            updateUser() {
                if (!this.USER.username && !this.USER.role) {
                    this.error = 'Пожалуйста введите требуемые данные для пользователя'
                } else {

                    if (this.USER.description === null || this.USER.description === '') {
                        this.USER.description === '0'
                    }
                    if (this.USER.role === null || this.USER.role === '') {
                        this.USER.role === 'Customer'
                    }

                    const user = {
                        id: this.id,
                        username: this.USER.username,
                        password: 'Qwertyruru20@)',
                        phone_number: this.USER.username,
                        email: (this.USER.last_name + '_' + this.USER.first_name + '@gmail.com').replace(/\s+/g, '').toLowerCase(),
                        address: this.USER.useraddress,
                        last_name: this.USER.last_name,
                        first_name: this.USER.first_name,
                        role: this.USER.role,
                        description: this.USER.description
                    }
                    this.UPDATE_USER_IN_API(user)
                    if (this.LOADING) {
                        this.MySpinner.val = this.LOADING
                    }
                }
            },
        },
        async mounted() {
            this.GET_USER_FROM_API(this.id)
        }

    }
</script>
<style scoped>
    .cont {
        width: 600px;
    }
</style>