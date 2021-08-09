<template>
    <div class="container">
        <h4>Добавить расход</h4>
        <form @submit.prevent="updateExpense" novalidate>
            <div class="row">
                <div class="col-6"><input type="number" placeholder="USD" class="form-control"
                                          v-model.number="EXPENSE.usd">
                </div>
                <div class="col-6"><input type="number" placeholder="RUB" class="form-control"
                                          v-model.number="EXPENSE.rub">
                </div>
            </div>
            <br>
            <div class="row">
                <div class="col">
                    <select name="customer" id="customer" class="form-select" v-model="EXPENSE.customer.id"
                            v-if="EXPENSE.customer">
                        <option v-for="customer in CUSTOMERS" v-bind:key="customer.id" v-bind:value="customer.id">
                            {{customer.id }} {{customer.last_name }} {{ customer.first_name }} {{ customer.phone_number
                            }}
                        </option>
                    </select>
                </div>

            </div>
            <br>
            <div class="row">
                <div class="col-3" v-if="EXPENSE.service">
                    <select name="service" id="service" class="form-select" v-model="EXPENSE.service.id">
                        <option v-for="service in SERVICES.slice(1)" v-bind:key="service.id" v-bind:value="service.id">
                            {{
                            service.name
                            }}
                        </option>
                    </select>
                </div>
                <div class="col-3" id="app-container" v-if="EXPENSE.plan">
                    <select name="plan" id="plan" class="form-select" v-model="EXPENSE.plan.id" :disabled="service!==2">
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
        props: {
            id: {
                type: String,
                required: true
            }
        },
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
            ...mapGetters('expenses', ['EXPENSE']),
            ...mapGetters('services', ['SERVICES', 'PLANS']),
            ...mapGetters('customers', ['CUSTOMERS']),
            ...mapGetters('loading', ['LOADING'])
        },
        methods: {

            ...mapActions('expenses', ['GET_EXPENSE_FROM_API', 'UPDATE_EXPENSE_IN_API']),
            ...mapActions('services', ['GET_PLANS_FROM_API']),
            ...mapActions('services', ['GET_SERVICES_FROM_API']),
            ...mapActions('customers', ['GET_CUSTOMERS_FROM_API']),
            updateExpense() {
                if (!this.EXPENSE.customer) {
                    this.EXPENSE.error === 'Пожалуйста введите требуемые данные для платежа'
                } else {
                    if (this.EXPENSE.service !== 2) {
                        this.EXPENSE.plan === 8
                    }
                    if (this.EXPENSE.usd === null || this.EXPENSE.usd === '') {
                        this.EXPENSE.usd = 0
                    }
                    if (this.EXPENSE.rub === null || this.EXPENSE.rub === '') {
                        this.EXPENSE.rub = 0
                    }
                    if (this.EXPENSE.description === null || this.EXPENSE.description === '') {
                        this.EXPENSE.description === '0'
                    }

                    const expense = {
                        id: this.id,
                        usd: this.EXPENSE.usd,
                        rub: this.EXPENSE.rub,
                        customer: this.EXPENSE.customer.id,
                        service: this.EXPENSE.service.id,
                        plan: this.EXPENSE.plan,
                        description: this.EXPENSE.description
                    }
                    this.UPDATE_EXPENSE_IN_API(expense)
                    console.log(expense)
                    if (this.LOADING) {
                        this.MySpinner.val = this.LOADING
                    }
                }
            },
        },
        async mounted() {
                this.GET_EXPENSE_FROM_API(this.id),
                this.GET_PLANS_FROM_API(),
                this.GET_SERVICES_FROM_API(),
                this.GET_CUSTOMERS_FROM_API()
        }
    }
</script>
<style scoped>

</style>