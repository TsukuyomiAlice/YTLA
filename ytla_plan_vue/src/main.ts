import './assets/main.css'
import '@fortawesome/fontawesome-free/css/all.min.css'

//// app ////
import { createApp } from 'vue'
import App from './App.vue'
const app = createApp(App)

import { createPinia } from 'pinia'
app.use(createPinia())

import { i18n } from '@/core/domain/area/frame/composables/usei18n.ts'
app.use(i18n)

//// registry ////
import '@/core/domain/busline/startup/registries/systemRegistry.ts'
import '@/core/domain/busline/startup/registries/featuresRegistry.ts'


//// initialize layout
import { useLayoutStore } from '@/core/domain/area/frame/services/layoutStore.ts'
const layoutStore = useLayoutStore()
layoutStore.initialize()

import { usePanelStore } from '@/core/domain/area/frame/services/panelStore.ts'
const panelStore = usePanelStore()
panelStore.initializeAllPlans().then(() => panelStore.watchPlanStatus())

app.mount('#app')
