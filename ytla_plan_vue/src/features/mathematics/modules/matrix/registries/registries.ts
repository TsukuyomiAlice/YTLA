import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'

import { matrixModuleFlowManager } from '@/features/mathematics/modules/matrix/flows/matrixFlowManager'
createModuleFlowRegistry('matrix', matrixModuleFlowManager)
import { matrixModuleConfig } from '@/features/mathematics/modules/matrix/registries/matrixModuleConfig'
createModuleRegistry('matrix', matrixModuleConfig)
