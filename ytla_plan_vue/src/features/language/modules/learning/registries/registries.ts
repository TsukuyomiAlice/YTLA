import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'

import { learningModuleFlowManager } from '@/features/language/modules/learning/flows/learningFlowManager.ts'
createModuleFlowRegistry('learning', learningModuleFlowManager)
import { learningModuleConfig } from '@/features/language/modules/learning/registries/learningModuleConfig.ts'
createModuleRegistry('learning', learningModuleConfig)
