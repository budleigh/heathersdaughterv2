<template>
    <div>
        <navbar></navbar>
        <router-view class="view"
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

<style lang="stylus">
</style>
