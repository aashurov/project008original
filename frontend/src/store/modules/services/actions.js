import axios from 'axios'
// import {csrftoken} from "../../csrf/csrf_token";
// import router from "../../routers";


export const GET_PLANS_FROM_API = ({commit}) => {
    axios.get('/api/plans/')
        .then((plans) => {
            commit('SET_PLANS_TO_STATE', plans.data)
            return plans
        })
        .catch(error => console.log(error))
}

export const GET_SERVICES_FROM_API = ({commit}) => {
    axios.get('/api/services/')
        .then((services) => {
            commit('SET_SERVICES_TO_STATE', services.data)
            return services
        })
        .catch(error => console.log(error))
}
