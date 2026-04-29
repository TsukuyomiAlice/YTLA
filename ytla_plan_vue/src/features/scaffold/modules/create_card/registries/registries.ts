import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'

import { create_cardModuleFlowManager } from '@/features/scaffold/modules/create_card/flows/create_cardFlowManager.ts'
createModuleFlowRegistry('create_card', create_cardModuleFlowManager)
import { create_cardModuleConfig } from '@/features/scaffold/modules/create_card/registries/create_cardModuleConfig.ts'
createModuleRegistry('create_card', create_cardModuleConfig)

