import axios from 'axios'
// import {csrftoken} from "../../csrf/csrf_token";
// import router from "../../routers";


export const GET_CUSTOMERS_FROM_API = ({commit}) => {
    axios.get('/api/customers/')
        .then((customers) => {
            commit('SET_CUSTOMERS_TO_STATE', customers.data)
            return customers
        })
        .catch(error => console.log(error))
}
