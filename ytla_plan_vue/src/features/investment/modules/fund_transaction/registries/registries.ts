import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'

import { fund_transactionModuleFlowManager } from '@/features/investment/modules/fund_transaction/flows/fund_transactionFlowManager.ts'
createModuleFlowRegistry('fund_transaction', fund_transactionModuleFlowManager)
import { fund_transactionModuleConfig } from '@/features/investment/modules/fund_transaction/registries/fund_transactionModuleConfig.ts'
createModuleRegistry('fund_transaction', fund_transactionModuleConfig)

