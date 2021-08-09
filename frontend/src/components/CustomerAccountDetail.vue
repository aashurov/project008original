<template>
    <div class="container ">
        <div class="row" style="padding-top: 15px">
            <div class="col-sm-6">
                <h4><p class="float-start">Подробно</p></h4>
            </div>
            <!--            <div class="col-sm-6"><p class="float-end"><a @click.prevent="ShowPopUpInfoAdd"-->
            <!--                                                          class="btn btn-success btn-sm"><i-->
            <!--                    class="material-icons">add</i></a></p>-->
            <!--            </div>-->
        </div>

        <nav>
            <div class="nav nav-tabs" id="nav-tab" role="tablist">
                <button class="nav-link active" id="nav-common-tab" data-bs-toggle="tab" data-bs-target="#nav-common"
                        type="button" role="tab" aria-controls="nav-common" aria-selected="true">Общее
                </button>
                <button class="nav-link" id="nav-home-tab" data-bs-toggle="tab" data-bs-target="#nav-home"
                        type="button" role="tab" aria-controls="nav-home" aria-selected="true">Платежи
                </button>

                <button class="nav-link" id="nav-contact-tab" data-bs-toggle="tab" data-bs-target="#nav-contact"
                        type="button" role="tab" aria-controls="nav-contact" aria-selected="false">Перевозки
                </button>
                <button class="nav-link" id="nav-profile-tab" data-bs-toggle="tab" data-bs-target="#nav-profile"
                        type="button" role="tab" aria-controls="nav-profile" aria-selected="false">Расходы
                </button>
            </div>
        </nav>
        <div class="tab-content" id="nav-tabContent">
            <div class="tab-pane fade show active" id="nav-common" role="tabpanel" aria-labelledby="nav-common-tab">
                <div v-for="account in ACCOUNT" v-bind:key="account.id">
                    {{account.customer.first_name}} {{account.customer.last_name}} {{account.customer.username}}
                    <br>
                    Обшая сумма: {{account.usd}} $
                    <br>
                    Обшая сумма: {{account.rub}} &#x20bd;
                </div>
                <div v-if="EXPENSES">
                    <div v-for="expenses in EXPENSES" v-bind:key="expenses.id"><br>
                        Обшая сумма расхода: {{expenses.usd}} $
                        <br>
                        Обшая сумма расхода: {{expenses.rub}} &#x20bd;
                    </div>
                </div>
                <button class="btn btn-success btn-sm">Добавить Платеж</button>
                <button class="btn btn-primary btn-sm">Добавить Расход</button>
                <router-link class="btn btn-danger btn-sm" to="/customeraccounts">Назад с к списку расходов
                </router-link>
                <!--<button class="btn btn-danger btn-sm" >Назад с к списку расходов</button>-->

            </div>
            <div class="tab-pane fade" id="nav-home" role="tabpanel" aria-labelledby="nav-home-tab">
                <table class="example table table-striped table-hover table-sm table-responsive">
                    <thead>
                    <tr>
                        <th scope="col">#</th>
                        <th scope="col">USD</th>
                        <th scope="col">RUB</th>
                        <th scope="col">Сервис</th>
                        <th scope="col">Тариф</th>
                        <th scope="col">Курьер</th>
                        <th scope="col">Менеджер</th>
                        <th scope="col">Дата</th>
                        <th scope="col">Действие</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr v-for="(paymentlist, i) in PAYMENTLIST" v-bind:key="paymentlist.id" v-bind:i="i">
                        <td>{{i+1}}</td>
                        <td>{{paymentlist.usd}} $</td>
                        <td>{{paymentlist.rub}} &#x20bd;</td>
                        <td>{{paymentlist.service.name}}</td>
                        <td>{{paymentlist.plan.name}}</td>
                        <td>{{paymentlist.courier.first_name}} {{paymentlist.courier.last_name}}</td>
                        <td>{{paymentlist.staff.first_name}} {{paymentlist.staff.last_name}}</td>
                        <td>{{ moment(paymentlist.created_at).format("DD-MM-YYYY, HH:mm a") }}</td>
                        <td>
                            <!--                    <a @click.prevent="ShowPopUpInfo(payment.id)" class="link-style you-mat-element">-->
                            <!--                    <router-link class="link-style" :to="{name:'paymentdetail', params:{id:account.id}}">-->

                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                                 class="bi bi-eye"
                                 viewBox="0 0 16 16" style="margin-right:10px; margin-top:5px;">
                                <path d="M16 8s-3-5.5-8-5.5S0 8 0 8s3 5.5 8 5.5S16 8 16 8zM1.173 8a13.133 13.133 0 0 1 1.66-2.043C4.12 4.668 5.88 3.5 8 3.5c2.12 0 3.879 1.168 5.168 2.457A13.133 13.133 0 0 1 14.828 8c-.058.087-.122.183-.195.288-.335.48-.83 1.12-1.465 1.755C11.879 11.332 10.119 12.5 8 12.5c-2.12 0-3.879-1.168-5.168-2.457A13.134 13.134 0 0 1 1.172 8z"/>
                                <path d="M8 5.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5zM4.5 8a3.5 3.5 0 1 1 7 0 3.5 3.5 0 0 1-7 0z"/>
                            </svg>
                            <!--                    </a>-->
                            <!--                    </router-link>-->

                            <a href="">
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                                     class="bi bi-trash" viewBox="0 0 16 16" style="margin-right:10px; margin-top:5px;">
                                    <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z"/>
                                    <path fill-rule="evenodd"
                                          d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z"/>
                                </svg>
                            </a>

                            <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-printer" fill="currentColor"
                                 xmlns="http://www.w3.org/2000/svg">
                                <path d="M11 2H5a1 1 0 0 0-1 1v2H3V3a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v2h-1V3a1 1 0 0 0-1-1zm3 4H2a1 1 0 0 0-1 1v3a1 1 0 0 0 1 1h1v1H2a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v3a2 2 0 0 1-2 2h-1v-1h1a1 1 0 0 0 1-1V7a1 1 0 0 0-1-1z"/>
                                <path fill-rule="evenodd"
                                      d="M11 9H5a1 1 0 0 0-1 1v3a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1v-3a1 1 0 0 0-1-1zM5 8a2 2 0 0 0-2 2v3a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H5z"/>
                                <path d="M3 7.5a.5.5 0 1 1-1 0 .5.5 0 0 1 1 0z"/>
                            </svg>
                        </td>
                    </tr>
                    </tbody>
                </table>
                <div class="buttons">
                    <button class="btn btn-success btn-sm" v-if="showNextButton">Next</button>
                    <button class="btn btn-success btn-sm" v-if="showPreviousButton">Previous</button>
                </div>
                <Pagination/>
            </div>
            <div class="tab-pane fade" id="nav-contact" role="tabpanel" aria-labelledby="nav-contact-tab">
                <table class="example table table-striped table-hover table-sm table-responsive">
                    <thead>
                    <tr>
                        <th scope="col">#</th>
                        <th scope="col">USD</th>
                        <th scope="col">RUB</th>
                        <th scope="col">Сервис</th>
                        <th scope="col">Тариф</th>
                        <th scope="col">Менеджер</th>
                        <th scope="col">Дата</th>
                        <th scope="col">Действие</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr v-for="(expenseslist, i) in EXPENSESLIST_TO_DELIVERY" v-bind:key="expenseslist.id" v-bind:i="i">
                        <td>{{i+1}}</td>
                        <td>{{expenseslist.usd}} $</td>
                        <td>{{expenseslist.rub}} &#x20bd;</td>
                        <td>{{expenseslist.service.name}}</td>
                        <td>{{expenseslist.plan.name}}</td>
                        <td>{{expenseslist.staff.first_name}} {{expenseslist.staff.last_name}}</td>
                        <td>{{ moment(expenseslist.created_at).format("DD-MM-YYYY, HH:mm a") }}</td>
                        <td>
                            <!--                    <a @click.prevent="ShowPopUpInfo(payment.id)" class="link-style you-mat-element">-->
                            <!--                    <router-link class="link-style" :to="{name:'paymentdetail', params:{id:account.id}}">-->

                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                                 class="bi bi-eye"
                                 viewBox="0 0 16 16" style="margin-right:10px; margin-top:5px;">
                                <path d="M16 8s-3-5.5-8-5.5S0 8 0 8s3 5.5 8 5.5S16 8 16 8zM1.173 8a13.133 13.133 0 0 1 1.66-2.043C4.12 4.668 5.88 3.5 8 3.5c2.12 0 3.879 1.168 5.168 2.457A13.133 13.133 0 0 1 14.828 8c-.058.087-.122.183-.195.288-.335.48-.83 1.12-1.465 1.755C11.879 11.332 10.119 12.5 8 12.5c-2.12 0-3.879-1.168-5.168-2.457A13.134 13.134 0 0 1 1.172 8z"/>
                                <path d="M8 5.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5zM4.5 8a3.5 3.5 0 1 1 7 0 3.5 3.5 0 0 1-7 0z"/>
                            </svg>
                            <!--                    </a>-->
                            <!--                    </router-link>-->

                            <a href="">
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                                     class="bi bi-trash" viewBox="0 0 16 16" style="margin-right:10px; margin-top:5px;">
                                    <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z"/>
                                    <path fill-rule="evenodd"
                                          d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z"/>
                                </svg>
                            </a>

                            <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-printer" fill="currentColor"
                                 xmlns="http://www.w3.org/2000/svg">
                                <path d="M11 2H5a1 1 0 0 0-1 1v2H3V3a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v2h-1V3a1 1 0 0 0-1-1zm3 4H2a1 1 0 0 0-1 1v3a1 1 0 0 0 1 1h1v1H2a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v3a2 2 0 0 1-2 2h-1v-1h1a1 1 0 0 0 1-1V7a1 1 0 0 0-1-1z"/>
                                <path fill-rule="evenodd"
                                      d="M11 9H5a1 1 0 0 0-1 1v3a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1v-3a1 1 0 0 0-1-1zM5 8a2 2 0 0 0-2 2v3a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H5z"/>
                                <path d="M3 7.5a.5.5 0 1 1-1 0 .5.5 0 0 1 1 0z"/>
                            </svg>
                        </td>
                    </tr>
                    </tbody>
                </table>
                <div class="buttons">
                    <button class="btn btn-success btn-sm" v-if="showNextButton">Next</button>
                    <button class="btn btn-success btn-sm" v-if="showPreviousButton">Previous</button>
                </div>
                <Pagination/>
            </div>
            <div class="tab-pane fade" id="nav-profile" role="tabpanel" aria-labelledby="nav-profile-tab">
                <table class="example table table-striped table-hover table-sm table-responsive">
                    <thead>
                    <tr>
                        <th scope="col">#</th>
                        <th scope="col">USD</th>
                        <th scope="col">RUB</th>
                        <th scope="col">Сервис</th>
                        <!--                        <th scope="col">Тариф</th>-->
                        <th scope="col">Менеджер</th>
                        <th scope="col">Дата</th>
                        <th scope="col">Действие</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr v-for="(expenseslist, i) in EXPENSESLIST" v-bind:key="expenseslist.id" v-bind:i="i">
                        <td>{{i+1}}</td>
                        <td>{{expenseslist.usd}} $</td>
                        <td>{{expenseslist.rub}} &#x20bd;</td>
                        <td>{{expenseslist.service.name}}</td>
                        <td>{{expenseslist.staff.first_name}} {{expenseslist.staff.last_name}}</td>
                        <td>{{ moment(expenseslist.created_at).format("DD-MM-YYYY, HH:mm a") }}</td>
                        <td>
                            <!--                    <a @click.prevent="ShowPopUpInfo(payment.id)" class="link-style you-mat-element">-->
                            <!--                    <router-link class="link-style" :to="{name:'paymentdetail', params:{id:account.id}}">-->

                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                                 class="bi bi-eye"
                                 viewBox="0 0 16 16" style="margin-right:10px; margin-top:5px;">
                                <path d="M16 8s-3-5.5-8-5.5S0 8 0 8s3 5.5 8 5.5S16 8 16 8zM1.173 8a13.133 13.133 0 0 1 1.66-2.043C4.12 4.668 5.88 3.5 8 3.5c2.12 0 3.879 1.168 5.168 2.457A13.133 13.133 0 0 1 14.828 8c-.058.087-.122.183-.195.288-.335.48-.83 1.12-1.465 1.755C11.879 11.332 10.119 12.5 8 12.5c-2.12 0-3.879-1.168-5.168-2.457A13.134 13.134 0 0 1 1.172 8z"/>
                                <path d="M8 5.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5zM4.5 8a3.5 3.5 0 1 1 7 0 3.5 3.5 0 0 1-7 0z"/>
                            </svg>
                            <!--                    </a>-->
                            <!--                    </router-link>-->

                            <a href="">
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                                     class="bi bi-trash" viewBox="0 0 16 16" style="margin-right:10px; margin-top:5px;">
                                    <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z"/>
                                    <path fill-rule="evenodd"
                                          d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z"/>
                                </svg>
                            </a>

                            <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-printer" fill="currentColor"
                                 xmlns="http://www.w3.org/2000/svg">
                                <path d="M11 2H5a1 1 0 0 0-1 1v2H3V3a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v2h-1V3a1 1 0 0 0-1-1zm3 4H2a1 1 0 0 0-1 1v3a1 1 0 0 0 1 1h1v1H2a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v3a2 2 0 0 1-2 2h-1v-1h1a1 1 0 0 0 1-1V7a1 1 0 0 0-1-1z"/>
                                <path fill-rule="evenodd"
                                      d="M11 9H5a1 1 0 0 0-1 1v3a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1v-3a1 1 0 0 0-1-1zM5 8a2 2 0 0 0-2 2v3a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H5z"/>
                                <path d="M3 7.5a.5.5 0 1 1-1 0 .5.5 0 0 1 1 0z"/>
                            </svg>
                        </td>
                    </tr>
                    </tbody>
                </table>
                <div class="buttons">
                    <button class="btn btn-success btn-sm" v-if="showNextButton">Next</button>
                    <button class="btn btn-success btn-sm" v-if="showPreviousButton">Previous</button>
                </div>
                <Pagination/>
            </div>

        </div>
    </div>
</template>

<script>
    import {mapActions, mapGetters} from 'vuex'
    import Pagination from "./Pagination";
    import moment from "moment";

    export default {

        components: {Pagination},
        inject: ['MySpinner'],
        data() {
            return {
                showNextButton: false,
                showPreviousButton: false,
            }
        },
        props: {
            id: {
                type: String,
                required: true,
            }
        },
        created: function () {
            this.moment = moment;
        },
        computed: {
            ...mapGetters('payments', ['PAYMENTLIST', 'EXPENSESLIST', 'EXPENSESLIST_TO_DELIVERY', 'ACCOUNT', 'EXPENSES']),
            ...mapGetters("loading", ["LOADING"]),

        },

        methods: {
            ...mapActions('payments', ['GET_PAYMENTLIST_FROM_API', 'GET_EXPENSESLIST_FROM_API', 'GET_EXPENSESLIST_TO_DELIVERY_FROM_API', 'GET_ACCOUNT_FROM_API', 'GET_EXPENSES_FROM_API']),
            showPrevious() {
                if (this.PAYMENTLIST['count']) {
                    this.showNextButton = true
                }
                if (this.PAYMENTLIST['count']) {
                    this.showPreviousButton = true
                }
                this.GET_PAYMENTLIST_FROM_API(this.id)
                this.GET_EXPENSESLIST_FROM_API(this.id)
                this.GET_EXPENSESLIST_TO_DELIVERY_FROM_API(this.id)
                this.GET_ACCOUNT_FROM_API(this.id)
                this.GET_EXPENSES_FROM_API(this.id)

                if (this.LOADING) {
                    this.MySpinner.val = this.LOADING
                }
            },

        },

        mounted() {
            this.showPrevious()
            // setTimeout(() => {
            //     this.showPrevious()
            //     this.GET_PAYMENTS_FROM_API()
            // }, 100);
        }
    }
</script>

<style scoped>
    .you-mat-element {
        cursor: pointer;
    }

    h4 {
        padding-top: 20px;
        padding-bottom: 10px;
    }

    .table-responsive {
        font-size: 14px !important;
    }

</style>