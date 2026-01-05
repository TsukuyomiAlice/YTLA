import { createCardEditorFlowRegistry } from '@/core/classic/cards/sideCardEditor/factories/cardEditorFlowRegistry.ts'
import { createCardRegistry } from '@/core/classic/cards/sideCard/registries/cardRegistry.ts'

import { sampleCardEditorFlowManager } from '@/features/sample/cards/_type/flows/cardEditorFlowManager.ts'
createCardEditorFlowRegistry('sample', sampleCardEditorFlowManager)
import { sampleCardConfig } from '@/features/sample/cards/_type/registries/cardRegistry.ts'
createCardRegistry('sample', sampleCardConfig)
