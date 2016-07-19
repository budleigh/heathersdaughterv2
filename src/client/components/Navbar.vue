<template>
    <nav>
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
                        title: 'Heather\'s Daughter Bakery',
                        url: '#/',
                        active: false
                    },
                    {
                        title: 'Order',
                        url: '#/order/',
                        active: false
                    },
                    {
                        title: 'Gallery',
                        url: '#/gallery/',
                        active: false
                    },
                    {
                        title: 'About',
                        url: '#/about/',
                        active: false
                    }
                ]
            }
        }
    }
</script>

<style lang="stylus">
</style>
