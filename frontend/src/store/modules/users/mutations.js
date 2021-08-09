export const SET_USERS_TO_STATE = (state, users) => {
    state.users = users
}

export const ADD_USER_TO_STATE = (state, user) => {
    state.user = user
}
export const SET_USER_TO_STATE = (state, user) => {
    state.user = user
}

export const CLEAR = (state) => {
    state.user = {}
}
export const DELETE_USER = (state, id) => {
    let users = state.users = state.users.filter(t => id !== t.id)
    state.users = users
    // let index = state.payments.findIndex(payment => payment.id === id)
    // state.payments.splice(index, 1)
}


