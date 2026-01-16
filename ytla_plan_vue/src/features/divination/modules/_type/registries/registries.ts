import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/registries/moduleRegistry.ts'

import { plumYiModuleFlowManager } from '@/features/divination/modules/plumYi/flows/plumYiFlowManager.ts'
createModuleFlowRegistry('plumYi', plumYiModuleFlowManager)
import { plumYiModuleConfig } from '@/features/divination/modules/plumYi/registries/plumYiModuleConfig.ts'
createModuleRegistry('plumYi', plumYiModuleConfig)
