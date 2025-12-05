import { createCardEditorFlowRegistry } from '@/core/sideCards/_type/flows/cardEditorFlowRegistry.ts'
import { createCardRegistry } from '@/core/sideCards/_type/registries/cardRegistry.ts'
import { createModuleFlowRegistry } from '@/core/modules/_type/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/modules/_type/registries/moduleRegistry.ts'

// cards
import { timerCardEditorFlowManager } from '@/features/timer/flows/timerCardFlowManager.ts'
createCardEditorFlowRegistry('timer', timerCardEditorFlowManager)
import { timerCardConfig } from '@/features/timer/registries/timerCardRegistry'
createCardRegistry('timer', timerCardConfig)

// modules
import { timerModuleFlowManager } from '@/features/timer/flows/timerFlowManager'
createModuleFlowRegistry('timer', timerModuleFlowManager)
import { timerModuleConfig } from '@/features/timer/registries/timerModuleConfig'
createModuleRegistry('timer', timerModuleConfig)
