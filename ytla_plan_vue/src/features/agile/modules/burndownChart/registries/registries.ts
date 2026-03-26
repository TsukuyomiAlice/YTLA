import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'

import { burndownChartModuleFlowManager } from '@/features/agile/modules/burndownChart/flows/burndownChartFlowManager.ts'
createModuleFlowRegistry('burndownChart', burndownChartModuleFlowManager)
import { burndownChartModuleConfig } from '@/features/agile/modules/burndownChart/registries/burndownChartModuleConfig.ts'
createModuleRegistry('burndownChart', burndownChartModuleConfig)
