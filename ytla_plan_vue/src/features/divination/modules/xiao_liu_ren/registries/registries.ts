import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'

import { xiao_liu_renModuleFlowManager } from '@/features/divination/modules/xiao_liu_ren/flows/xiao_liu_renFlowManager.ts'
createModuleFlowRegistry('xiao_liu_ren', xiao_liu_renModuleFlowManager)
import { xiao_liu_renModuleConfig } from '@/features/divination/modules/xiao_liu_ren/registries/xiao_liu_renModuleConfig.ts'
createModuleRegistry('xiao_liu_ren', xiao_liu_renModuleConfig)

