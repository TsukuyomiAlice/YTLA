import { createCardEditorFlowRegistry } from '@/core/sideCards/flows/cardEditorFlowRegistry.ts'
import { createCardRegistry } from '@/core/sideCards/registries/cardRegistry.ts'
import { createModuleFlowRegistry } from '@/core/modules/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'

// cards
import { sampleCardEditorFlowManager } from '@/features/sample/flows/sampleCardFlowManager.ts'
createCardEditorFlowRegistry('sample', sampleCardEditorFlowManager)
import { sampleCardConfig } from '@/features/sample/registries/sampleCardRegistry'
createCardRegistry('sample', sampleCardConfig)

// modules

import { sampleModuleFlowManager } from '@/features/sample/flows/sampleModuleFlowManager.ts'
createModuleFlowRegistry('sample', sampleModuleFlowManager)
import { sampleModuleConfig } from '@/features/sample/registries/sampleModuleConfig.ts'
createModuleRegistry('sample', sampleModuleConfig)
