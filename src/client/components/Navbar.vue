<template>
    <nav class="nav">
        <ul>
            <li v-for="page in pages">
                <a href="{{ page.url }}">{{ page.title }}</a>
            </li>
        </ul>
    </nav>
</template>

<script>
    export default {
        data () {
            return {
                // Note: modifying `msg` below will not cause changes to occur with
                // hot-reload. As reloaded components preserve their initial state,
                // modifying these values will have no effect.
                pages: [
                    {
                        title: 'Home',
                        url: '#/',
                        active: false
                    },
                    {
                        title: 'Order',
                        url: '#/order/',
                        active: false
                    }
                ]
            }
        }
    }
</script>

<style lang="stylus">
    @import "../variables.styl"

    .nav
        width: 100%
        ul
            list-style: none
            li
                display: inline-block
</style>
