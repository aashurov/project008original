import axios from 'axios'
import {csrftoken} from "../../../csrf/csrf_token";
import router from "../../../routers";

export const GET_EXPENSES_FROM_API = async ({commit}) => {
    commit('loading/on', null, {root: true})
    await axios.get('api/customerexpenseshistory/', {})
        .then((expenses) => {
            commit('SET_EXPENSES_TO_STATE', expenses.data['results'])
            commit('loading/off', null, {root: true})
            return expenses
        })
        .catch((error) => {
            console.log(error)
            return error
        })
}

export const GET_EXPENSE_FROM_API = async ({commit}, id) => {
    commit('loading/on', null, {root: true})
    await axios.get(`/api/customerexpenseshistory/${id}`, {
        method: "GET"
    })
        .then((expense) => {
            commit('SET_EXPENSE_TO_STATE', expense.data)
            commit('loading/off', null, {root: true})
            return expense
        })
        .catch((error) => {
            console.log(error)
            return error
        })

}

export const DELETE_EXPENSE_FROM_API = ({commit}, expense) => {
    let x = 0
    if (expense.usd === 0) {
        x = expense.rub
    } else {
        x = expense.usd
    }
    if (confirm("Вы действительно хотите удалить следующий платеж в размере?" + " " + x)) {
        commit('loading/on', null, {root: true})

        axios.delete(`/api/customerexpenseshistory/${expense.id}`, {
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFTOKEN': csrftoken
            }
        })
            .then(() => {
                commit('DELETE_EXPENSE', expense.id)
                commit('loading/off', null, {root: true})

            })
            .catch(error => console.log(error))
    }
}

export const ADD_EXPENSE_TO_API = async ({commit}, expense) => {
    commit('loading/on', null, {root: true})
    await axios.post('api/customerexpenseshistory/', expense, {
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFTOKEN': csrftoken
        }
    })
        .then((expense) => {
            commit('ADD_EXPENSE_TO_STATE', expense.data)
            commit('loading/off', null, {root: true})
            return expense
        })
        .then(() => router.push({name: 'listexpenses'}))
        .catch(error => console.log(error))
}

export const UPDATE_EXPENSE_IN_API = async ({commit}, expense) => {
    commit('loading/on', null, {root: true})
    await axios.put(`/api/customerexpenseshistory/${expense.id}`, expense, {
        headers: {
                'Content-Type': 'application/json',
                'X-CSRFTOKEN': csrftoken
            }
    })
        .then((expense) => {
            commit('SET_EXPENSE_TO_STATE', expense)
            commit('loading/off', null, {root: true})
            return expense
        })
        .then(() => router.push({name: 'listexpenses'}))
        .catch((error) => {
            console.log(error)
            return error
        })

}

///////

export const GET_ACCOUNTS_FROM_API = async ({commit}) => {
    commit('loading/on', null, {root: true})
    await axios.get('/api/customerexpenses/', {})
        .then((accounts) => {
            commit('SET_ACCOUNTS_TO_STATE', accounts.data['results'])
            commit('loading/off', null, {root: true})
        })
        .catch((error) => {
            console.log(error)
            return error
        })
}

export const GET_EXPENSESLIST_FROM_API = async ({commit}) => {
    commit('loading/on', null, {root: true})
    await axios.get(`/api/customerexpenseslist/`, {})
        .then((expenseslist) => {
            commit('SET_EXPENSESLIST_TO_STATE', expenseslist.data['results'])
            commit('loading/off', null, {root: true})
            return expenseslist
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


