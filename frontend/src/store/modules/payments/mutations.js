export const SET_PAYMENTS_TO_STATE = (state, payments) => {
    state.payments = payments
}

export const SET_PAYMENT_TO_STATE = (state, payment) => {
    state.payment = payment
}

export const SET_PAYMENTLIST_TO_STATE = (state, paymentlist) => {
    state.paymentlist = paymentlist
}

export const SET_EXPENSESLIST_TO_STATE = (state, expenseslist) => {
    state.expenseslist = expenseslist
}

export const SET_EXPENSESLIST_TO_DELIVERY_TO_STATE = (state, expenseslist_to_delivery) => {
    state.expenseslist_to_delivery = expenseslist_to_delivery
}

export const SET_ACCOUNT_TO_STATE = (state, account) => {
    state.account = account
}
export const SET_EXPENSES_TO_STATE = (state, expenses) => {
    state.expenses = expenses
}
// export const SET_PAYYMENT_TO_STATE = (state, payment) => {
//     state.payyment = payment
// }

export const CLEAR = (state) => {
    state.payment = {}
}

export const ADD_PAYMENT_TO_STATE = (state, payment) => {
    state.payment = payment
}

export const DELETE_PAYMENT = (state, id) => {
    let payments = state.payments = state.payments.filter(t => id !== t.id)
    state.payments = payments
    // let index = state.payments.findIndex(payment => payment.id === id)
    // state.payments.splice(index, 1)
}

export const SET_ACCOUNTS_TO_STATE = (state, accounts) => {
    state.accounts = accounts
}