import './assets/main.css'
import '@fortawesome/fontawesome-free/css/all.min.css'

// app
import { createApp } from 'vue'
import App from './App.vue'
const app = createApp(App)

import { createPinia } from 'pinia'
app.use(createPinia())

import { i18n } from '@/core/frame/composables/usei18n.ts'
app.use(i18n)

////// registry
// plan card registry
import { createPlanCardRegistry } from '@/core/plans/registries/planCardRegistry.ts'
createPlanCardRegistry()
// module card registry
import { createModuleCardRegistry } from '@/core/modules/registries/moduleCardRegistry.ts'
createModuleCardRegistry()

import { createCardRegistry } from '@/core/cards/registries/cardRegistry.ts'

import { registerModuleFlowManager } from '@/core/modules/flows/moduleFlowRegistry.ts'

//// card ////
// card (type) registry
import { sampleCardRegistry } from '@/features/sample/registries/sampleCardRegistry'
createCardRegistry('sample', sampleCardRegistry)
import { timerCardRegistry } from '@/features/timer/registries/timerCardRegistry'
createCardRegistry('timer', timerCardRegistry)
import { relaxCardRegistry } from '@/features/relax/registries/relaxCardRegistry'
createCardRegistry('relax', relaxCardRegistry)

// card editor flow (for creation and edit) registry
import { registerCardEditorFlowManager } from '@/core/cards/flows/cardEditorFlowRegistry.ts'
import { sampleCardEditorFlowManager } from '@/features/sample/flows/sampleCardFlowManager.ts'
registerCardEditorFlowManager('sample', sampleCardEditorFlowManager)
import { timerCardEditorFlowManager } from '@/features/timer/flows/timerCardFlowManager.ts'
registerCardEditorFlowManager('timer', timerCardEditorFlowManager)
import { relaxCardEditorFlowManager } from '@/features/relax/flows/relaxCardFlowManager.ts'
registerCardEditorFlowManager('relax', relaxCardEditorFlowManager)

//// module ////
// system module and flow registry
import { welcomeModuleFlowManager } from '@/features/planManage/flows/welcomeModuleFlowManager.ts'
registerModuleFlowManager('welcome', welcomeModuleFlowManager)
import '@/features/planManage/registries/welcomeModuleRegistry'

import { planManageModuleFlowManager } from '@/features/planManage/flows/planManageModuleFlowManager.ts'
registerModuleFlowManager('planManage', planManageModuleFlowManager)
import '@/features/planManage/registries/planManageModuleRegistry.ts'

import { planDashboardModuleFlowManager } from '@/features/planManage/flows/planDashboardModuleFlowManager.ts'
registerModuleFlowManager('planDashboard', planDashboardModuleFlowManager)
import '@/features/planManage/registries/planDashboardModuleRegistry.ts'

import { addModuleModuleFlowManager } from '@/features/planManage/flows/addModuleModuleFlowManager.ts'
registerModuleFlowManager('addModule', addModuleModuleFlowManager)
import '@/features/planManage/registries/addModuleModuleRegistry'

import { settingsModuleFlowManager } from '@/features/planManage/flows/settingsFlowManager'
registerModuleFlowManager('settings', settingsModuleFlowManager)
import '@/features/planManage/registries/settingsModuleRegistry'

// basic module and flow registry
import { timeModuleFlowManager } from '@/features/basic/flows/timeFlowManager'
registerModuleFlowManager('time', timeModuleFlowManager)
import '@/features/basic/registries/timeModuleRegistry'
import { spaceModuleFlowManager } from '@/features/basic/flows/spaceFlowManager'
registerModuleFlowManager('space', spaceModuleFlowManager)
import '@/features/basic/registries/spaceModuleRegistry'
import { definitionModuleFlowManager } from '@/features/basic/flows/definitionFlowManager'
registerModuleFlowManager('definition', definitionModuleFlowManager)
import '@/features/basic/registries/definitionModuleRegistry'
import { relationModuleFlowManager } from '@/features/basic/flows/relationFlowManager'
registerModuleFlowManager('relation', relationModuleFlowManager)
import '@/features/basic/registries/relationModuleRegistry'
import { interactionModuleFlowManager } from '@/features/basic/flows/interactionFlowManager'
registerModuleFlowManager('interaction', interactionModuleFlowManager)
import '@/features/basic/registries/interactionModuleRegistry'

// feature module and flow registry
// agile
import { bibleModuleFlowManager } from '@/features/agile/flows/bibleModuleFlowManager.ts'
registerModuleFlowManager('bible', bibleModuleFlowManager)
import '@/features/agile/registries/bibleModuleRegistry'

import { meetingsModuleFlowManager } from '@/features/agile/flows/meetingsFlowManager'
registerModuleFlowManager('meetings', meetingsModuleFlowManager)
import '@/features/agile/registries/meetingsModuleRegistry'

import { userStoryModuleFlowManager } from '@/features/agile/flows/userStoryFlowManager'
registerModuleFlowManager('userStory', userStoryModuleFlowManager)
import '@/features/agile/registries/userStoryModuleRegistry'

import { whiteboardModuleFlowManager } from '@/features/agile/flows/whiteboardModuleFlowManager.ts'
registerModuleFlowManager('whiteboard', whiteboardModuleFlowManager)
import '@/features/agile/registries/whiteboardModuleRegistry'

import { featuresModuleFlowManager } from '@/features/agile/flows/featuresFlowManager'
registerModuleFlowManager('features', featuresModuleFlowManager)
import '@/features/agile/registries/featuresModuleRegistry'

import { prototypeModuleFlowManager } from '@/features/agile/flows/prototypeFlowManager'
registerModuleFlowManager('prototype', prototypeModuleFlowManager)
import '@/features/agile/registries/prototypeModuleRegistry'

import { vsmModuleFlowManager } from '@/features/agile/flows/vsmFlowManager'
registerModuleFlowManager('vsm', vsmModuleFlowManager)
import '@/features/agile/registries/vsmModuleRegistry'

import { dmdModuleFlowManager } from '@/features/agile/flows/dmdFlowManager'
registerModuleFlowManager('dmd', dmdModuleFlowManager)
import '@/features/agile/registries/dmdModuleRegistry'

import { riskModuleFlowManager } from '@/features/agile/flows/riskFlowManager'
registerModuleFlowManager('risk', riskModuleFlowManager)
import '@/features/agile/registries/riskModuleRegistry'

import { ganttChartModuleFlowManager } from '@/features/agile/flows/ganttChartFlowManager'
registerModuleFlowManager('ganttChart', ganttChartModuleFlowManager)
import '@/features/agile/registries/ganttChartModuleRegistry'

import { backlogModuleFlowManager } from '@/features/agile/flows/backlogFlowManager'
registerModuleFlowManager('backlog', backlogModuleFlowManager)
import '@/features/agile/registries/backlogModuleRegistry'

import { kanbanModuleFlowManager } from '@/features/agile/flows/kanbanModuleFlowManager.ts'
registerModuleFlowManager('kanban', kanbanModuleFlowManager)
import '@/features/agile/registries/kanbanModuleRegistry'

import { dashboardModuleFlowManager } from '@/features/agile/flows/dashboardFlowManager'
registerModuleFlowManager('dashboard', dashboardModuleFlowManager)
import '@/features/agile/registries/dashboardModuleRegistry'

import { burndownChartModuleFlowManager } from '@/features/agile/flows/burndownChartFlowManager'
registerModuleFlowManager('burndownChart', burndownChartModuleFlowManager)
import '@/features/agile/registries/burndownChartModuleRegistry'

import { propertyModuleFlowManager } from '@/features/agile/flows/propertyFlowManager'
registerModuleFlowManager('property', propertyModuleFlowManager)
import '@/features/agile/registries/propertyModuleRegistry'

// language
import { ratingModuleFlowManager } from '@/features/language/flows/ratingFlowManager'
registerModuleFlowManager('rating', ratingModuleFlowManager)
import '@/features/language/registries/ratingModuleRegistry'
import { dictionaryModuleFlowManager } from '@/features/language/flows/dictionaryFlowManager'
registerModuleFlowManager('dictionary', dictionaryModuleFlowManager)
import '@/features/language/registries/dictionaryModuleRegistry'
import { assessmentModuleFlowManager } from '@/features/language/flows/assessmentFlowManager'
registerModuleFlowManager('assessment', assessmentModuleFlowManager)
import '@/features/language/registries/assessmentModuleRegistry'
import { vocabularyModuleFlowManager } from '@/features/language/flows/vocabularyFlowManager'
registerModuleFlowManager('vocabulary', vocabularyModuleFlowManager)
import '@/features/language/registries/vocabularyModuleRegistry'
import { readingsModuleFlowManager } from '@/features/language/flows/readingsFlowManager'
registerModuleFlowManager('readings', readingsModuleFlowManager)
import '@/features/language/registries/readingsModuleRegistry'
import { learningModuleFlowManager } from '@/features/language/flows/learningFlowManager'
registerModuleFlowManager('learning', learningModuleFlowManager)
import '@/features/language/registries/learningModuleRegistry'

// sample
import { sampleModuleFlowManager } from '@/features/sample/flows/sampleModuleFlowManager.ts'
registerModuleFlowManager('sample', sampleModuleFlowManager)
import '@/features/sample/registries/sampleModuleRegistry'

// timer
import '@/features/timer/registries/timerModuleRegistry'

// divination
import { plumYiModuleFlowManager } from '@/features/divination/flows/plumYiFlowManager'
registerModuleFlowManager('plumYi', plumYiModuleFlowManager)
import '@/features/divination/registries/plumYiModuleRegistry'

//// initialize layout
import { useLayoutStore } from '@/core/frame/services/layoutStore.ts'
const layoutStore = useLayoutStore()
layoutStore.initialize()

import { usePanelStore } from '@/core/frame/services/panelStore.ts'
const panelStore = usePanelStore()
panelStore.initializeAllPlans().then(() => panelStore.watchPlanStatus())

app.mount('#app')
