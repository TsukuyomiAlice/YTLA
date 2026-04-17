import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'

import { readingsModuleFlowManager } from '@/features/language/modules/readings/flows/readingsFlowManager.ts'
createModuleFlowRegistry('readings', readingsModuleFlowManager)
import { readingsModuleConfig } from '@/features/language/modules/readings/registries/readingsModuleConfig.ts'
createModuleRegistry('readings', readingsModuleConfig)
