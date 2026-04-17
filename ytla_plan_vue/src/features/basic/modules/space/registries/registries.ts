import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'

import { spaceModuleFlowManager } from '@/features/basic/modules/space/flows/spaceFlowManager.ts'
createModuleFlowRegistry('space', spaceModuleFlowManager)
import { spaceModuleConfig } from '@/features/basic/modules/space/registries/spaceModuleConfig.ts'
createModuleRegistry('space', spaceModuleConfig)
