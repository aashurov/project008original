<template>
    <div class="container">
        <h4>Добавить расход</h4>
        <form @submit.prevent="onSubmit" novalidate>
            <div class="row">
                <div class="col-6"><input type="number" placeholder="USD" class="form-control" v-model.number="usd">
                </div>
                <div class="col-6"><input type="number" placeholder="RUB" class="form-control" v-model.number="rub">
                </div>
            </div>
            <br>
            <div class="row">
                <div class="col">
                    <select name="customer" id="customer" class="form-select" v-model="customer">
                        <option v-for="customer in CUSTOMERS" v-bind:key="customer.id" v-bind:value="customer.id">
                            {{customer.id }} {{customer.last_name }} {{ customer.first_name }} {{ customer.phone_number
                            }}
                        </option>
                    </select>
                </div>

            </div>
            <br>
            <div class="row">
                <div class="col-3">
                        <select name="service" id="service" class="form-select" v-model="service">
                            <option v-for="service in SERVICES.slice(1)" v-bind:key="service.id" v-bind:value="service.id"> {{
                                service.name
                                }}
                            </option>
                        </select>
                </div>
                <div class="col-3" id="app-container">
                    <select name="plan" id="plan" class="form-select" v-model="plan" :disabled="service!==2">
                        <option v-for="plan in PLANS" v-bind:key="plan.id" v-bind:value="plan.id"> {{ plan.name }}
                        </option>
                    </select>
                </div>
                <div class="col-6"><input type="text" placeholder="Коментарий платежа" class="form-control"
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
                usd: null,
                rub: null,
                description: null,
                customer: null,
                service: 2,
                error: null,
                plan: 1,
                loading: false
            }
        },
        computed: {
            ...mapGetters('services', ['PLANS']),
            ...mapGetters('services', ['SERVICES']),
            ...mapGetters('customers', ['CUSTOMERS']),
            // ...mapGetters('couriers', ['COURIERS']),
            ...mapGetters('loading', ['LOADING'])
        },
        methods: {

            ...mapActions('expenses', ['ADD_EXPENSE_TO_API']),
            ...mapActions('services', ['GET_PLANS_FROM_API']),
            ...mapActions('services', ['GET_SERVICES_FROM_API']),
            ...mapActions('customers', ['GET_CUSTOMERS_FROM_API']),
            // ...mapActions('couriers', ['GET_COURIERS_FROM_API']),
            onSubmit() {
                if (!this.customer) {
                    this.error = 'Пожалуйста введите требуемые данные для платежа'
                } else {
                    if (this.service !== 2) {
                        this.plan = 8
                     }
                        // else {
                    //     this.service = 2
                    // }
                    if (this.usd === null || this.usd === '') {
                        this.usd = 0
                    }
                    if (this.rub === null || this.rub === '') {
                        this.rub = 0
                    }
                    if (this.description === null || this.description === '') {
                        this.description = '0'
                    }

                    const expense = {
                        usd: this.usd,
                        rub: this.rub,
                        customer: this.customer,
                        service: this.service,
                        plan: this.plan,
                        description: this.description
                    }
                    this.ADD_EXPENSE_TO_API(expense)
                    console.log(expense)
                    if (this.LOADING) {
                        this.MySpinner.val = this.LOADING
                        // this.loading = this.LOADING
                    }
                }
            },
        },
        async mounted() {
            this.GET_PLANS_FROM_API(),
                this.GET_SERVICES_FROM_API(),
                this.GET_CUSTOMERS_FROM_API()
        }
    }
</script>
<style scoped>

</style>