import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'

import { eight_charactersModuleFlowManager } from '@/features/divination/modules/eight_characters/flows/eight_charactersFlowManager.ts'
createModuleFlowRegistry('eight_characters', eight_charactersModuleFlowManager)
import { eight_charactersModuleConfig } from '@/features/divination/modules/eight_characters/registries/eight_charactersModuleConfig.ts'
createModuleRegistry('eight_characters', eight_charactersModuleConfig)

