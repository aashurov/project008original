import {createRouter, createWebHistory} from 'vue-router'
import CustomerExpenses from "./components/CustomerExpenses";
import AddExpenses from "./components/AddExpenses";
// import ListExpenses from "./components/ListExpenses";
import CustomerAccounts from "./components/CustomerAccounts";

const routes = [
    {
        path: '/:pathMatch(.*)*',
        name: "notfound",
        component: () => import('./components/404'),
    },
    {
        path: '/',
        name: "home",
        component: () => import('./components/Home'),
    },
    {
        path: '/listpayments',
        name: "listpayments",
        component: () => import('./components/ListPayments')
    },
    {
        path: '/paymentdetail/:id',
        name: "paymentdetail",
        component: () => import('./components/PaymentDetail'),
        props: true,
    },
    {
        path: '/paymentedit/:id',
        name: "paymentedit",
        component: () => import('./components/EditPayment'),
        props: true,
    },
    {
        path: '/addpayment',
        name: "addpayment",
        component: () => import('./components/AddPayment'),
    },
    {
        path: '/accounts',
        name: "accounts",
        component: () => import('./components/AddPayment'),
    },
    {
        path: '/listusers',
        name: "listusers",
        component: () => import('./components/ListUsers'),
    },
    {
        path: '/adduser',
        name: "adduser",
        component: () => import('./components/AddUser'),
    },
    {
        path: '/useredit/:id',
        name: "useredit",
        component: () => import('./components/EditUser'),
        props: true
    },
    {
        path: '/userdetail/:id',
        name: "userdetail",
        component: () => import('./components/DetailUser'),
        props: true
    },
    {
        path: '/customeraccounts',
        name: "customeraccounts",
        component: CustomerAccounts,
    },
    {
        path: '/customeraccountdetail/:id',
        name: "customeraccountdetail",
        component: () => import('./components/CustomerAccountDetail'),
        props: true
        // component: CustomerAccountDetail,
    },
    {
        path: '/addexpenses',
        name: "addaccounts",
        component: AddExpenses,
    },
    {
        path: '/listexpenses',
        name: "listexpenses",
        component: () => import('./components/ListExpenses'),
    },
     {
        path: '/expensedetail/:id',
        name: "expensedetail",
        component: () => import('./components/ExpenseDetail'),
        props: true,
    },
    {
        path: '/expenseedit/:id',
        name: "expenseedit",
        component: () => import('./components/EditExpense'),
        props: true,
    },
    {
        path: '/customerexpenses',
        name: "customerexpenses",
        component: CustomerExpenses,
    },

]
const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router;