import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'

import { functionModuleFlowManager } from '@/features/workshop/modules/function/flows/functionFlowManager.ts'
createModuleFlowRegistry('function', functionModuleFlowManager)
import { functionModuleConfig } from '@/features/workshop/modules/function/registries/functionModuleConfig.ts'
createModuleRegistry('function', functionModuleConfig)
