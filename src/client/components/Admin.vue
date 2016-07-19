<template>
    <div>
        <form v-on:submit.prevent="auth" v-show="!authed">
            <input type="text" v-model="username" placeholder="username"/>
            <input type="password" v-model="password" placeholder="password"/>
            <input type="submit" value="log in"/>
        </form>
        <div v-if="authed">
            <ul>
                <li v-for="order in orders">{{ order | json }}</li>
            </ul>
            <button v-on:click="logout">logout</button>
        </div>
    </div>
</template>

<script>
    import menu from '../menu.js'

    export default {
        data: function () {
            return {
                username: '',
                password: '',
                orders: [],
                sessionId: 1234,
                authed: false
            }
        },

        methods: {
            auth: function () {
                var self = this
                $.post({
                    url: '/auth/',
                    data: {
                        username: this.username,
                        password: this.password,
                        sessionId: this.sessionId
                    },
                    success: function (_) {
                        self.authed = true
                        var ping = self.ping.bind(this)
                        ping()
                        setInterval(function () {
                            ping()
                        }, 5000)
                    },
                    error: function () {
                        alert('failed to authorize')
                    }
                })
            },

            ping: function () {
                var self = this
                $.post({
                    url: '/orders/',
                    data: {
                        sessionId: this.sessionId
                    },
                    success: function (data) {
                        self.orders = JSON.parse(data)
                    }
                })
            },

            logout: function () {
                var self = this
                $.post({
                    url: '/logout/',
                    data: {
                        sessionId: this.sessionId
                    },
                    success: function (_) {
                        self.authed = false
                    },
                    error: function () {
                        console.log('couldnt logout')
                    }
                })
            }
        }
    }
</script>

<style lang="stylus">
</style>
