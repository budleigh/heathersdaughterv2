import Vue from 'vue'
import Router from 'vue-router'
import App from './App.vue'
import Order from './components/Order.vue'
import Index from './components/Index.vue'

Vue.use(Router)

var router = new Router()

router.map({
    '/': {
        component: Index
    },
    '/order/': {
        component: Order
    }
})

router.beforeEach(function () {
    window.scrollTo(0, 0)
})

router.redirect({
    '*': '/'
})

router.start(App, '#app')
