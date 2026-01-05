import { createCardEditorFlowRegistry } from '@/core/classic/cards/sideCardEditor/factories/cardEditorFlowRegistry.ts'
import { createCardRegistry } from '@/core/classic/cards/sideCard/registries/cardRegistry.ts'

import { relaxCardEditorFlowManager } from '@/features/relax/cards/_type/flows/relaxCardFlowManager.ts'
createCardEditorFlowRegistry('relax', relaxCardEditorFlowManager)
import { relaxCardConfig } from '@/features/relax/cards/_type/registries/relaxCardConfig.ts'
createCardRegistry('relax', relaxCardConfig)
