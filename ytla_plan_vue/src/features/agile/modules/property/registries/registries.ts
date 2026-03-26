import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'

import { propertyModuleFlowManager } from '@/features/agile/modules/property/flows/propertyFlowManager.ts'
createModuleFlowRegistry('property', propertyModuleFlowManager)
import { propertyModuleConfig } from '@/features/agile/modules/property/registries/propertyModuleConfig.ts'
createModuleRegistry('property', propertyModuleConfig)
