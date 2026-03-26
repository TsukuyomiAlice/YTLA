import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'

import { relationModuleFlowManager } from '@/features/basic/modules/relation/flows/relationFlowManager.ts'
createModuleFlowRegistry('relation', relationModuleFlowManager)
import { relationModuleConfig } from '@/features/basic/modules/relation/registries/relationModuleConfig.ts'
createModuleRegistry('relation', relationModuleConfig)
