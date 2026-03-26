import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'

import { vsmModuleFlowManager } from '@/features/agile/modules/vsm/flows/vsmFlowManager.ts'
createModuleFlowRegistry('vsm', vsmModuleFlowManager)
import { vsmModuleConfig } from '@/features/agile/modules/vsm/registries/vsmModuleConfig.ts'
createModuleRegistry('vsm', vsmModuleConfig)
