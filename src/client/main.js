import Vue from 'vue'
import Router from 'vue-router'
import App from './App.vue'
import Order from './components/Order.vue'
import Index from './components/Index.vue'
import Gallery from './components/Gallery.vue'
import About from './components/About.vue'
import Admin from './components/Admin.vue'

Vue.use(Router)

var router = new Router()

router.map({
    '/': {
        component: Index
    },
    '/order/': {
        component: Order
    },
    '/gallery/': {
        component: Gallery
    },
    '/about/': {
        component: About
    },
    '/admin/': {
        component: Admin
    }
})

router.beforeEach(function () {
    window.scrollTo(0, 0)
})

router.redirect({
    '*': '/'
})

router.start(App, '#app')
