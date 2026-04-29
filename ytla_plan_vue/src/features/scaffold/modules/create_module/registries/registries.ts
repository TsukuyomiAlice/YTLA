import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'

import { create_moduleModuleFlowManager } from '@/features/scaffold/modules/create_module/flows/create_moduleFlowManager.ts'
createModuleFlowRegistry('create_module', create_moduleModuleFlowManager)
import { create_moduleModuleConfig } from '@/features/scaffold/modules/create_module/registries/create_moduleModuleConfig.ts'
createModuleRegistry('create_module', create_moduleModuleConfig)

