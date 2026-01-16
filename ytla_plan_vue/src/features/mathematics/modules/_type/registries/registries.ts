import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/registries/moduleRegistry.ts'

import { sphereModuleFlowManager } from '@/features/mathematics/modules/sphere/flows/sphereFlowManager'
createModuleFlowRegistry('sphere', sphereModuleFlowManager)
import { sphereModuleConfig } from '@/features/mathematics/modules/sphere/registries/sphereModuleConfig.ts'
createModuleRegistry('sphere', sphereModuleConfig)

import { matrixModuleFlowManager } from '@/features/mathematics/modules/matrix/flows/matrixFlowManager'
createModuleFlowRegistry('matrix', matrixModuleFlowManager)
import { matrixModuleConfig } from '@/features/mathematics/modules/matrix/registries/matrixModuleConfig'
createModuleRegistry('matrix', matrixModuleConfig)
