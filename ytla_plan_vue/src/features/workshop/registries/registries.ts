import { createCardEditorFlowRegistry } from '@/core/sideCards/_type/flows/cardEditorFlowRegistry.ts'
import { createCardRegistry } from '@/core/sideCards/_type/registries/cardRegistry.ts'
import { createModuleFlowRegistry } from '@/core/modules/_type/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/modules/_type/registries/moduleRegistry.ts'

// cards


// modules

import { thoughtModuleFlowManager } from '@/features/workshop/flows/thoughtFlowManager'
createModuleFlowRegistry('thought', thoughtModuleFlowManager)
import { thoughtModuleConfig } from '@/features/workshop/registries/thoughtModuleConfig'
createModuleRegistry('thought', thoughtModuleConfig)

import { connectionModuleFlowManager } from '@/features/workshop/flows/connectionFlowManager'
createModuleFlowRegistry('connection', connectionModuleFlowManager)
import { connectionModuleConfig } from '@/features/workshop/registries/connectionModuleConfig'
createModuleRegistry('connection', connectionModuleConfig)

import { functionModuleFlowManager } from '@/features/workshop/flows/functionFlowManager'
createModuleFlowRegistry('function', functionModuleFlowManager)
import { functionModuleConfig } from '@/features/workshop/registries/functionModuleConfig'
createModuleRegistry('function', functionModuleConfig)
