import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'

import { dashboardModuleFlowManager } from '@/features/agile/modules/dashboard/flows/dashboardFlowManager.ts'
createModuleFlowRegistry('dashboard', dashboardModuleFlowManager)
import { dashboardModuleConfig } from '@/features/agile/modules/dashboard/registries/dashboardModuleConfig.ts'
createModuleRegistry('dashboard', dashboardModuleConfig)
