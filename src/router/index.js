import { createRouter, createWebHistory } from 'vue-router'

import loginPage from '../components/login.vue'
import cadastroPage from '../components/cadastroUsuario.vue'
import cadastrarMedicos from '../components/cadastroMedico.vue'
import cadastroUsuarioMais from '../components/cadastroUsuarioMais.vue'
import homePage from '../components/home.vue'
import funcionalidadesPage from '../components/funcionalidades.vue'
import agendarConsulta from '../components/agendarConsulta.vue'
import agPasso2 from '../components/agPasso2.vue'

const routes = [
  {
    path: '/',
    name: 'homePage',
    component: homePage
  },
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
  },
  {
    path: '/cadastroUsuarioMais',
    name: 'cadastroUsuarioMais',
    component: cadastroUsuarioMais
  },
  {
    path: '/funcionalidadesPage',
    name: 'funcionalidadesPage',
    component: funcionalidadesPage
  },
  {
    path: '/agendarConsulta',
    name: 'agendarConsulta',
    component: agendarConsulta
  },
  {
    path: '/agPasso2',
    name: 'agPasso2',
    component: agPasso2
  }  
]

const router = createRouter({
  history: createWebHistory(),
  routes
})
export default router