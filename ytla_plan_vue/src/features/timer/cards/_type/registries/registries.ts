import { createCardEditorFlowRegistry } from '@/core/classic/cards/sideCard/flows/cardEditorFlowRegistry.ts'
import { createCardRegistry } from '@/core/classic/cards/sideCard/registries/cardRegistry.ts'

import { timerCardEditorFlowManager } from '@/features/timer/cards/_type/flows/timerCardFlowManager.ts'
createCardEditorFlowRegistry('timer', timerCardEditorFlowManager)
import { timerCardConfig } from '@/features/timer/cards/_type/registries/cardRegistry.ts'
createCardRegistry('timer', timerCardConfig)
