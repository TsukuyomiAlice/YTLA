import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'

import { ganttChartModuleFlowManager } from '@/features/agile/modules/ganttChart/flows/ganttChartFlowManager.ts'
createModuleFlowRegistry('ganttChart', ganttChartModuleFlowManager)
import { ganttChartModuleConfig } from '@/features/agile/modules/ganttChart/registries/ganttChartModuleConfig.ts'
createModuleRegistry('ganttChart', ganttChartModuleConfig)
