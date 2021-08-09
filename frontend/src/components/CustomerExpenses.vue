<template>
    <div class="container ">
        <div class="row" style="padding-top: 15px">
            <div class="col-sm-6">
                <h4><p class="float-start">Расходы клиентов</p></h4>
            </div>
            <!--            <div class="col-sm-6"><p class="float-end"><a @click.prevent="ShowPopUpInfoAdd"-->
            <!--                                                          class="btn btn-success btn-sm"><i-->
            <!--                    class="material-icons">add</i></a></p>-->
            <!--            </div>-->
        </div>
        <table class="example table table-striped table-hover table-sm table-responsive">
            <thead>
            <tr>
                <th scope="col">#</th>
                <th scope="col">Клиент</th>
                <th scope="col">Номер клиента</th>
                <th scope="col">USD</th>
                <th scope="col">RUB</th>
                <th scope="col">Действие</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="(expenseslist, i) in EXPENSESLIST" v-bind:key="expenseslist.id" v-bind:i="i">
                <td>{{i+1}}</td>
                <td> {{expenseslist.customer.last_name}} {{expenseslist.customer.first_name}}</td>
                <td>{{expenseslist.customer.phone_number}}</td>
                <td>{{expenseslist.usd}} $</td>
                <td>{{expenseslist.rub}} &#x20bd;</td>
                <td>
<!--                                        <a @click.prevent="ShowPopUpInfo(payment.id)" class="link-style you-mat-element">-->
                    <router-link class="link-style" :to="{name:'customeraccountdetail', params:{id:expenseslist.customer.id}}">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                             class="bi bi-eye"
                             viewBox="0 0 16 16" style="margin-right:10px; margin-top:5px;">
                            <path d="M16 8s-3-5.5-8-5.5S0 8 0 8s3 5.5 8 5.5S16 8 16 8zM1.173 8a13.133 13.133 0 0 1 1.66-2.043C4.12 4.668 5.88 3.5 8 3.5c2.12 0 3.879 1.168 5.168 2.457A13.133 13.133 0 0 1 14.828 8c-.058.087-.122.183-.195.288-.335.48-.83 1.12-1.465 1.755C11.879 11.332 10.119 12.5 8 12.5c-2.12 0-3.879-1.168-5.168-2.457A13.134 13.134 0 0 1 1.172 8z"/>
                            <path d="M8 5.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5zM4.5 8a3.5 3.5 0 1 1 7 0 3.5 3.5 0 0 1-7 0z"/>
                        </svg>
                        <!--                    </a>-->
                    </router-link>

                    <a href="" >
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
</template>

<script>
    import {mapActions, mapGetters} from 'vuex'
    import Pagination from "./Pagination";

    export default {

        components: {Pagination},
        inject: ['MySpinner'],
        data() {
            return {
                id: 0,
                showNextButton: false,
                showPreviousButton: false,
            }
        },
        computed: {
            ...mapGetters('expenses', ['EXPENSESLIST']),
            ...mapGetters("loading", ["LOADING"])
        },

        methods: {
            ...mapActions('expenses', ['GET_EXPENSESLIST_FROM_API']),
            showPrevious() {
                // if (this.ACCOUNTS['count']) {
                //     this.showNextButton = true
                // }
                // if (this.ACCOUNTS['count']) {
                //     this.showPreviousButton = true
                // }
                this.GET_EXPENSESLIST_FROM_API()
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