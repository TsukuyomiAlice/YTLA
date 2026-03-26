import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'

import { kanbanModuleFlowManager } from '@/features/agile/modules/kanban/flows/kanbanModuleFlowManager.ts'
createModuleFlowRegistry('kanban', kanbanModuleFlowManager)
import { kanbanModuleConfig } from '@/features/agile/modules/kanban/registries/kanbanModuleConfig.ts'
createModuleRegistry('kanban', kanbanModuleConfig)
