import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'

import { userStoryModuleFlowManager } from '@/features/agile/modules/userStory/flows/userStoryFlowManager.ts'
createModuleFlowRegistry('userStory', userStoryModuleFlowManager)
import { userStoryModuleConfig } from '@/features/agile/modules/userStory/registries/userStoryModuleConfig.ts'
createModuleRegistry('userStory', userStoryModuleConfig)
