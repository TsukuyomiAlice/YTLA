import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'

import { navigatorModuleFlowManager } from '@//core/classic/busline/navigator/flows/navigatorFlowManager.ts'
createModuleFlowRegistry('navigator', navigatorModuleFlowManager)
import { navigatorModuleConfig } from '@/core/classic/busline/navigator/registries/navigatorModuleConfig.ts'
createModuleRegistry('navigator', navigatorModuleConfig)

import './navigatorRegistry.ts'

