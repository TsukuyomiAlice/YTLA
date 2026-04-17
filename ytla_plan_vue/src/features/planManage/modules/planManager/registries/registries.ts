import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'

import { planManageModuleFlowManager } from '@/features/planManage/modules/planManager/flows/planManageModuleFlowManager.ts'
createModuleFlowRegistry('planManage', planManageModuleFlowManager)
import { planManageModuleConfig } from '@/features/planManage/modules/planManager/registries/planManageModuleConfig.ts'
createModuleRegistry('planManage', planManageModuleConfig)
