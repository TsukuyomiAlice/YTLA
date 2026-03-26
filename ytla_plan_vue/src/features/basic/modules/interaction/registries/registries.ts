import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'

import { interactionModuleFlowManager } from '@/features/basic/modules/interaction/flows/interactionFlowManager.ts'
createModuleFlowRegistry('interaction', interactionModuleFlowManager)
import { interactionModuleConfig } from '@/features/basic/modules/interaction/registries/interactionModuleConfig.ts'
createModuleRegistry('interaction', interactionModuleConfig)
