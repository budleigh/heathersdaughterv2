<template>
    <div>
        ${{ total }}
        {{ counts | json }}
        <ul>
            <li v-for="item in menu">
                {{ item.name }}: {{ item.price }}
                <button v-on:click="add(item)">+</button>
                <button v-on:click="remove(item)">-</button>
            </li>
        </ul>
        <input type="text" v-model="orderer.name" placeholder="Your name"/>
        <input type="text" v-model="orderer.address" placeholder="Your address"/>
        <input type="text" v-model="orderer.phone" placeholder="Phone number"/>
        <textarea v-model="orderer.instructions" placeholder="Special instructions"></textarea>
        <button v-on:click="order">Order</button>
    </div>
</template>

<script>
    import $ from 'jquery'
    import menu from '../menu.js'

    export default {
        data () {
            return {
                cart: [],
                menu: menu,
                orderer: {
                    name: '',
                    address: '',
                    phone: '',
                    instructions: ''
                }
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
            },

            order: function () {
                var self = this
                $.post({
                    url: '/order/',
                    contentType: 'application/json; charset=utf-8'
                    data: JSON.stringify({
                        orderer: this.orderer,
                        order: this.counts
                        created: new Date().getDate()
                    }),
                    success: function (data) {
                        console.log('ordered successfuly!')
                        self.clear()
                    },
                    error: function () {
                        console.log('something went wrong')
                    }
                })
            },

            clear: function () {
                this.cart = []
                this.orderer = {}
            }
        }
    }
</script>

<style lang="stylus">
</style>
