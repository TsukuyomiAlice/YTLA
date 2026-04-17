import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'

import { ratingModuleFlowManager } from '@/features/language/modules/rating/flows/ratingFlowManager.ts'
createModuleFlowRegistry('rating', ratingModuleFlowManager)
import { ratingModuleConfig } from '@/features/language/modules/rating/registries/ratingModuleConfig.ts'
createModuleRegistry('rating', ratingModuleConfig)
