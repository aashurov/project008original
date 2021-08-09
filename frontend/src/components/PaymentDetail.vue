<template>
    <div class="container">
        ID: {{PAYMENT.id}}
        <br>
        USD: {{PAYMENT.usd}}
        <br>
        RUB: {{PAYMENT.rub}}
        <br>
        <div v-if="PAYMENT.service">
        Service: {{PAYMENT.service.name}}
            </div>
                <div v-if="PAYMENT.plan">
        Plan: {{PAYMENT.plan.name}}
            </div>
        <div v-if="PAYMENT.customer"> CUSTOMER:
            {{PAYMENT.customer.id}} {{PAYMENT.customer.last_name}} {{PAYMENT.customer.first_name}}
            {{PAYMENT.customer.phone_number}}
        </div>
        <div v-if="PAYMENT.courier"> COURIER:
            {{PAYMENT.courier.id}} {{PAYMENT.courier.last_name}} {{PAYMENT.courier.first_name}}
            {{PAYMENT.courier.phone_number}}
        </div>
        <div v-if="PAYMENT.description"> DESCRIPTION:
            {{PAYMENT.description}}
        </div>
        <div v-if="PAYMENT.staff"> Manager Name:
            {{PAYMENT.staff.last_name}} {{PAYMENT.staff.first_name}}
            {{PAYMENT.staff.phone_number}}
        </div>
        DATE: {{ moment(PAYMENT.created_at).format("DD-MM-YYYY, HH:mm a") }}
    </div>
    <div>
        <router-link class="btn btn-success btn-sm" @click.prevent="CLEAR" to="/listpayments">Назад</router-link>
    </div>
</template>

<script>
    import {mapActions, mapGetters, mapMutations} from 'vuex'
import moment from 'moment'
    export default {
        name: "PaymentDetail",
        props: {
            id: {
                type: String,
                required: true,
            }
        },
        inject: ['MySpinner'],
        computed: {
            ...mapGetters('payments', ['PAYMENT']),
            ...mapGetters("loading", ["LOADING"])
        },
        created() {
            this.moment = moment
        },
        methods: {
            ...mapActions('payments', ['GET_PAYMENT_FROM_API']),
            ...mapMutations('payments', ['CLEAR']),
            loader() {
                if (this.LOADING) {
                    this.MySpinner.val = this.LOADING
                }
            }
        },
        mounted() {
            this.GET_PAYMENT_FROM_API(this.id)
            this.loader()
        },
    }
</script>

<style scoped>

</style>