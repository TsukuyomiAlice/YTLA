import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/registries/moduleRegistry.ts'

import { timerModuleFlowManager } from '@/features/timer/modules/_type/flows/timerFlowManager.ts'
createModuleFlowRegistry('timer', timerModuleFlowManager)
import { timerModuleConfig } from '@/features/timer/modules/timer/registries/timerModuleConfig.ts'
createModuleRegistry('timer', timerModuleConfig)
