import { createCardEditorFlowRegistry } from '@/core/sideCards/flows/cardEditorFlowRegistry.ts'
import { createCardRegistry } from '@/core/sideCards/registries/cardRegistry.ts'
import { createModuleFlowRegistry } from '@/core/modules/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/modules/registries/moduleRegistry.ts'

// cards


// modules

import { sphereModuleFlowManager } from '@/features/mathematics/flows/sphereFlowManager'
createModuleFlowRegistry('sphere', sphereModuleFlowManager)
import { sphereModuleConfig } from '@/features/mathematics/registries/sphereModuleConfig.ts'
createModuleRegistry('sphere', sphereModuleConfig)

import { matrixModuleFlowManager } from '@/features/mathematics/flows/matrixFlowManager'
createModuleFlowRegistry('matrix', matrixModuleFlowManager)
import { matrixModuleConfig } from '@/features/mathematics/registries/matrixModuleConfig'
createModuleRegistry('matrix', matrixModuleConfig)
