import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'

import { connectionModuleFlowManager } from '@/features/workshop/modules/connection/flows/connectionFlowManager.ts'
createModuleFlowRegistry('connection', connectionModuleFlowManager)
import { connectionModuleConfig } from '@/features/workshop/modules/connection/registries/connectionModuleConfig.ts'
createModuleRegistry('connection', connectionModuleConfig)
