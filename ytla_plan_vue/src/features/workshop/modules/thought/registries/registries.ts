import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'

import { thoughtModuleFlowManager } from '@/features/workshop/modules/thought/flows/thoughtFlowManager.ts'
createModuleFlowRegistry('thought', thoughtModuleFlowManager)
import { thoughtModuleConfig } from '@/features/workshop/modules/thought/registries/thoughtModuleConfig.ts'
createModuleRegistry('thought', thoughtModuleConfig)
