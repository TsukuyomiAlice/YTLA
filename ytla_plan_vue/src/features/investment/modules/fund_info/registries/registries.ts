import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'

import { fund_infoModuleFlowManager } from '@/features/investment/modules/fund_info/flows/fund_infoFlowManager.ts'
createModuleFlowRegistry('fund_info', fund_infoModuleFlowManager)
import { fund_infoModuleConfig } from '@/features/investment/modules/fund_info/registries/fund_infoModuleConfig.ts'
createModuleRegistry('fund_info', fund_infoModuleConfig)

