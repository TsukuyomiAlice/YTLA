import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'

import { data_managerModuleFlowManager } from '@/features/data_power/modules/data_manager/flows/data_managerFlowManager.ts'
createModuleFlowRegistry('data_manager', data_managerModuleFlowManager)
import { data_managerModuleConfig } from '@/features/data_power/modules/data_manager/registries/data_managerModuleConfig.ts'
createModuleRegistry('data_manager', data_managerModuleConfig)

