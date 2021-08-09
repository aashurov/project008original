import axios from 'axios'
import {csrftoken} from "../../../csrf/csrf_token";
import router from "../../../routers";

export const GET_PAYMENTS_FROM_API = async ({commit}) => {
    commit('loading/on', null, {root: true})
    await axios.get('api/customeraccounthistory/', {})
        .then((payments) => {
            commit('SET_PAYMENTS_TO_STATE', payments.data['results'])
            commit('loading/off', null, {root: true})
        })
        .catch((error) => {
            console.log(error)
            return error
        })
}

// export const FGET_PAYMENT_FROM_API = async ({commit}, id) => {
//
//     let URL1 = '/api/customers/'
//     let URL2 = '/api/couriers/'
//     // let URL3 = `/api/plans/`
//     // let URL4 = `/api/customeraccounthistory/${id}/`
//     let rid = id
//     console.log(rid)
//     const promise1 = axios.get(URL1);
//     const promise2 = axios.get(URL2);
//     // const promise3 = axios.get(URL3);
//     // const promise4 = axios.get(URL4);
//
//     commit('loading/on', null, {root: true})
//     Promise.all([ promise1, promise2], commit).then((values) => {
//         commit('SET_PAYYMENT_TO_STATE', values)
//         commit('loading/off', null, {root: true})
//         console.log(values);
//     });
//     // await axios.get(`/api/customeraccounthistory/${id}/`)
//     //     .then((payment) => {
//     //         commit('SET_PAYMENT_TO_STATE', payment.data)
//     //         commit('loading/off', null, {root: true})
//     //         return payment
//     //     })
//     //
//     //     .catch((error) => {
//     //         console.log(error)
//     //         return error
//     //     })
// }

export const GET_PAYMENT_FROM_API = async ({commit}, id) => {
    commit('loading/on', null, {root: true})
    await axios.get(`/api/customeraccounthistory/${id}/`, {
        method: "GET"
    })
        .then((payment) => {
            commit('SET_PAYMENT_TO_STATE', payment.data)
            commit('loading/off', null, {root: true})
            return payment
        })
        .catch((error) => {
            console.log(error)
            return error
        })

}

export const DELETE_PAYMENT_FROM_API = ({commit}, payment) => {
    let x = 0
    if (payment.usd === 0) {
        x = payment.rub
    } else {
        x = payment.usd
    }
    if (confirm("Вы действительно хотите удалить следующий платеж в размере?" + " " + x)) {
        commit('loading/on', null, {root: true})

        axios.delete(`/api/customeraccounthistory/${payment.id}/`, {
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFTOKEN': csrftoken
            }
        })
            .then(() => {
                commit('DELETE_PAYMENT', payment.id)
                commit('loading/off', null, {root: true})

            })
            .catch(error => console.log(error))
    }
}

export const ADD_PAYMENT_TO_API = async ({commit}, payment) => {
    commit('loading/on', null, {root: true})
    await axios.post('api/customeraccounthistory/', payment, {
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFTOKEN': csrftoken
        }
    })
        .then((payment) => {
            commit('ADD_PAYMENT_TO_STATE', payment.data)
            commit('loading/off', null, {root: true})
            return payment
        })
        .then(() => router.push({name: 'listpayments'}))
        .catch(error => console.log(error))
}

export const UPDATE_PAYMENT_IN_API = async ({commit}, payment) => {
    commit('loading/on', null, {root: true})
    await axios.put(`/api/customeraccounthistory/${payment.id}/`, payment, {
        headers: {
                'Content-Type': 'application/json',
                'X-CSRFTOKEN': csrftoken
            }
    })
        .then((payment) => {
            commit('SET_PAYMENT_TO_STATE', payment)
            commit('loading/off', null, {root: true})
            return payment
        })
        .then(() => router.push({name: 'listpayments'}))
        .catch((error) => {
            console.log(error)
            return error
        })

}


///////


export const GET_ACCOUNTS_FROM_API = async ({commit}) => {
    commit('loading/on', null, {root: true})
    await axios.get('/api/customeraccounts/', {})
        .then((accounts) => {
            commit('SET_ACCOUNTS_TO_STATE', accounts.data['results'])
            commit('loading/off', null, {root: true})
        })
        .catch((error) => {
            console.log(error)
            return error
        })
}

export const GET_PAYMENTLIST_FROM_API = async ({commit}, id) => {
    commit('loading/on', null, {root: true})
    await axios.get(`/api/customeraccounthistoryy/${id}/`, {})
        .then((accounts) => {
            commit('SET_PAYMENTLIST_TO_STATE', accounts.data['results'])
            commit('loading/off', null, {root: true})
        })
        .catch((error) => {
            console.log(error)
            return error
        })
}

export const GET_EXPENSESLIST_FROM_API = async ({commit}, id) => {
    commit('loading/on', null, {root: true})
    await axios.get(`/api/customerexpenseshistoryy/${id}/`, {})
        .then((accounts) => {
            commit('SET_EXPENSESLIST_TO_STATE', accounts.data['results'])
            commit('loading/off', null, {root: true})
        })
        .catch((error) => {
            console.log(error)
            return error
        })
}

export const GET_EXPENSESLIST_TO_DELIVERY_FROM_API = async ({commit}, id) => {
    commit('loading/on', null, {root: true})
    await axios.get(`/api/customerexpenseshistoryyy/${id}/`, {})
        .then((accounts) => {
            commit('SET_EXPENSESLIST_TO_DELIVERY_TO_STATE', accounts.data['results'])
            commit('loading/off', null, {root: true})
        })
        .catch((error) => {
            console.log(error)
            return error
        })
}

export const GET_ACCOUNT_FROM_API = async ({commit}, id) => {
    commit('loading/on', null, {root: true})
    await axios.get(`/api/customeraccount/${id}/`, {})
        .then((account) => {
            commit('SET_ACCOUNT_TO_STATE', account.data['results'])
            commit('loading/off', null, {root: true})
        })
        .catch((error) => {
            console.log(error)
            return error
        })
}

export const GET_EXPENSES_FROM_API = async ({commit}, id) => {
    commit('loading/on', null, {root: true})
    await axios.get(`/api/customerexpenses/${id}`, {})
        .then((expenses) => {
            commit('SET_EXPENSES_TO_STATE', expenses.data['results'])
            commit('loading/off', null, {root: true})
        })
        .catch((error) => {
            console.log(error)
            return error
        })
}