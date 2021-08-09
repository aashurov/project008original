<template>
    <div class="container">
        <h4>Редактировать платеж</h4>
        <form @submit.prevent="updatePayment" novalidate>
            <div class="row">
                <div class="col-6"><input type="number" placeholder="USD" class="form-control" v-model.number="PAYMENT.usd">
                </div>
                <div class="col-6"><input type="number" placeholder="RUB" class="form-control" v-model.number="PAYMENT.rub">
                </div>
            </div>
            <br>
            <div class="row">
                <div class="col">
                    <select name="customer" id="customer" class="form-select" v-model="PAYMENT.customer.id" v-if="PAYMENT.customer">
                        <option v-for="customer in CUSTOMERS" v-bind:key="customer.id" v-bind:value="customer.id">
                            {{customer.last_name }} {{ customer.first_name }} {{ customer.phone_number }}
                        </option>
                    </select>
                </div>
                <div class="col">
                    <select name="courier" id="courier" class="form-select" v-model="PAYMENT.courier.id"
                            v-if="PAYMENT.courier">
                        <option v-for="courier in COURIERS" v-bind:key="courier.id" v-bind:value="courier.id">
                            {{courier.last_name }} {{ courier.first_name }} {{ courier.phone_number }}
                        </option>
                    </select>
                </div>
            </div>
            <br>
            <div class="row">
                <div class="col-3" id="app-containerr" v-if="PAYMENT.service">
                    <select name="service" id="service" class="form-select" v-model="PAYMENT.service.id">
                        <option v-for="service in SERVICES" v-bind:key="service.id" v-bind:value="service.id" :selected="PAYMENT.service.id"> {{service.name}}
                        </option>
                    </select>
                </div>
                <div class="col-3 " id="app-container" v-if="PAYMENT.plan">
                    <select name="plan" id="plan" class="form-select" v-model="PAYMENT.plan.id" :disabled="PAYMENT.service.id!==2" :selected="PAYMENT.plan.id">
                        <option v-for="plan in PLANS" v-bind:key="plan.id" v-bind:value="plan.id" v-bind:selected="PAYMENT.plan"> {{ plan.name }}
                        </option>
                    </select>
                </div>
                <div class="col-6"><input type="text" placeholder="Коментарий платежа" class="form-control" v-model="PAYMENT.description"></div>
            </div>
            <div class="row">
                <div class="col">
                    <button class="btn btn-success btn-sm" style="margin-top: 10px">Сохранить</button>
                </div>
                <div class="col">
                    <router-link class="btn btn-success btn-sm" to="/listpayments">Назад</router-link>
                </div>
            </div>
        </form>
        <div v-if="PAYMENT.error" class="alert alert-warning alert-dismissable fade show mt-5" role="alert">
            <strong>{{PAYMENT.error}}</strong></div>
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
        computed: {
            ...mapGetters('services', ['PLANS']),
            ...mapGetters('services', ['SERVICES']),
            ...mapGetters('customers', ['CUSTOMERS']),
            ...mapGetters('couriers', ['COURIERS']),
            ...mapGetters('payments', ['PAYMENT']),
            ...mapGetters('loading', ['LOADING'])
        },
        methods: {
            ...mapActions('services', ['GET_PLANS_FROM_API']),
            ...mapActions('services', ['GET_SERVICES_FROM_API']),
            ...mapActions('couriers', ['GET_COURIERS_FROM_API']),
            ...mapActions('customers', ['GET_CUSTOMERS_FROM_API']),
            ...mapActions('payments', ['UPDATE_PAYMENT_IN_API', 'GET_PAYMENT_FROM_API']),

            updatePayment() {
                if (!this.PAYMENT.customer.id) {
                    this.error = 'Пожалуйста введите требуемые данные для платежа'
                } else {
                    if (this.PAYMENT.service !== 2) {
                        this.PAYMENT.plan.id = 8
                    }
                    if (this.PAYMENT.usd === null || this.PAYMENT.usd === '') {
                        this.PAYMENT.usd = 0
                    }
                    if (this.PAYMENT.rub === null || this.PAYMENT.rub === '') {
                        this.PAYMENT.rub = 0
                    }
                    if (this.description === null || this.description === '') {
                        this.description = '0'
                    }

                    const payment = {
                        id: this.id,
                        usd: this.PAYMENT.usd,
                        rub: this.PAYMENT.rub,
                        customer: this.PAYMENT.customer.id,
                        courier: this.PAYMENT.courier.id,
                        service: this.PAYMENT.service.id,
                        plan: this.PAYMENT.plan.id,
                        description: this.PAYMENT.description
                    }
                    this.UPDATE_PAYMENT_IN_API(payment)
                    if (this.LOADING) {
                        this.MySpinner.val = this.LOADING
                    }
                }
            },

        },

        async mounted() {
             this.GET_PLANS_FROM_API()
                this.GET_SERVICES_FROM_API()
                this.GET_CUSTOMERS_FROM_API()
                this.GET_COURIERS_FROM_API()
                this.GET_PAYMENT_FROM_API(this.id)
        }
    }
</script>
<style scoped>

</style>