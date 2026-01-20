import { createRouter, createWebHistory } from 'vue-router'
import NotesGeneratorView from '../views/NotesGeneratorView.vue'

const routes = [{ path: '/', component: NotesGeneratorView }]

export default createRouter({ history: createWebHistory(), routes })