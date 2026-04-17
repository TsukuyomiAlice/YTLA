import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'

import { timerModuleFlowManager } from '@/features/timer/modules/timer/flows/timerModuleFlowManager.ts'
createModuleFlowRegistry('timer', timerModuleFlowManager)
import { timerModuleConfig } from '@/features/timer/modules/timer/registries/timerModuleConfig.ts'
createModuleRegistry('timer', timerModuleConfig)
