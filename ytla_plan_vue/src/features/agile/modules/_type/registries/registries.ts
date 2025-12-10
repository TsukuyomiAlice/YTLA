import { createModuleFlowRegistry } from '@/core/domain/area/modules/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/domain/area/modules/registries/moduleRegistry.ts'

import { bibleModuleFlowManager } from '@/features/agile/modules/bible/flows/bibleModuleFlowManager.ts'
createModuleFlowRegistry('bible', bibleModuleFlowManager)
import { bibleModuleConfig } from '@/features/agile/modules/bible/registries/bibleModuleConfig.ts'
createModuleRegistry('bible', bibleModuleConfig)

import { meetingsModuleFlowManager } from '@/features/agile/modules/meetings/flows/meetingsFlowManager.ts'
createModuleFlowRegistry('meetings', meetingsModuleFlowManager)
import { meetingsModuleConfig } from '@/features/agile/modules/meetings/registries/meetingsModuleConfig.ts'
createModuleRegistry('meetings', meetingsModuleConfig)

import { userStoryModuleFlowManager } from '@/features/agile/modules/userStory/flows/userStoryFlowManager.ts'
createModuleFlowRegistry('userStory', userStoryModuleFlowManager)
import { userStoryModuleConfig } from '@/features/agile/modules/userStory/registries/userStoryModuleConfig.ts'
createModuleRegistry('userStory', userStoryModuleConfig)

import { whiteboardModuleFlowManager } from '@/features/agile/modules/whiteboard/flows/whiteboardModuleFlowManager.ts'
createModuleFlowRegistry('whiteboard', whiteboardModuleFlowManager)
import { whiteboardModuleConfig } from '@/features/agile/modules/whiteboard/registries/whiteboardModuleConfig.ts'
createModuleRegistry('whiteboard', whiteboardModuleConfig)

import { featuresModuleFlowManager } from '@/features/agile/modules/features/flows/featuresFlowManager.ts'
createModuleFlowRegistry('features', featuresModuleFlowManager)
import { featuresModuleConfig } from '@/features/agile/modules/features/registries/featuresModuleConfig.ts'
createModuleRegistry('features', featuresModuleConfig)

import { prototypeModuleFlowManager } from '@/features/agile/modules/prototype/flows/prototypeFlowManager.ts'
createModuleFlowRegistry('prototype', prototypeModuleFlowManager)
import { prototypeModuleConfig } from '@/features/agile/modules/prototype/registries/prototypeModuleConfig.ts'
createModuleRegistry('prototype', prototypeModuleConfig)

import { vsmModuleFlowManager } from '@/features/agile/modules/vsm/flows/vsmFlowManager.ts'
createModuleFlowRegistry('vsm', vsmModuleFlowManager)
import { vsmModuleConfig } from '@/features/agile/modules/vsm/registries/vsmModuleConfig.ts'
createModuleRegistry('vsm', vsmModuleConfig)

import { dmdModuleFlowManager } from '@/features/agile/modules/dmd/flows/dmdFlowManager.ts'
createModuleFlowRegistry('dmd', dmdModuleFlowManager)
import { dmdModuleConfig } from '@/features/agile/modules/dmd/registries/dmdModuleConfig.ts'
createModuleRegistry('dmd', dmdModuleConfig)

import { riskModuleFlowManager } from '@/features/agile/modules/risk/flows/riskFlowManager.ts'
createModuleFlowRegistry('risk', riskModuleFlowManager)
import { riskModuleConfig } from '@/features/agile/modules/risk/registries/riskModuleConfig.ts'
createModuleRegistry('risk', riskModuleConfig)

import { ganttChartModuleFlowManager } from '@/features/agile/modules/ganttChart/flows/ganttChartFlowManager.ts'
createModuleFlowRegistry('ganttChart', ganttChartModuleFlowManager)
import { ganttChartModuleConfig } from '@/features/agile/modules/ganttChart/registries/ganttChartModuleConfig.ts'
createModuleRegistry('ganttChart', ganttChartModuleConfig)

import { backlogModuleFlowManager } from '@/features/agile/modules/backlog/flows/backlogFlowManager.ts'
createModuleFlowRegistry('backlog', backlogModuleFlowManager)
import { backlogModuleConfig } from '@/features/agile/modules/backlog/registries/backlogModuleConfig.ts'
createModuleRegistry('backlog', backlogModuleConfig)

import { kanbanModuleFlowManager } from '@/features/agile/modules/kanban/flows/kanbanModuleFlowManager.ts'
createModuleFlowRegistry('kanban', kanbanModuleFlowManager)
import { kanbanModuleConfig } from '@/features/agile/modules/kanban/registries/kanbanModuleConfig.ts'
createModuleRegistry('kanban', kanbanModuleConfig)

import { dashboardModuleFlowManager } from '@/features/agile/modules/dashboard/flows/dashboardFlowManager.ts'
createModuleFlowRegistry('dashboard', dashboardModuleFlowManager)
import { dashboardModuleConfig } from '@/features/agile/modules/dashboard/registries/dashboardModuleConfig.ts'
createModuleRegistry('dashboard', dashboardModuleConfig)

import { burndownChartModuleFlowManager } from '@/features/agile/modules/burndownChart/flows/burndownChartFlowManager.ts'
createModuleFlowRegistry('burndownChart', burndownChartModuleFlowManager)
import { burndownChartModuleConfig } from '@/features/agile/modules/burndownChart/registries/burndownChartModuleConfig.ts'
createModuleRegistry('burndownChart', burndownChartModuleConfig)

import { propertyModuleFlowManager } from '@/features/agile/modules/property/flows/propertyFlowManager.ts'
createModuleFlowRegistry('property', propertyModuleFlowManager)
import { propertyModuleConfig } from '@/features/agile/modules/property/registries/propertyModuleConfig.ts'
createModuleRegistry('property', propertyModuleConfig)
