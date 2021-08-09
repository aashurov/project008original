<template>
    <div id="app">
        <Loading :start="spin.val"/>
        <Navbar/>
        <router-view/>
    </div>

</template>

<script>
    import Navbar from "./components/Navbar";
    import Loading from "./components/Loading";
    import {mapState} from 'vuex'

    export default {
        name: 'App',
        components: {
            Navbar,
            Loading
        },
        data: () => ({
            spin: {
                val: false
            },
        }),
        computed: {
            ...mapState('loading', ['loading']),
        },
        watch: {
            loading(value) {
                if (value === false) {
                    this.spin.val = value
                    console.log(value);
                }
            }
        },
        provide() {
            return {
                MySpinner: this.spin
            }
        },
    }
</script>

<style>
    #app {
        font-family: Avenir, Helvetica, Arial, sans-serif;

        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        margin-top: 0px;
    }
</style>
