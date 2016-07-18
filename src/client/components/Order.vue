<template>
    <div>
        {{ total }}
        {{ counts | json }}
        <ul>
            <li v-for="item in menu">
                {{ item.name }}: {{ item.price }}
                <button v-on:click="add(item)">+</button>
                <button v-on:click="remove(item)">-</button>
            </li>
        </ul>
    </div>
</template>

<script>
    export default {
        data () {
            return {
                cart: [],
                menu: [
                    {
                        name: 'Cinnamon bombs',
                        price: 2,
                        quantity: 2
                    },
                    {
                        name: 'Almond brulee',
                        price: 2,
                        quantity: 2
                    }
                ]
            }
        },

        computed: {
            total: function () {
                return this.cart.reduce(function (total, item) {
                    return total + item.price
                }, 0)
            },

            counts: function () {
                return this.cart.reduce(function (counts, item) {
                    var itemType = item.name
                    counts[itemType] = counts[itemType] ? counts[itemType] + 1 : 1
                    return counts
                }, {})
            }
        },

        methods: {
            add: function (item) {
                this.cart.push(item)
            },

            remove: function (item) {
                var itemType = item.name
                for (var x = 0; x < this.cart.length; x++) {
                    if (this.cart[x].name === itemType) {
                        this.cart.splice(x, 1)
                        break
                    }
                }
            }
        }
    }
</script>

<style lang="stylus">
</style>
