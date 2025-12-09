import { createCardEditorFlowRegistry } from '@/core/domain/area/cards/flows/cardEditorFlowRegistry.ts'
import { createCardRegistry } from '@/core/domain/area/cards/registries/cardRegistry.ts'

import { relaxCardEditorFlowManager } from '@/features/relax/cards/_type/flows/relaxCardFlowManager.ts'
createCardEditorFlowRegistry('relax', relaxCardEditorFlowManager)
import { relaxCardConfig } from '@/features/relax/cards/_type/registries/relaxCardConfig.ts'
createCardRegistry('relax', relaxCardConfig)
