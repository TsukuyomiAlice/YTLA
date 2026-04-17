import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'

import { bibleModuleFlowManager } from '@/features/agile/modules/bible/flows/bibleModuleFlowManager.ts'
createModuleFlowRegistry('bible', bibleModuleFlowManager)
import { bibleModuleConfig } from '@/features/agile/modules/bible/registries/bibleModuleConfig.ts'
createModuleRegistry('bible', bibleModuleConfig)
