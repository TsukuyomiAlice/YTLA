import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'

import { plum_yiModuleFlowManager } from '@/features/divination/modules/plum_yi/flows/plum_yiFlowManager.ts'
createModuleFlowRegistry('plum_yi', plum_yiModuleFlowManager)
import { plum_yiModuleConfig } from '@/features/divination/modules/plum_yi/registries/plum_yiModuleConfig.ts'
createModuleRegistry('plum_yi', plum_yiModuleConfig)

