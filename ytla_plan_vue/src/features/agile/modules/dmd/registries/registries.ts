import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'

import { dmdModuleFlowManager } from '@/features/agile/modules/dmd/flows/dmdFlowManager.ts'
createModuleFlowRegistry('dmd', dmdModuleFlowManager)
import { dmdModuleConfig } from '@/features/agile/modules/dmd/registries/dmdModuleConfig.ts'
createModuleRegistry('dmd', dmdModuleConfig)
