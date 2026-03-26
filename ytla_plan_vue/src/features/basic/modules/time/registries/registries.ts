import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'

import { timeModuleFlowManager } from '@/features/basic/modules/time/flows/timeFlowManager.ts'
createModuleFlowRegistry('time', timeModuleFlowManager)
import { timeModuleConfig } from '@/features/basic/modules/time/registries/timeModuleConfig.ts'
createModuleRegistry('time', timeModuleConfig)
