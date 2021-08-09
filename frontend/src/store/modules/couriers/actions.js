import axios from 'axios'
// import {csrftoken} from "../../csrf/csrf_token";
// import router from "../../routers";


export const GET_COURIERS_FROM_API = ({commit}) => {
    axios.get('/api/couriers/')
        .then((couriers) => {
            commit('SET_COURIERS_TO_STATE', couriers.data)
            return couriers
        })
        .catch(error => console.log(error))
}
