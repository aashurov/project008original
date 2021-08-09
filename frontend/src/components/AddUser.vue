<template>
    <div class="container cont">
        <h4>Добавить нового пользователя</h4>
        <form @submit.prevent="onSubmit" novalidate autocomplete="off">
            <div class="row">
                <div class="col"><input type="number" placeholder="Username" class="form-control" v-model="username">
                </div>
            </div>
            <br>
            <div class="row">
                <div class="col-6"><input autocomplete="off" type="text" placeholder="First Name" class="form-control"
                                          v-model="first_name"></div>
                <div class="col-6"><input autocomplete="off" type="text" placeholder="Last Name" class="form-control" v-model="last_name">
                </div>
            </div>
            <br>
            <div class="row">
                <div class="col-6"><input autocomplete="off" type="text" placeholder="Address" class="form-control" v-model="useraddress">
                </div>
                <div class="col-6"><select name="role" id="role" class="form-select" v-model="role">
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
                                        v-model="description"></div>
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

    export default {

        el: '#selector',
        inject: ['MySpinner'],
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
            ...mapGetters('customers', ['CUSTOMERS']),
        },
        methods: {
            ...mapActions('users', ['ADD_USER_TO_API']),
            onSubmit() {
                if (!this.username && !this.role) {
                    this.error = 'Пожалуйста введите требуемые данные для пользователя'
                } else {

                    if (this.description === null || this.description === '') {
                        this.description = '0'
                    }
                    if (this.role === null || this.role === '') {
                        this.role = 'Customer'
                    }

                    const user = {
                        username: this.username,
                        password: 'Qwertyruru20@)',
                        phone_number: this.username,
                        email: (this.last_name + '_' + this.first_name + '@gmail.com').replace(/\s+/g, '').toLowerCase(),
                        address: this.useraddress,
                        last_name: this.last_name,
                        first_name: this.first_name,
                        role: this.role,
                        description: this.description
                    }
                    this.ADD_USER_TO_API(user)

                    if (this.LOADING) {
                        this.MySpinner.val = this.LOADING
                    }
                }
            },
        }

    }
</script>
<style scoped>
    .cont {
        width: 600px;
    }
</style>