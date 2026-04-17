import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'

import { riskModuleFlowManager } from '@/features/agile/modules/risk/flows/riskFlowManager.ts'
createModuleFlowRegistry('risk', riskModuleFlowManager)
import { riskModuleConfig } from '@/features/agile/modules/risk/registries/riskModuleConfig.ts'
createModuleRegistry('risk', riskModuleConfig)
