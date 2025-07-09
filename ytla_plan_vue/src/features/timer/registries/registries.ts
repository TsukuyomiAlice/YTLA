import { createCardEditorFlowRegistry } from '@/core/sideCards/flows/cardEditorFlowRegistry.ts'
import { createCardRegistry } from '@/core/sideCards/registries/cardRegistry.ts'
import { createModuleFlowRegistry } from '@/core/modules/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'

// cards
import { timerCardEditorFlowManager } from '@/features/timer/flows/timerCardFlowManager.ts'
createCardEditorFlowRegistry('timer', timerCardEditorFlowManager)
import { timerCardConfig } from '@/features/timer/registries/timerCardRegistry'
createCardRegistry('timer', timerCardConfig)

// modules
import { timerModuleConfig } from '@/features/timer/registries/timerModuleConfig.ts'
createModuleRegistry('timer', timerModuleConfig)
