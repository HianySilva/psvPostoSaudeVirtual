import { createRouter, createWebHistory } from 'vue-router'

import loginPage from '../components/login.vue'
import cadastroPage from '../components/cadastroUsuario.vue'
import cadastrarMedicos from '../components/cadastroMedico.vue'

const routes = [
  {
    path: '/loginPage',
    name: 'loginPage',
    component: loginPage
  },
  {
    path: '/cadastroPage',
    name: 'cadastroPage',
    component: cadastroPage
  },
  {
    path: '/cadastrarMedicos',
    name: 'cadastrarMedicos',
    component: cadastrarMedicos
  }  
]

const router = createRouter({
  history: createWebHistory(),
  routes
})
export default router