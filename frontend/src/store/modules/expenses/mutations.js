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

export const SET_EXPENSE_TO_STATE = (state, expense) => {
    state.expense = expense
}

export const CLEAR = (state) => {
    state.expense = {}
}

export const ADD_EXPENSE_TO_STATE = (state, expense) => {
    state.expense = expense
}

export const DELETE_EXPENSE = (state, id) => {
    let expenses = state.expenses = state.expenses.filter(t => id !== t.id)
    state.expenses = expenses
    // let index = state.payments.findIndex(payment => payment.id === id)
    // state.payments.splice(index, 1)
}
