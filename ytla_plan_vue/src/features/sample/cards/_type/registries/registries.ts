import { createCardEditorFlowRegistry } from '@/core/domain/area/cards/flows/cardEditorFlowRegistry.ts'
import { createCardRegistry } from '@/core/domain/area/cards/registries/cardRegistry.ts'

import { sampleCardEditorFlowManager } from '@/features/sample/cards/_type/flows/sampleCardFlowManager.ts'
createCardEditorFlowRegistry('sample', sampleCardEditorFlowManager)
import { sampleCardConfig } from '@/features/sample/cards/_type/registries/sampleCardRegistry'
createCardRegistry('sample', sampleCardConfig)
