import { createCardEditorFlowRegistry } from '@/core/sideCards/flows/cardEditorFlowRegistry.ts'
import { createCardRegistry } from '@/core/sideCards/registries/cardRegistry.ts'
import { createModuleFlowRegistry } from '@/core/modules/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'

// cards

import { relaxCardEditorFlowManager } from '@/features/relax/flows/relaxCardFlowManager.ts'
createCardEditorFlowRegistry('relax', relaxCardEditorFlowManager)
import { relaxCardConfig } from '@/features/relax/registries/relaxCardConfig.ts'
createCardRegistry('relax', relaxCardConfig)

// modules
