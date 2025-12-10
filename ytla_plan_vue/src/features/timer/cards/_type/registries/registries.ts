import { createCardEditorFlowRegistry } from '@/core/domain/area/cards/flows/cardEditorFlowRegistry.ts'
import { createCardRegistry } from '@/core/domain/area/cards/registries/cardRegistry.ts'

import { timerCardEditorFlowManager } from '@/features/timer/cards/_type/flows/timerCardFlowManager.ts'
createCardEditorFlowRegistry('timer', timerCardEditorFlowManager)
import { timerCardConfig } from '@/features/timer/cards/_type/registries/cardRegistry.ts'
createCardRegistry('timer', timerCardConfig)
