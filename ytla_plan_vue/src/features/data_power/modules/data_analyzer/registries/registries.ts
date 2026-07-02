import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'

import { data_analyzerModuleFlowManager } from '@/features/data_power/modules/data_analyzer/flows/data_analyzerFlowManager.ts'
createModuleFlowRegistry('data_analyzer', data_analyzerModuleFlowManager)
import { data_analyzerModuleConfig } from '@/features/data_power/modules/data_analyzer/registries/data_analyzerModuleConfig.ts'
createModuleRegistry('data_analyzer', data_analyzerModuleConfig)

