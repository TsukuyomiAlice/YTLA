import { createCardEditorFlowRegistry } from '@/core/classic/cards/sideCardEditor/factories/cardEditorFlowRegistry.ts'
import { timerCardEditorFlowManager } from '@/features/timer/cards/_type/flows/timerCardFlowManager.ts'
createCardEditorFlowRegistry('timer', timerCardEditorFlowManager)

import { createCardRegistry } from '@/core/classic/cards/sideCard/factories/cardRegistry.ts'
import { timerCardConfig } from '@/features/timer/cards/_type/registries/cardRegistry.ts'
createCardRegistry('timer', timerCardConfig)
