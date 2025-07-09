import { createCardEditorFlowRegistry } from '@/core/sideCards/flows/cardEditorFlowRegistry.ts'
import { createCardRegistry } from '@/core/sideCards/registries/cardRegistry.ts'
import { createModuleFlowRegistry } from '@/core/modules/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'

// cards


// modules

import { plumYiModuleFlowManager } from '@/features/divination/flows/plumYiFlowManager'
createModuleFlowRegistry('plumYi', plumYiModuleFlowManager)
import { plumYiModuleConfig } from '@/features/divination/registries/plumYiModuleConfig.ts'
createModuleRegistry('plumYi', plumYiModuleConfig)
