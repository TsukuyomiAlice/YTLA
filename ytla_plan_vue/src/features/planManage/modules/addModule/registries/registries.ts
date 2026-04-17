import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'

import { addModuleModuleFlowManager } from '@/features/planManage/modules/addModule/flows/addModuleModuleFlowManager.ts'
createModuleFlowRegistry('addModule', addModuleModuleFlowManager)
import { addModuleModuleConfig } from '@/features/planManage/modules/addModule/registries/addModuleModuleConfig.ts'
createModuleRegistry('addModule', addModuleModuleConfig)
