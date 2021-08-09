import axios from 'axios'
import {csrftoken} from "../../../csrf/csrf_token";
import router from "../../../routers";
// import {csrftoken} from "../../csrf/csrf_token";
// import router from "../../routers";


export const GET_USERS_FROM_API = ({commit}) => {
    commit('loading/on', null, {root: true})
    axios.get('/api/users/')
        .then((users) => {
            commit('SET_USERS_TO_STATE', users.data['results'])
            commit('loading/off', null, {root: true})
            return users
        })
        .catch(error => console.log(error))
}


export const GET_USER_FROM_API = ({commit}, id) => {
    console.log(id)
    commit('loading/on', null, {root: true})
    axios.get(`/api/users/${id}/`)
        .then((user) => {
            commit('SET_USER_TO_STATE', user.data)
            commit('loading/off', null, {root: true})
            return user
        })
        .catch(error => console.log(error))
}

export const DELETE_USER_FROM_API = ({commit}, user) => {
    if (confirm("Вы действительно хотите удалить следующего пользователя?" + ' ' + user.last_name + ' ' + user.first_name)) {
        commit('loading/on', null, {root: true})
        axios.delete(`/api/users/${user.id}/`, {
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFTOKEN': csrftoken
            }
        })
            .then(() => {
                commit('DELETE_USER', user.id)
                commit('loading/off', null, {root: true})

            })
            .catch(error => console.log(error))
    }
}

export const ADD_USER_TO_API = async ({commit}, user) => {
    commit('loading/on', null, {root: true})
    await axios.post('api/usersall/', user, {
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFTOKEN': csrftoken
        }
    })
        .then((payment) => {
            commit('ADD_USER_TO_STATE', payment.data)
            commit('loading/off', null, {root: true})
            return user
        })
        .then(() => router.push({name: 'listusers'}))
        .catch(error => console.log(error))
}

export const UPDATE_USER_IN_API = async ({commit}, user) => {
    commit('loading/on', null, {root: true})
    await axios.put(`/api/users/${user.id}/`, user, {
        headers: {
                'Content-Type': 'application/json',
                'X-CSRFTOKEN': csrftoken
            }
    })
        .then((user) => {
            commit('SET_USER_TO_STATE', user)
            commit('loading/off', null, {root: true})
            return user
        })
        .then(() => router.push({name: 'listusers'}))
        .catch((error) => {
            console.log(error)
            return error
        })

}