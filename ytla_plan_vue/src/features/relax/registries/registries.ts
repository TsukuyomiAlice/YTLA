import { createCardEditorFlowRegistry } from '@/core/sideCards/_type/flows/cardEditorFlowRegistry.ts'
import { createCardRegistry } from '@/core/sideCards/_type/registries/cardRegistry.ts'
import { createModuleFlowRegistry } from '@/core/modules/_type/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/modules/_type/registries/moduleRegistry.ts'

// cards

import { relaxCardEditorFlowManager } from '@/features/relax/flows/relaxCardFlowManager.ts'
createCardEditorFlowRegistry('relax', relaxCardEditorFlowManager)
import { relaxCardConfig } from '@/features/relax/registries/relaxCardConfig.ts'
createCardRegistry('relax', relaxCardConfig)

// modules
