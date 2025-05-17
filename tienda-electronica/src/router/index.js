import { createRouter, createWebHistory } from 'vue-router'
import Ping from '../components/Ping.vue'
import Electronics from '../components/electronics.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'electronic',
      component: Electronics,
    },
    {
      path: '/ping',
      name: 'ping',
      component: Ping
    },
  ]
})


export default router