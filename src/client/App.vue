<template>
    <div>
        <navbar></navbar>
        <router-view class="view"
                    transition="expand"
                    keep-alive>
        </router-view>
    </div>
</template>

<script>
    import Navbar from './components/Navbar.vue'

    export default {
        components: {
            Navbar
        }
    }
</script>

<style>
    body {
        font-family: Helvetica, sans-serif;
        padding: 0;
        margin: 0;
    }

    .expand-transition {
        transition: all .8s ease;
    }

    /* .expand-enter defines the starting state for entering */
    /* .expand-leave defines the ending state for leaving */
    .expand-enter, .expand-leave {
        height: 0;
        padding: 0 10px;
        opacity: 0;
    }
</style>
