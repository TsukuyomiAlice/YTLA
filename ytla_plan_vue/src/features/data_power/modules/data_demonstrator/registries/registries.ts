import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'

import { data_demonstratorModuleFlowManager } from '@/features/data_power/modules/data_demonstrator/flows/data_demonstratorFlowManager.ts'
createModuleFlowRegistry('data_demonstrator', data_demonstratorModuleFlowManager)
import { data_demonstratorModuleConfig } from '@/features/data_power/modules/data_demonstrator/registries/data_demonstratorModuleConfig.ts'
createModuleRegistry('data_demonstrator', data_demonstratorModuleConfig)

