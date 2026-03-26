import { createModuleFlowRegistry } from '@/core/classic/modules/moduleCard/flows/moduleFlowRegistry.ts'
import { createModuleRegistry } from '@/core/classic/modules/moduleCard/factories/moduleRegistry.ts'

import { meetingsModuleFlowManager } from '@/features/agile/modules/meetings/flows/meetingsFlowManager.ts'
createModuleFlowRegistry('meetings', meetingsModuleFlowManager)
import { meetingsModuleConfig } from '@/features/agile/modules/meetings/registries/meetingsModuleConfig.ts'
createModuleRegistry('meetings', meetingsModuleConfig)
