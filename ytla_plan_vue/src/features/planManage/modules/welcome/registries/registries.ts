import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'

import { welcomeModuleFlowManager } from '@/features/planManage/modules/welcome/flows/welcomeModuleFlowManager.ts'
createModuleFlowRegistry('welcome', welcomeModuleFlowManager)
import { welcomeModuleConfig } from '@/features/planManage/modules/welcome/registries/welcomeModuleConfig.ts'
createModuleRegistry('welcome', welcomeModuleConfig)
