import { createCardEditorFlowRegistry } from '@/core/sideCards/_type/flows/cardEditorFlowRegistry.ts'
import { createCardRegistry } from '@/core/sideCards/_type/registries/cardRegistry.ts'
import { createModuleFlowRegistry } from '@/core/modules/_type/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/modules/_type/registries/moduleRegistry.ts'

// cards


// modules

import { plumYiModuleFlowManager } from '@/features/divination/modules/plumYi/flows/plumYiFlowManager.ts'
createModuleFlowRegistry('plumYi', plumYiModuleFlowManager)
import { plumYiModuleConfig } from '@/features/divination/modules/plumYi/registries/plumYiModuleConfig.ts'
createModuleRegistry('plumYi', plumYiModuleConfig)
