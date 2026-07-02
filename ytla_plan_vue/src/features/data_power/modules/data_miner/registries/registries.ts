import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'

import { data_minerModuleFlowManager } from '@/features/data_power/modules/data_miner/flows/data_minerFlowManager.ts'
createModuleFlowRegistry('data_miner', data_minerModuleFlowManager)
import { data_minerModuleConfig } from '@/features/data_power/modules/data_miner/registries/data_minerModuleConfig.ts'
createModuleRegistry('data_miner', data_minerModuleConfig)

