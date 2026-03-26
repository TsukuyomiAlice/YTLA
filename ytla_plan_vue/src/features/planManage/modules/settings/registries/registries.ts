import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'

import { settingsModuleFlowManager } from '@/features/planManage/modules/settings/flows/settingsFlowManager.ts'
createModuleFlowRegistry('settings', settingsModuleFlowManager)
import { settingsModuleConfig } from '@/features/planManage/modules/settings/registries/settingsModuleConfig.ts'
createModuleRegistry('settings', settingsModuleConfig)
