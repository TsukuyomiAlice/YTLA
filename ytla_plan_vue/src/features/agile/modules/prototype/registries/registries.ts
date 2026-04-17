import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'

import { prototypeModuleFlowManager } from '@/features/agile/modules/prototype/flows/prototypeFlowManager.ts'
createModuleFlowRegistry('prototype', prototypeModuleFlowManager)
import { prototypeModuleConfig } from '@/features/agile/modules/prototype/registries/prototypeModuleConfig.ts'
createModuleRegistry('prototype', prototypeModuleConfig)
