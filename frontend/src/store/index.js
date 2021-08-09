import {createStore} from 'vuex'
import customers from './modules/customers'
import couriers from './modules/couriers'
import services from './modules/services'
import payments from './modules/payments'
import loading from './modules/loading'
import roles from './modules/roles'
import users from './modules/users'
import expenses from './modules/expenses'
export default createStore({

    modules: {
        customers,
        couriers,
        services,
        payments,
        loading,
        roles,
        users,
        expenses
    }
})

