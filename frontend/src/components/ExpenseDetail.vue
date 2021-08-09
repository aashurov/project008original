<template>
    <div class="container">
        ID: {{EXPENSE.id}}
        <br>
        USD: {{EXPENSE.usd}}
        <br>
        RUB: {{EXPENSE.rub}}
        <br>
        <div v-if="EXPENSE.service">
            Service: {{EXPENSE.service.name}}
        </div>
        <div v-if="EXPENSE.plan">
            Plan: {{EXPENSE.plan.name}}
        </div>
        <div v-if="EXPENSE.customer"> CUSTOMER:
            {{EXPENSE.customer.id}} {{EXPENSE.customer.last_name}} {{EXPENSE.customer.first_name}}
            {{EXPENSE.customer.phone_number}}
        </div>
        <div v-if="EXPENSE.courier"> COURIER:
            {{EXPENSE.courier.id}} {{EXPENSE.courier.last_name}} {{EXPENSE.courier.first_name}}
            {{EXPENSE.courier.phone_number}}
        </div>
        <div v-if="EXPENSE.description"> DESCRIPTION:
            {{EXPENSE.description}}
        </div>
        <div v-if="EXPENSE.staff"> Manager Name:
            {{EXPENSE.staff.last_name}} {{EXPENSE.staff.first_name}}
            {{EXPENSE.staff.phone_number}}
        </div>
        DATE: {{ moment(EXPENSE.created_at).format("DD-MM-YYYY, HH:mm a") }}
    </div>
    <div>
        <router-link class="btn btn-success btn-sm" @click.prevent="CLEAR" to="/listexpenses">Назад</router-link>
    </div>
</template>

<script>
    import {mapActions, mapGetters, mapMutations} from 'vuex'
    import moment from 'moment'

    export default {
        name: "ExpenseDetail",
        props: {
            id: {
                type: String,
                required: true,
            }
        },
        inject: ['MySpinner'],
        computed: {
            ...mapGetters('expenses', ['EXPENSE']),
            ...mapGetters("loading", ["LOADING"])
        },
        created() {
            this.moment = moment
        },
        methods: {
            ...mapActions('expenses', ['GET_EXPENSE_FROM_API']),
            ...mapMutations('payments', ['CLEAR']),
            loader() {
                if (this.LOADING) {
                    this.MySpinner.val = this.LOADING
                }
            }
        },
        mounted() {
            this.GET_EXPENSE_FROM_API(this.id)
            this.loader()
        },
    }
</script>

<style scoped>

</style>