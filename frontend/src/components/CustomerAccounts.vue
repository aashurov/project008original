<template>
    <div class="container ">
        <div class="row" style="padding-top: 15px">
            <div class="col-sm-6">
                <h4><p class="float-start">Счета клиентов</p></h4>
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
            <tr v-for="(account, i) in ACCOUNTS" v-bind:key="account.id" v-bind:i="i">
                <td>{{i+1}}</td>
                <td> {{account.customer.last_name}} {{account.customer.first_name}}</td>
                <td>{{account.customer.phone_number}}</td>
                <td>{{account.usd}} $</td>
                <td>{{account.rub}} &#x20bd;</td>
                <td>
<!--                                        <a @click.prevent="ShowPopUpInfo(payment.id)" class="link-style you-mat-element">-->
                    <router-link class="link-style" :to="{name:'customeraccountdetail', params:{id:account.customer.id}}">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                             class="bi bi-eye"
                             viewBox="0 0 16 16" style="margin-right:10px; margin-top:5px;">
                            <path d="M16 8s-3-5.5-8-5.5S0 8 0 8s3 5.5 8 5.5S16 8 16 8zM1.173 8a13.133 13.133 0 0 1 1.66-2.043C4.12 4.668 5.88 3.5 8 3.5c2.12 0 3.879 1.168 5.168 2.457A13.133 13.133 0 0 1 14.828 8c-.058.087-.122.183-.195.288-.335.48-.83 1.12-1.465 1.755C11.879 11.332 10.119 12.5 8 12.5c-2.12 0-3.879-1.168-5.168-2.457A13.134 13.134 0 0 1 1.172 8z"/>
                            <path d="M8 5.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5zM4.5 8a3.5 3.5 0 1 1 7 0 3.5 3.5 0 0 1-7 0z"/>
                        </svg>
                        <!--                    </a>-->
                    </router-link>

                    <a href="" >
<!--                        <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-cash" fill="currentColor" xmlns="http://www.w3.org/2000/svg">-->
<!--  <path fill-rule="evenodd" d="M15 4H1v8h14V4zM1 3a1 1 0 0 0-1 1v8a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1V4a1 1 0 0 0-1-1H1z"/>-->
<!--  <path d="M13 4a2 2 0 0 0 2 2V4h-2zM3 4a2 2 0 0 1-2 2V4h2zm10 8a2 2 0 0 1 2-2v2h-2zM3 12a2 2 0 0 0-2-2v2h2zm7-4a2 2 0 1 1-4 0 2 2 0 0 1 4 0z"/>-->
<!--</svg>-->
<!--                        <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-cash-stack" fill="currentColor" xmlns="http://www.w3.org/2000/svg">-->
<!--  <path d="M14 3H1a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1h-1z"/>-->
<!--  <path fill-rule="evenodd" d="M15 5H1v8h14V5zM1 4a1 1 0 0 0-1 1v8a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1V5a1 1 0 0 0-1-1H1z"/>-->
<!--  <path d="M13 5a2 2 0 0 0 2 2V5h-2zM3 5a2 2 0 0 1-2 2V5h2zm10 8a2 2 0 0 1 2-2v2h-2zM3 13a2 2 0 0 0-2-2v2h2zm7-4a2 2 0 1 1-4 0 2 2 0 0 1 4 0z"/>-->
<!--</svg>-->
<!--                        <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-plus" fill="currentColor" xmlns="http://www.w3.org/2000/svg">-->
<!--  <path fill-rule="evenodd" d="M8 3.5a.5.5 0 0 1 .5.5v4a.5.5 0 0 1-.5.5H4a.5.5 0 0 1 0-1h3.5V4a.5.5 0 0 1 .5-.5z"/>-->
<!--  <path fill-rule="evenodd" d="M7.5 8a.5.5 0 0 1 .5-.5h4a.5.5 0 0 1 0 1H8.5V12a.5.5 0 0 1-1 0V8z"/>-->
<!--</svg>-->

                        <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-plus-circle" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
  <path fill-rule="evenodd" d="M8 3.5a.5.5 0 0 1 .5.5v4a.5.5 0 0 1-.5.5H4a.5.5 0 0 1 0-1h3.5V4a.5.5 0 0 1 .5-.5z"/>
  <path fill-rule="evenodd" d="M7.5 8a.5.5 0 0 1 .5-.5h4a.5.5 0 0 1 0 1H8.5V12a.5.5 0 0 1-1 0V8z"/>
  <path fill-rule="evenodd" d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/>
</svg>

<!--<svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-plus-square" fill="currentColor" xmlns="http://www.w3.org/2000/svg">-->
<!--  <path fill-rule="evenodd" d="M8 3.5a.5.5 0 0 1 .5.5v4a.5.5 0 0 1-.5.5H4a.5.5 0 0 1 0-1h3.5V4a.5.5 0 0 1 .5-.5z"/>-->
<!--  <path fill-rule="evenodd" d="M7.5 8a.5.5 0 0 1 .5-.5h4a.5.5 0 0 1 0 1H8.5V12a.5.5 0 0 1-1 0V8z"/>-->
<!--  <path fill-rule="evenodd" d="M14 1H2a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1zM2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z"/>-->
<!--</svg>-->

<!--                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"-->
<!--                             class="bi bi-trash" viewBox="0 0 16 16" style="margin-right:10px; margin-top:5px;">-->
<!--                            <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z"/>-->
<!--                            <path fill-rule="evenodd"-->
<!--                                  d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z"/>-->
<!--                        </svg>-->
                    </a>

<!--                    <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-printer" fill="currentColor"-->
<!--                         xmlns="http://www.w3.org/2000/svg">-->
<!--                        <path d="M11 2H5a1 1 0 0 0-1 1v2H3V3a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v2h-1V3a1 1 0 0 0-1-1zm3 4H2a1 1 0 0 0-1 1v3a1 1 0 0 0 1 1h1v1H2a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v3a2 2 0 0 1-2 2h-1v-1h1a1 1 0 0 0 1-1V7a1 1 0 0 0-1-1z"/>-->
<!--                        <path fill-rule="evenodd"-->
<!--                              d="M11 9H5a1 1 0 0 0-1 1v3a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1v-3a1 1 0 0 0-1-1zM5 8a2 2 0 0 0-2 2v3a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H5z"/>-->
<!--                        <path d="M3 7.5a.5.5 0 1 1-1 0 .5.5 0 0 1 1 0z"/>-->
<!--                    </svg>-->

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
            ...mapGetters('payments', ['ACCOUNTS']),
            ...mapGetters("loading", ["LOADING"])
        },

        methods: {
            ...mapActions('payments', ['GET_ACCOUNTS_FROM_API']),
            showPrevious() {
                if (this.ACCOUNTS['count']) {
                    this.showNextButton = true
                }
                if (this.ACCOUNTS['count']) {
                    this.showPreviousButton = true
                }
                this.GET_ACCOUNTS_FROM_API()
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