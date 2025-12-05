import './assets/main.css'
import '@fortawesome/fontawesome-free/css/all.min.css'

// app
import { createApp } from 'vue'
import App from './App.vue'
const app = createApp(App)

import { createPinia } from 'pinia'
app.use(createPinia())

import { i18n } from '@/core/frame/_type/composables/usei18n.ts'
app.use(i18n)

////// registry
// plan card registry
import { createPlanCardRegistry } from '@/core/plans/_type/registries/planCardRegistry.ts'
createPlanCardRegistry()
// module card registry
import { createModuleCardRegistry } from '@/core/modules/_type/registries/moduleCardRegistry.ts'
createModuleCardRegistry()

//// features ////
// system module and flow registry
import '@/features/planManage/registries/registries.ts'

// basic
import '@/features/basic/modules/_type/registries/registries.ts'
// agile
import '@/features/agile/modules/_type/registries/registries.ts'
// mathematics
import '@/features/mathematics/registries/registries.ts'
// language
import '@/features/language/modules/_type/registries/registries.ts'
// relax
import '@/features/relax/registries/registries.ts'
// sample
import '@/features/sample/registries/registries.ts'
// timer
import '@/features/timer/registries/registries.ts'
// divination
import '@/features/divination/modules/_type/registries/registries.ts'
// workshop
import '@/features/workshop/registries/registries.ts'

//// initialize layout
import { useLayoutStore } from '@/core/frame/_type/services/layoutStore.ts'
const layoutStore = useLayoutStore()
layoutStore.initialize()

import { usePanelStore } from '@/core/frame/_type/services/panelStore.ts'
const panelStore = usePanelStore()
panelStore.initializeAllPlans().then(() => panelStore.watchPlanStatus())

app.mount('#app')
