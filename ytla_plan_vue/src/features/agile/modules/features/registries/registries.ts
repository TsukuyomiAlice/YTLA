import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'

import { featuresModuleFlowManager } from '@/features/agile/modules/features/flows/featuresFlowManager.ts'
createModuleFlowRegistry('features', featuresModuleFlowManager)
import { featuresModuleConfig } from '@/features/agile/modules/features/registries/featuresModuleConfig.ts'
createModuleRegistry('features', featuresModuleConfig)
