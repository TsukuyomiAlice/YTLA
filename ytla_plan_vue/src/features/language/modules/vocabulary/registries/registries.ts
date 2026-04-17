import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'

import { vocabularyModuleFlowManager } from '@/features/language/modules/vocabulary/flows/vocabularyFlowManager.ts'
createModuleFlowRegistry('vocabulary', vocabularyModuleFlowManager)
import { vocabularyModuleConfig } from '@/features/language/modules/vocabulary/registries/vocabularyModuleConfig.ts'
createModuleRegistry('vocabulary', vocabularyModuleConfig)
