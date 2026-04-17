import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'

import { planDashboardModuleFlowManager } from '@/features/planManage/modules/planDashboard/flows/planDashboardModuleFlowManager.ts'
createModuleFlowRegistry('planDashboard', planDashboardModuleFlowManager)
import { planDashboardModuleConfig } from '@/features/planManage/modules/planDashboard/registries/planDashboardModuleConfig.ts'
createModuleRegistry('planDashboard', planDashboardModuleConfig)
