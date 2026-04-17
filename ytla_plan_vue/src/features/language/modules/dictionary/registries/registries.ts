import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'

import { dictionaryModuleFlowManager } from '@/features/language/modules/dictionary/flows/dictionaryFlowManager.ts'
createModuleFlowRegistry('dictionary', dictionaryModuleFlowManager)
import { dictionaryModuleConfig } from '@/features/language/modules/dictionary/registries/dictionaryModuleConfig.ts'
createModuleRegistry('dictionary', dictionaryModuleConfig)
