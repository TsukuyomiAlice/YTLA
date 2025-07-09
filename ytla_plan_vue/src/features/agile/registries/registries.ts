import { createCardEditorFlowRegistry } from '@/core/sideCards/flows/cardEditorFlowRegistry.ts'
import { createCardRegistry } from '@/core/sideCards/registries/cardRegistry.ts'
import { createModuleFlowRegistry } from '@/core/modules/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'

// cards


// modules

import { bibleModuleFlowManager } from '@/features/agile/flows/bibleModuleFlowManager.ts'
createModuleFlowRegistry('bible', bibleModuleFlowManager)
import { bibleModuleConfig } from '@/features/agile/registries/bibleModuleConfig.ts'
createModuleRegistry('bible', bibleModuleConfig)

import { meetingsModuleFlowManager } from '@/features/agile/flows/meetingsFlowManager'
createModuleFlowRegistry('meetings', meetingsModuleFlowManager)
import { meetingsModuleConfig } from '@/features/agile/registries/meetingsModuleConfig.ts'
createModuleRegistry('meetings', meetingsModuleConfig)

import { userStoryModuleFlowManager } from '@/features/agile/flows/userStoryFlowManager'
createModuleFlowRegistry('userStory', userStoryModuleFlowManager)
import { userStoryModuleConfig } from '@/features/agile/registries/userStoryModuleConfig.ts'
createModuleRegistry('userStory', userStoryModuleConfig)

import { whiteboardModuleFlowManager } from '@/features/agile/flows/whiteboardModuleFlowManager.ts'
createModuleFlowRegistry('whiteboard', whiteboardModuleFlowManager)
import { whiteboardModuleConfig } from '@/features/agile/registries/whiteboardModuleConfig.ts'
createModuleRegistry('whiteboard', whiteboardModuleConfig)

import { featuresModuleFlowManager } from '@/features/agile/flows/featuresFlowManager'
createModuleFlowRegistry('features', featuresModuleFlowManager)
import { featuresModuleConfig } from '@/features/agile/registries/featuresModuleConfig.ts'
createModuleRegistry('features', featuresModuleConfig)

import { prototypeModuleFlowManager } from '@/features/agile/flows/prototypeFlowManager'
createModuleFlowRegistry('prototype', prototypeModuleFlowManager)
import { prototypeModuleConfig } from '@/features/agile/registries/prototypeModuleConfig.ts'
createModuleRegistry('prototype', prototypeModuleConfig)

import { vsmModuleFlowManager } from '@/features/agile/flows/vsmFlowManager'
createModuleFlowRegistry('vsm', vsmModuleFlowManager)
import { vsmModuleConfig } from '@/features/agile/registries/vsmModuleConfig.ts'
createModuleRegistry('vsm', vsmModuleConfig)

import { dmdModuleFlowManager } from '@/features/agile/flows/dmdFlowManager'
createModuleFlowRegistry('dmd', dmdModuleFlowManager)
import { dmdModuleConfig } from '@/features/agile/registries/dmdModuleConfig.ts'
createModuleRegistry('dmd', dmdModuleConfig)

import { riskModuleFlowManager } from '@/features/agile/flows/riskFlowManager'
createModuleFlowRegistry('risk', riskModuleFlowManager)
import { riskModuleConfig } from '@/features/agile/registries/riskModuleConfig.ts'
createModuleRegistry('risk', riskModuleConfig)

import { ganttChartModuleFlowManager } from '@/features/agile/flows/ganttChartFlowManager'
createModuleFlowRegistry('ganttChart', ganttChartModuleFlowManager)
import { ganttChartModuleConfig } from '@/features/agile/registries/ganttChartModuleConfig.ts'
createModuleRegistry('ganttChart', ganttChartModuleConfig)

import { backlogModuleFlowManager } from '@/features/agile/flows/backlogFlowManager'
createModuleFlowRegistry('backlog', backlogModuleFlowManager)
import { backlogModuleConfig } from '@/features/agile/registries/backlogModuleConfig.ts'
createModuleRegistry('backlog', backlogModuleConfig)

import { kanbanModuleFlowManager } from '@/features/agile/flows/kanbanModuleFlowManager.ts'
createModuleFlowRegistry('kanban', kanbanModuleFlowManager)
import { kanbanModuleConfig } from '@/features/agile/registries/kanbanModuleConfig.ts'
createModuleRegistry('kanban', kanbanModuleConfig)

import { dashboardModuleFlowManager } from '@/features/agile/flows/dashboardFlowManager'
createModuleFlowRegistry('dashboard', dashboardModuleFlowManager)
import { dashboardModuleConfig } from '@/features/agile/registries/dashboardModuleConfig.ts'
createModuleRegistry('dashboard', dashboardModuleConfig)

import { burndownChartModuleFlowManager } from '@/features/agile/flows/burndownChartFlowManager'
createModuleFlowRegistry('burndownChart', burndownChartModuleFlowManager)
import { burndownChartModuleConfig } from '@/features/agile/registries/burndownChartModuleConfig.ts'
createModuleRegistry('burndownChart', burndownChartModuleConfig)

import { propertyModuleFlowManager } from '@/features/agile/flows/propertyFlowManager'
createModuleFlowRegistry('property', propertyModuleFlowManager)
import { propertyModuleConfig } from '@/features/agile/registries/propertyModuleConfig.ts'
createModuleRegistry('property', propertyModuleConfig)
