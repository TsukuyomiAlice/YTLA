import { createCardEditorFlowRegistry } from '@/core/domain/area/cards/flows/cardEditorFlowRegistry.ts'
import { createCardRegistry } from '@/core/domain/area/cards/registries/cardRegistry.ts'
import { createModuleFlowRegistry } from '@/core/domain/area/modules/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/domain/area/modules/registries/moduleRegistry.ts'

// cards


// modules

import { thoughtModuleFlowManager } from '@/features/workshop/modules/thought/flows/thoughtFlowManager.ts'
createModuleFlowRegistry('thought', thoughtModuleFlowManager)
import { thoughtModuleConfig } from '@/features/workshop/modules/thought/registries/thoughtModuleConfig.ts'
createModuleRegistry('thought', thoughtModuleConfig)

import { connectionModuleFlowManager } from '@/features/workshop/modules/connection/flows/connectionFlowManager.ts'
createModuleFlowRegistry('connection', connectionModuleFlowManager)
import { connectionModuleConfig } from '@/features/workshop/modules/connection/registries/connectionModuleConfig.ts'
createModuleRegistry('connection', connectionModuleConfig)

import { functionModuleFlowManager } from '@/features/workshop/modules/function/flows/functionFlowManager.ts'
createModuleFlowRegistry('function', functionModuleFlowManager)
import { functionModuleConfig } from '@/features/workshop/modules/function/registries/functionModuleConfig.ts'
createModuleRegistry('function', functionModuleConfig)
