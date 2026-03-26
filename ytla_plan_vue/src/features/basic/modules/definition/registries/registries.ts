import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'

import { definitionModuleFlowManager } from '@/features/basic/modules/definition/flows/definitionFlowManager.ts'
createModuleFlowRegistry('definition', definitionModuleFlowManager)
import { definitionModuleConfig } from '@/features/basic/modules/definition/registries/definitionModuleConfig.ts'
createModuleRegistry('definition', definitionModuleConfig)
