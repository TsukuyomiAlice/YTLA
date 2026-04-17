import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'

import { assessmentModuleFlowManager } from '@/features/language/modules/assessment/flows/assessmentFlowManager.ts'
createModuleFlowRegistry('assessment', assessmentModuleFlowManager)
import { assessmentModuleConfig } from '@/features/language/modules/assessment/registries/assessmentModuleConfig.ts'
createModuleRegistry('assessment', assessmentModuleConfig)
