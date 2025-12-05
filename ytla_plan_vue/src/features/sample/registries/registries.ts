import { createCardEditorFlowRegistry } from '@/core/sideCards/_type/flows/cardEditorFlowRegistry.ts'
import { createCardRegistry } from '@/core/sideCards/_type/registries/cardRegistry.ts'
import { createModuleFlowRegistry } from '@/core/modules/_type/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/modules/_type/registries/moduleRegistry.ts'

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
