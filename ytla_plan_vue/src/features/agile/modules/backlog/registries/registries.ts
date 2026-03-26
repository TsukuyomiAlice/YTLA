import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'

import { backlogModuleFlowManager } from '@/features/agile/modules/backlog/flows/backlogFlowManager.ts'
createModuleFlowRegistry('backlog', backlogModuleFlowManager)
import { backlogModuleConfig } from '@/features/agile/modules/backlog/registries/backlogModuleConfig.ts'
createModuleRegistry('backlog', backlogModuleConfig)
