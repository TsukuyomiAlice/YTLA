import './assets/main.css'
import '@fortawesome/fontawesome-free/css/all.min.css'

//// app ////
import { createApp } from 'vue'
import App from './App.vue'
const app = createApp(App)

import { createPinia } from 'pinia'
app.use(createPinia())

import { i18n } from '@/core/classic/frame/main/composables/usei18n.ts'
app.use(i18n)

//// registry ////
import '@/core/classic/busline/startup/registries/systemRegistry.ts'
import '@/core/classic/busline/startup/registries/featuresRegistry.ts'


//// initialize layout
import { useLayoutStore } from '@/core/classic/frame/main/services/layoutStore.ts'
const layoutStore = useLayoutStore()
layoutStore.initialize()

import { usePanelStore } from '@/core/classic/frame/panel/stores/panelStore.ts'
const panelStore = usePanelStore()
panelStore.initializeAllPlans().then(() => panelStore.watchPlanStatus())

app.mount('#app')
