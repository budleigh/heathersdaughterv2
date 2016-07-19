<template>
    <div>
        <ul>
            <li v-for="image in images"><img v-bind:src="image"</li>
        </ul>
    </div>
</template>

<script>
    import menu from '../menu.js'

    export default {
        data: function () {
            return {
                menu: menu
            }
        },

        computed: {
            images: function () {
                return this.menu.reduce(function (images, item) {
                    return images.concat(item.images) 
                }, [])
            }
        }
    }
</script>

<style lang="stylus">
</style>
