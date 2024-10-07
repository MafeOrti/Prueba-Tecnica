import Vue from 'vue'
import VueRouter from 'vue-router'
const HomeView = () => import('../components/views/HomeView.vue')
const ProductCreate = () => import('../components/views/ProductCreate.vue')
const NotFound = () => import('../components/shared/NotFound.vue')

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path:'/product/:idProduct?',
    name: 'product',
    component: ProductCreate
  },
  {
    // path: "*",
    path: "/:catchAll(.*)",
    name: "NotFound",
    component: NotFound,
  } 
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
